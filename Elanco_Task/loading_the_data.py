import pandas as pd

#Data Handling

def load_data():
    df = pd.read_excel("Tick Sightings.xlsx")
    df["date"] = pd.to_datetime(df["date"], errors = "coerce")
    df.dropna(subset=["date"], inplace=True)
    for collumn in ["location", "latinName", "species"]:
        df[collumn] = df[collumn].astype(str).str.strip().str.title()
    df.drop_duplicates(inplace=True)
    df.reset_index(drop=True, inplace=True)

    return df
