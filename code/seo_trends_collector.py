from pytrends.request import TrendReq
import pandas as pd

# Initialize pytrends
pytrends = TrendReq(hl='en-US', tz=360)

# Define search terms relevant to Evago
keywords = [
    "event infrastructure rental",       # General
    "Absperrgitter mieten",              # Germany
    "event barrier hire",                # UK
    "eventverhuur",                      # Netherlands
    "event fencing rental"               # Australia
]

geo_codes = {
    "Germany": "DE",
    "England": "GB",
    "Netherlands": "NL",
    "Australia": "AU",
    "United States": "US"
}

all_data = []

# Fetch data for each keyword and region
for kw in keywords:
    for country, geo in geo_codes.items():
        pytrends.build_payload([kw], cat=0, timeframe='today 12-m', geo=geo)
        df = pytrends.interest_over_time()
        if not df.empty:
            df = df.reset_index()
            df["Keyword"] = kw
            df["Country"] = country
            df = df.rename(columns={kw: "Interest"})
            df = df[["date", "Keyword", "Country", "Interest"]]
            all_data.append(df)

# Combine all
final_df = pd.concat(all_data)
final_df.to_csv("evago_seo_trends.csv", index=False)
print("Saved as evago_seo_trends.csv")