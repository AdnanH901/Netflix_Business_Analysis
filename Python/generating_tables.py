# Import relevant libraries
from faker import Faker
import random
import pandas as pd
import numpy as np
from IPython.display import display

fake = Faker(locale="en_US")

# Extracted using AI from: https://flixpatrol.com/streaming-service/netflix/subscribers/by-value/#list

subscribers_dict = {
    "Albania": 90489,
    "Algeria": 60000,
    "Angola": 30163,
    "Argentina": 6334230,
    "Armenia": 30163,
    "Australia": 6937490,
    "Austria": 1508150,
    "Azerbaijan": 60326,
    "Bahamas": 60326,
    "Bahrain": 90489,
    "Bangladesh": 301630,
    "Belgium": 2262225,
    "Bolivia": 271467,
    "Bosnia and Herzegovina": 120652,
    "Brazil": 16589650,
    "Bulgaria": 331793,
    "Canada": 9048900,
    "Chile": 2413040,
    "Colombia": 6032600,
    "Costa Rica": 452445,
    "Croatia": 211141,
    "Czech Republic": 935053,
    "Denmark": 1658965,
    "Dominican Republic": 1206520,
    "Ecuador": 904890,
    "Egypt": 90489,
    "Estonia": 120652,
    "Ethiopia": 30163,
    "Finland": 1236683,
    "France": 13573350,
    "Germany": 16589650,
    "Greece": 904890,
    "Guatemala": 211141,
    "Guyana": 60326,
    "Honduras": 150815,
    "Hong-Kong": 1206520,
    "Hungary": 965216,
    "Iceland": 90489,
    "India": 12366830,
    "Indonesia": 4222820,
    "Ireland": 1357335,
    "Israel": 754075,
    "Italy": 5730970,
    "Jamaica": 90489,
    "Japan": 9048900,
    "Kenya": 90489,
    "Kuwait": 301630,
    "Latvia": 180978,
    "Lithuania": 211141,
    "Luxembourg": 211141,
    "Malaysia": 2262225,
    "Malta": 60326,
    "Mexico": 13874980,
    "Moldova": 60326,
    "Montenegro": 30163,
    "Netherlands": 4222820,
    "New Zealand": 1206520,
    "Nicaragua": 90489,
    "Nigeria": 150815,
    "North Macedonia": 60326,
    "Norway": 1598639,
    "Oman": 180978,
    "Panama": 452445,
    "Paraguay": 452445,
    "Peru": 1809780,
    "Philippines": 2714670,
    "Poland": 3921190,
    "Portugal": 1206520,
    "Qatar": 150815,
    "Romania": 1176357,
    "Salvador": 150815,
    "Saudi Arabia": 1809780,
    "Serbia": 271467,
    "Singapore": 1809780,
    "Slovakia": 422282,
    "Slovenia": 211141,
    "South Africa": 1206520,
    "South Korea": 8355151,
    "Spain": 7842380,
    "Suriname": 30163,
    "Sweden": 2413040,
    "Switzerland": 2413040,
    "Taiwan": 2413040,
    "Thailand": 2111410,
    "Trinidad and Tobago": 150815,
    "Tunisia": 60326,
    "Turkey": 3740212,
    "Ukraine": 512771,
    "United Arab Emirates": 452445,
    "United Kingdom": 18399430,
    "United States": 81440100,
    "Uruguay": 452445,
    "Venezuela": 301630,
    "Vietnam": 1206520,
}

# Collected from: https://money.cnn.com/2016/01/06/media/netflix-global-launch-countries/

