import requests
import pandas as pd
import itertools

netflix_titles = pd.read_csv("netflix_titles.csv")  
condensed_netflix_data = netflix_titles[["show_id", "title", "cast", "director"]]

API_KEY = "254bbff2d20f7cae857f0d6bd9e2306e"
content_names = (
    netflix_titles.loc[
        netflix_titles["country"].isna() &
        ~netflix_titles["title"].str.lower().isin(
            [
                "black holes | the edge of all we know", 
                "paradise hills",
                "ginny & georgia - the afterparty"
            ]
        )
    ]["title"]
    .str.lower()
    .tolist()
)

names = []
countries = []
meta_cast_list = []
meta_directors = []
meta_content_ids = []
counter = 0

for content_name in content_names:
    content_type = "movie"

    url = f"https://api.themoviedb.org/3/search/multi?api_key={API_KEY}&query={content_name}"
    
    response = requests.get(url)
    data = response.json()

    country = data.get("production_countries", [])
    content_ids = []

    for content in data["results"]:
        # Check if the ID is a movie
        movie_url = f"https://api.themoviedb.org/3/movie/{content["id"]}?api_key={API_KEY}"
        movie_response = requests.get(movie_url)

        # Check if the ID is a TV show
        tv_url = f"https://api.themoviedb.org/3/tv/{content["id"]}?api_key={API_KEY}"
        tv_response = requests.get(tv_url)

        if movie_response.status_code == 200:
            content_type = "movie"
        elif tv_response.status_code == 200:
            content_type = "tv"

        url = f"https://api.themoviedb.org/3/{content_type}/{content['id']}/credits?api_key={API_KEY}"
        response = requests.get(url)
        content_data = response.json()
        cast_list = []
        content_ids.append(content["id"])
        try:
            for cast_data in content_data["cast"]:
                cast_list.append(cast_data["name"])
            meta_cast_list.append(cast_list)
        except KeyError:
            meta_cast_list.append([])

    for content_id in content_ids:
        url = f"https://api.themoviedb.org/3/{content_type}/{content_id}?api_key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        name = data.get("original_title", [])
        names.append(name)

        country = data.get("production_countries", [])
        if country == []:
            countries.append(["Unknown"])
        else:
            countries.append(country[0]["name"])

    for content_id in content_ids:
        url = f"https://api.themoviedb.org/3/{content_type}/{content_id}/credits?api_key={API_KEY}"
        response = requests.get(url)
        data = response.json()
        director = data.get("crew", [])
        directors = []
        for crew_member in director:
            if crew_member["job"] == "Director":
                directors.append(crew_member["name"])
        meta_directors.append(directors)

    meta_content_ids.append(content_ids)

    print(f"Counter: {counter}, {content_name}")
    counter += 1

meta_content_ids = list(itertools.chain(*meta_content_ids))


print("----CAST LIST----")
print(meta_cast_list)
for cast in meta_cast_list:
    print(cast)
print("size of meta_cast_list", len(meta_cast_list))
print("\n\n\n")

print("----COUNTRIES----")
print(countries)
print("size of countries", len(countries))
print("\n\n\n")

print("----DIRECTORS----")
print(meta_directors)
print("size of meta_directors", len(meta_directors))
print("\n\n\n")

print("----MOVIE IDS----")
print(meta_content_ids)
print("size of meta_content_ids", len(meta_content_ids))
print("\n\n\n")

print("----NAME----")
print(names)
print("size of names", len(names))
print("\n\n\n")

print("----FINAL DATA----")
data = pd.DataFrame(
    {
        "content_id": meta_content_ids, 
        "name": names,
        "cast": meta_cast_list, 
        "director": meta_directors, 
        "country": countries
    }
)

# Filter the DataFrame
data_refined = (
    data
    .loc[
        data["name"].str
        .lower()
        .isin(content_names)
    ]
)
data_refined = data_refined.to_csv("data_refined.csv", index=False)
print(data_refined)