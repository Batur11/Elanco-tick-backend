from fastapi import FastAPI
from loading_the_data import load_data
import pandas as pd
from sklearn.cluster import KMeans

app = FastAPI()

#Search & Filtering

@app.get("/ticks")
def get_ticks(location: str=None, start_date: str=None, end_date: str=None):
    df = load_data()

#filter by location
    if location is not None:
        df = df[df["location"].str.lower() == location.lower()]

#filter by dates
    if start_date is not None:
        start = pd.to_datetime(start_date, errors="coerce")
        if pd.isna(start):
            return {"Invalid date"}
        df = df[df["date"] >= start]

    if end_date is not None:
        end = pd.to_datetime(end_date, errors="coerce")
        if pd.isna(end):
            return {"Invalid date"}
        df = df[df["date"] <= end]

    return df.to_dict(orient="records")

#Data Reporting

#sightings by location
@app.get("/report/locations")
def report_locations():
    df = load_data()
    summary = df.groupby("location").size().reset_index(name="count")
    return summary.to_dict(orient="records")

#sightings per species
@app.get("/report/species")
def report_species():
    df = load_data()
    summary = df.groupby("species").size().reset_index(name="count")
    return summary.to_dict(orient="records")

#sightings per month
@app.get("/report/monthly")
def report_monthly():
    df = load_data()
    df["month"] = pd.to_datetime(df["date"], errors="coerce").dt.month
    return df["month"].value_counts().sort_index().to_dict()

#Machine Learning Insight (Extension)
#Splits species into rare and common
@app.get("/report/species_clusters")
def species_clusters():
    df = load_data()
    counts = df["species"].value_counts().reset_index()
    counts.columns = ["species", "count"]
    X = counts[["count"]]
    kmeans = KMeans(n_clusters=2, random_state=0)
    counts["cluster"] = kmeans.fit_predict(X)
    rare_cluster = counts.groupby("cluster")["count"].mean().idxmin()

    rare_species = counts[counts["cluster"] == rare_cluster]["species"].tolist()
    common_species = counts[counts["cluster"] != rare_cluster]["species"].tolist()

    return {
        "rare_species": rare_species,
        "common_species": common_species
    }