netflix_countries = [
    "Afghanistan", "Albania", "Algeria", "American Samoa", "Andorra", "Angola", "Anguilla", 
    "Antigua and Barbuda", "Argentina", "Armenia", "Aruba", "Australia", "Australian Antarctica", 
    "Austria", "Azerbaijan", "Bahamas", "Bahrain", "Bangladesh", "Barbados", "Belarus", "Belgium", 
    "Belize", "Benin (Dahomey)", "Bermuda", "Bhutan", "Bolivia", "Bonaire, Sint Eustatius and Saba", 
    "Bosnia and Herzegovina", "Botswana", "Brazil", "British Guyana", "British Indian Ocean Territory", 
    "British Virgin Islands", "Brunei Darussalam", "Bulgaria", "Burkina Faso (Upper Volta)", "Burundi", 
    "Cambodia (Kampuchea)", "Cameroon", "Canada", "Cape Verde Islands (Cabo Verde)", "Cayman Islands", 
    "Central African Republic", "Chad", "Chile", "Christmas Island", "Cocos (Keeling) Islands", "Colombia", 
    "Comoros", "Cook Islands", "Costa Rica", "Croatia", "Cuba", "Curaçao", "Cyprus", "Czech Republic", 
    "Democratic Republic of Congo", "Denmark", "Djibouti Republic", "Dominica", "Dominican Republic", 
    "East Timor (Timor-Leste)", "Ecuador", "Egypt", "El Salvador", "Equatorial Guinea", "Eritrea", 
    "Estonia", "Ethiopia", "Falkland Islands", "Faroe Islands", "Fijian Islands", "Finland", "France", 
    "French Guiana", "French Polynesia", "Gabon", "Gambia", "Georgia", "Germany", "Ghana", "Gibraltar", 
    "Greece", "Greenland", "Grenada", "Guadeloupe", "Guam", "Guatemala", "Guernsey", "Guinea", "Guinea-Bissau", 
    "Haiti", "Heard Island and McDonald Islands", "Honduras", "Hong Kong", "Hungary", "Iceland", "India", 
    "Indonesia", "Iran", "Iraq", "Ireland", "Isle Of Man", "Israel", "Italy", "Ivory Coast (Cote d'Ivoire)", 
    "Jamaica", "Japan", "Jersey", "Jordan", "Kazakhstan", "Kenya", "Kiribati", "Kuwait", "Kyrgyzstan", 
    "Lao People's Democratic Republic", "Latvia", "Lebanon", "Lesotho", "Liberia", "Libya", "Liechtenstein", 
    "Lithuania", "Luxembourg", "Macao", "Macedonia", "Madagascar", "Malawi", "Malaysia", "Maldives", "Mali", 
    "Malta", "Marshall Islands", "Martinique", "Mauritania", "Mauritius", "Mayotte", "Mexico", "Micronesia", 
    "Moldova", "Monaco", "Mongolia", "Montenegro", "Montserrat", "Morocco", "Mozambique", "Myanmar (Burma)", 
    "Namibia", "Nauru", "Nepal", "Netherlands", "Netherlands Antilles", "New Caledonia", "New Zealand", 
    "Nicaragua", "Niger", "Nigeria", "Niue", "Norfolk Island", "Northern Mariana Islands", "Norway", "Oman", 
    "Pakistan", "Palau", "Palestine", "Panama", "Papua New Guinea", "Paraguay", "Peru", "Philippines", 
    "Pitcairn Islands", "Poland", "Portugal", "Puerto Rico", "Qatar", "Republic of the Congo", "Réunion", 
    "Romania", "Russian Federation", "Rwanda", "Saint Barthélemy", "Saint Helena, Ascension and Tristan da Cunha", 
    "Saint Kitts And Nevis", "Saint Lucia", "Saint Martin", "Saint Pierre and Miquelon", 
    "Saint Vincent And The Grenadines", "Samoa", "San Marino", "Sao Tome and Principe", "Saudi Arabia", 
    "Senegal", "Seychelles", "Sierra Leone", "Singapore", "Sint Maarten", "Slovakia", "Slovenia", "Solomon Islands", 
    "Somalia", "South Africa", "South Georgia and the South Sandwich Islands", "South Korea (Republic of Korea)", 
    "South Sudan", "Spain", "Sri Lanka (Ceylon)", "Sudan", "Suriname", "Swaziland", "Sweden", "Switzerland", 
    "Syria (Syrian Arab Republic)", "Taiwan", "Tajikistan", "Tanzania", "Thailand", "Togo", "Tokelau Islands", 
    "Tonga", "Trinidad and Tobago", "Tunisia", "Turkey", "Turkmenistan", "Turks And Caicos Islands", "Tuvalu", 
    "U.S. Virgin Islands (St. Croix, St. John, St. Thomas)", "Uganda", "Ukraine", "United Arab Emirates", 
    "United Kingdom (Great Britain)", "United States", "United States Minor Outlying Islands (Baker Island, Midway Atoll, Wake Island)", 
    "Uruguay", "Uzbekistan", "Vanuatu (New Hebrides)", "Vatican City (Holy See)", "Venezuela", "Vietnam", 
    "Wallis and Futuna", "Western Sahara", "Yemen", "Zambia", "Zimbabwe"
]

