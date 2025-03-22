# Import relavent libraries
import pandas as pd
import numpy as np

def par():
    print("\n\n\n")

def is_subset(row1, row2):
    return set(row1).issubset(set(row2))

# Read the CSV file into a DataFrame: netflix_titles
nt = pd.read_csv("netflix_titles.csv")

# Read the CSV file into a DataFrame: content_production_countries
cpc = pd.read_csv("content_production_countries.csv")

# Create a deep copy of cpc
cpc_staging = cpc.copy(deep=True)

# Clean the [] and '' in cpc_staging
cpc_staging[['cast', 'director', 'country']] = cpc_staging[['cast', 'director', 'country']].apply(lambda x: x.str.strip("[]").str.replace("'", ""))

# Drop all rows in cpc_staging where the cast, director and country are all empty lists
cpc_staging = cpc_staging.drop(
    cpc[
        (cpc_staging["cast"] == '') &
        (cpc_staging["director"] == '') & 
        (cpc_staging["country"] == "Unknown")
    ].index
)

# Percentage of countries listed as "Unknown"
unknown_countries = cpc_staging["country"].loc[cpc_staging["country"] == "Unknown"].count() / cpc_staging["country"].count() * 100

# View tables with relevant data
## View cpc staging table with the country listed as ["Unknown"]
print(cpc_staging[["name", "cast", "director", "country"]].loc[cpc_staging["country"] == "Unknown"])
par()

## View nt table without the countries listed as NaN
print(nt[["title", "director", "cast", "country"]].loc[~nt["country"].isnull()])
par()

# Join tables nt and cpc_staging where the following conditions are met
# - The cast members match
# - cpc_stagin["cast"] is a subset of nt["cast"] and cpc_staging["director"] == nt["director"] DONE
# - nt["cast"] is a subset of cpc_staging["cast"] and cpc_staging["director"] == nt["director"] DONE
# - The titles names match and cpc_staging["director"] == nt["director"] DONE
cross_joined_df = (
    cpc_staging[["name", "cast", "director", "country"]].loc[cpc_staging["country"] == "Unknown"]
    .merge(
        nt[["title", "director", "cast", "country"]].loc[~nt["country"].isnull()], 
        how='cross',
        suffixes=('_cpc', '_nt')
    )
)
cross_joined_df = cross_joined_df.astype(str)

df = cross_joined_df.loc[
    (cross_joined_df.apply(lambda row: is_subset(row['cast_cpc'], row['cast_nt']), axis=1) &
    cross_joined_df.apply(lambda row: is_subset(row['cast_nt'], row['cast_cpc']), axis=1))
]

'''df = (
    cross_joined_df
    .loc[
        (cross_joined_df["director_cpc"] == cross_joined_df["director_nt"]) & 
        (
            cross_joined_df.apply(lambda row: is_subset(row['cast_cpc'], row['cast_nt']), axis=1) |
            cross_joined_df.apply(lambda row: is_subset(row['cast_nt'], row['cast_cpc']), axis=1) |
            cross_joined_df["name"] == cross_joined_df["title"]
        )
    ]
)'''

print(df)