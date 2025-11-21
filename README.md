Elanco Technical Task – Tick Sightings (FastAPI)
This project is a backend built for the technical task given by Elanco Placement. 
It loads the data (of tick sightings) from an Excel file, filters data, provides simple reports and some basic Machine Learning report.

Structure of the project:
-	main.py
-	loading_the_data.py
-	Tick Sightings.xlsx
-	Imports.txt

main.py contains all API endpoints:
-	/ticks – filters by location and date range
-	/report/locations – number of sightings per location
-	/report/species – number of sightings per species
-	/report/monthly – number of sightings per month
-	/report/species_clusters – a very basic ML insight grouping species into “rare” vs “common” 

Loading_the_data.py reads the excel file and handles: date conversion, some column cleaning, removes missing rows and removes duplicates.

This project is built using:
-	FastAPI
-	Uvicorn
-	Pandas
-	Openpyxl
-	scikit-learn for KMeans
-	On Python 3.14

Instructions for running:
1)	Install the imports depending on python version:

pip install -r imports.txt

pip3 install -r imports.txt

2)	Start server:

uvicorn main:app –reload

3)	Link for API, to paste in browser:
http://127.0.0.1:8000/docs

Design Choices:
-	Tried to keep everything as simple and easy to follow as possible
-	Used pandas as it is good for datasets of this kind
-	Used FastAPI as simple to implement clean routing 
-	Included the ML insight because I wanted to add something extra
-	I’ve done my best to structure the project in a way that can scale if the dataset changes

What I would have done with more time:
-	Make the ML insight more useful, potentially time based or location based rather than rarity and work towards a prediction factor
-	Clean the presentation of the API

Batur Gunen

Elanco Technical Task - Backend