leftover_countries = [country for country in netflix_countries if country not in list(subscribers_dict.keys())]

for country in leftover_countries:
    subscribers_dict[country] = min(subscribers_dict.values())

countryKeys = list(subscribers_dict.keys())
countryKeys.sort()

# Sorted Dictionary
subscribers_dict = {country: subscribers_dict[country] for country in countryKeys}
netflix_countries = list(subscribers_dict.keys())
subscribers = list(subscribers_dict.values())

netflix_gallery = pd.read_csv("netflix_titles.csv")

def generate_customer_data(rows_count) -> pd.DataFrame:
    data = []
    for row_num in range(1, rows_count+1):
        data_dict = {}
        start_date = fake.date()
        end_date = fake.date()
        age_range = [i for i in range(18, 79)]
        netflix_churn_rate = 1.8 # 1.8% churn rate according to studies

        data_dict["customer_id"] = row_num
        data_dict["subscription_start_date"] = start_date
        
        while end_date < start_date:
            end_date = fake.date()
            
        data_dict["subscription_end_date"] = random.choices(
            (end_date, None), 
            weights = [netflix_churn_rate, 100 - netflix_churn_rate]
        )[0] 
        data_dict["subscription_plan"] = random.choices(
            ["Standard (with adverts)", "Standard", "Premium"],
            weights=[6, 3, 1]
        )[0]
        data_dict["payment_method"] = random.choices(
            [
                "Credit/Debit Cards", 
                "PayPal", 
                "Netflix Gift Cards", 
                "Partner Billing", 
                "Prepaid/Virtual Cards",
                "Other Methods"
            ], 
            weights = [60, 20, 10, 5, 3, 2]
        )[0]
        data_dict["country"] = random.choices(
            netflix_countries,
            weights=subscribers
        )[0]
        data_dict["age"] = random.choices(age_range, weights=[
                333 if 18 <= age and age < 28 else 
                182 if 28 <= age and age < 44 else
                263 if 44 <= age and age < 60 else
                222
                for age in age_range
            ]
        )[0]
        data_dict["gender"] = random.choices(["male", "female"], weights=[49, 51])[0]
        
        data.append(data_dict)
    return pd.DataFrame(data)

def generate_viewing_behaviour_data(rows_count, customer_data, netflix_gallery) -> pd.DataFrame:
    data = []
    for i in range(rows_count):
        data_dict = {}
        customer = customer_data.sample(n=1).iloc[0]  # Pick a random customer
        content = netflix_gallery.sample(n=1).iloc[0]  # Pick a random content
        
        watch_date = fake.date_between(pd.to_datetime(customer["subscription_start_date"]), pd.to_datetime(customer["subscription_end_date"]) if customer["subscription_end_date"] else "today")

        data_dict["customer_id"] = customer["customer_id"]
        data_dict["content_id"] = content["show_id"]
        data_dict["watch_date"] = watch_date
        data_dict["rating"] = random.choices([-1, 0, 1, 2], weights=[5, 50, 25, 20])[0]

        data.append(data_dict)
        if i == 1000:
            print("checkpoint 1,000!")
        elif i == 10000:
            print("checkpoint 10,000!")
        elif i == 50000:
            print("checkpoint 50,000!")
        elif i == 100000:
            print("checkpoint 100,000!")
        elif i == 500000:
            print("checkpoint 500,000!")
        elif i == 1000000:
            print("checkpoint 1,000,000!")

    return pd.DataFrame(data)

if __name__ == "__main__":
    n = 100000 # Modify this value to generate more or less data.
    print("Generating customer data...")
    customer_data = generate_customer_data(n)

    print("Generating customer viewing behaviour data...")
    viewing_beahviour_data = generate_viewing_behaviour_data(10 * n, customer_data, netflix_gallery)
    
    print("Saving data to CSV files...")
    customer_data.to_csv("consumer_data.csv", index=False)
    viewing_beahviour_data.to_csv("viewing_behaviour_data.csv", index=False)
    
    display(customer_data.head())
    print("\n")
    display(viewing_beahviour_data.head())
    print("Data generation complete!")
