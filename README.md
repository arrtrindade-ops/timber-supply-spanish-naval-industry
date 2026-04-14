# Timber Supply for the Spanish Naval Industry (Cádiz Maritime Department, 1748–1751)

## Project overview

This project forms part of a broader study in the fields of naval and environmental history concerning the supply of forest resources for the shipbuilding and ship maintenance industry of the eighteenth-century Spanish Armada.

The selected dataset covers the period between 1748 and 1751 and documents the exploitation of forests and woodlands located in Andalusia for the Maritime Department of Cádiz, based in the Arsenal of La Carraca.

The project combines:

* data cleaning
* exploratory data analysis
* interactive charts
* spatial analysis
* historical mapping
* Streamlit dashboard development

The main objective is to explore how forest resources were mobilised for naval construction and ship maintenance in the Maritime Department of Cádiz during the reforms promoted under the Marquis of Ensenada.

## Historical context

The data was extracted from correspondence, accounts and reports exchanged between the officers of the Maritime Department of Cádiz and the Navy Secretary.

These documents record the bureaucratic process behind the large-scale felling campaigns promoted by the Spanish state between 1748 and 1751, through direct administration.

These fellings formed part of a broader strategy of raw material procurement in preparation for an ambitious naval construction programme promoted by the Navy Secretary, Zénon Somodevilla, Marquis of Ensenada, between 1748 and 1754.

This effort resulted in the construction and maintenance of several new warships of different classes during one of the most productive phases of the early modern Spanish naval industry, representing a milestone in the Bourbon reforms.

## Data source

The sources for this dataset are historical manuscripts preserved in the Archivo General de Simancas, mainly from the Secretaría de Marina section, including the subsections:

* Arsenales (315, 317–320, 327)
* Montes y sus Incidencias (558)
* Asientos (608)
* Tribunal Mayor de Cuentas (4104, 4108, 4112)

The data was originally compiled in an Excel spreadsheet for digital analysis and later transformed into a structured dataset for cleaning, visualisation and mapping.

The coordinates were obtained through the Iberpix viewer of the Instituto Geográfico Nacional:

https://www.ign.es/iberpix/visor/

Administrative boundaries were adapted from shapefiles downloaded from the IGN Centro de Descargas.

## Research questions

The project explores several questions:

* How were felling locations distributed geographically?
* Which municipalities and provinces supplied the greatest quantities of timber?
* Which places concentrated the highest number of felling records?
* Which tree species were most frequently procured?
* How were tree species distributed geographically?
* Which landownership types were most represented?
* Which landowners contributed the largest number of felled trees?
* How were tree species distributed according to landownership categories?
* What were the most productive years and territories?
* How do communal, private, noble and ecclesiastical properties compare in terms of timber production?

## Dataset description

The dataset consists of 419 entries organised into 11 variables.

Each row represents a documented timber felling location or cutting area according to period, landownership and tree species.

Main variables included in the dataset:

* felling_period
* felling_toponymy_source
* felling_toponymy_mtn25
* latitude
* longitude
* municipality
* province
* landownership
* landowner_name
* tree_species
* tree_quantity

## Data cleaning and preprocessing

Before starting the analysis, several data cleaning and preprocessing tasks were carried out in order to improve the consistency and usability of the dataset.

The original dataset contained missing values, different spellings for municipalities and provinces, inconsistent coordinate formats and tree quantities written in different ways.

The main preprocessing steps included:

* standardising latitude and longitude coordinates
* cleaning and converting numeric values in tree_quantity
* unifying municipality and province names
* normalising landownership categories and tree species names
* handling missing and incomplete values
* removing unnecessary spaces and formatting inconsistencies
* separating mixed categories in landownership
* identifying duplicated or repeated records
* converting textual quantities such as "57 trees" into numeric values
* preparing geographic coordinates for mapping

The final EDA and mapping notebooks use the cleaned dataset. Some manual corrections were later introduced into the final dataset, especially in coordinates and place identification fields. For this reason, the original data cleaning notebook may not fully reproduce the current final dataset exactly, but it remains important as documentation of the main cleaning process.

## Tools and libraries

This project uses the following Python libraries:

* pandas
* geopandas
* folium
* streamlit
* streamlit-folium
* matplotlib
* plotly
* openpyxl

Main tools used in the project include:

* Python
* Jupyter Notebook
* Visual Studio Code
* GitHub
* Streamlit Community Cloud
* ChatGPT

## Project structure

```text
timber-supply-spanish-naval-industry/
│
├── app/
│   └── app.py
├── data/
│   ├── raw/
│   ├── cleaned/
│   │   ├── dataset_maderas_clean.csv
│   │   ├── dataset_maderas_final.csv
│   │   └── dataset_maderas_final.xlsx
│   ├── boundaries/
│   └── boundaries_app/
│       ├── provinces_app.geojson
│       └── municipalities_app.geojson
├── notebooks/
│   ├── 01_data_cleaning.ipynb
│   ├── 02_eda.ipynb
│   └── 03_mapping_spatial_analysis.ipynb
├── docs/
│   ├── methodology.md
│   └── eda.md
├── img/
│   ├── charts/
│   └── maps/
│       ├── total_combined_map.html
│       ├── species_oak_map.html
│       ├── species_holm_oak_map.html
│       ├── species_gall_oak_map.html
│       ├── species_pine_map.html
│       ├── ownership_comunal_map.html
│       ├── ownership_noble_estate_map.html
│       ├── ownership_private_map.html
│       └── ownership_ecclesiastic_map.html
├── requirements.txt
└── README.md
```


## Dashboard contents

The Streamlit dashboard includes:

* filters by province, municipality, species, landownership, landowner and period
* keyword search
* summary indicators
* downloadable filtered CSV
* dataset preview table
* interactive charts
* dynamic point map with markers
* choropleth maps by species and ownership type

## How to run the app

Install the dependencies:

```bash
pip install -r requirements.txt
```

Then run the Streamlit app:

```bash
streamlit run app/app.py
```

## Main findings

This section can be expanded later with the main conclusions obtained from the exploratory analysis and mapping.

## Future improvements

Possible future developments include:

* additional charts and filters
* time-series visualisations
* more advanced historical GIS analysis
* integration of archival references into the dashboard
* publication of the dataset in CSV and GeoJSON formats
* connection with larger research projects on naval supply networks

## Deployment

The dashboard was deployed using Streamlit Community Cloud.

The repository was hosted on GitHub and connected directly to Streamlit Community Cloud through the main branch of the project repository.

The application was deployed from:

`app/app.py`

The deployment process required adapting the original spatial data workflow. Large shapefiles were converted into lighter GeoJSON files in order to improve compatibility with Streamlit Cloud and reduce installation problems related to geospatial dependencies.

Interactive choropleth maps were exported as HTML files and embedded directly into the dashboard. This approach reduced loading times and avoided dependency issues with packages such as Fiona and GDAL during cloud deployment.

The final online version of the project is available at:

`https://timber-spanish-naval-industry.streamlit.app/`

## Author

Ana Rita Trindade

Instituto de Historia – CSIC

Programa MOMENTUM

Project: Historia Sumergida y Big Data: Gestión y visualización del patrimonio marítimo y subacuático, siglos XV–XIX (MMT24-IH-01)
