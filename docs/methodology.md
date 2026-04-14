# Methodology

## Data collection

The dataset was compiled from historical archival documentation preserved in the Archivo General de Simancas, mainly in the Secretaría de Marina section.

The records document timber extraction activities carried out for the Maritime Department of Cádiz between 1748 and 1751.

The original information was first organised in Excel format and later transformed into CSV and XLSX datasets for analysis.

## Data cleaning

The original dataset required several cleaning and preprocessing steps before analysis.

The main cleaning tasks included:

- removing unnecessary spaces
- standardising municipality and province names
- normalising tree species and landownership categories
- converting tree quantities into numeric values
- correcting coordinate formats
- identifying missing values
- reviewing duplicate records
- preparing latitude and longitude fields for mapping

Some manual corrections were later introduced into the final dataset, especially in coordinates, municipality names and place identification fields.

For this reason, the data cleaning notebook documents the main preprocessing workflow, although it may not reproduce the current final dataset exactly.

## Exploratory data analysis

The exploratory analysis focused on:

- total tree quantities
- most productive provinces
- municipalities with the highest timber quantities
- most represented tree species
- landownership distribution
- most important landowners
- comparison between ownership categories
- temporal distribution of felling periods

The analysis was carried out mainly with Pandas and Matplotlib.

## Spatial analysis and mapping

The project includes both static and interactive mapping.

Spatial analysis used:

- Folium for interactive maps
- GeoPandas for reading and processing shapefiles
- historical coordinates created from Iberpix
- administrative boundaries downloaded from the IGN

The mapping notebook generated:

- point distribution maps
- choropleth maps by species
- choropleth maps by ownership type
- municipal and provincial boundary overlays

## Streamlit dashboard

The final dashboard was developed in Streamlit.

The application includes:

- filters
- summary indicators
- data table
- charts
- interactive maps
- downloadable CSV export

The goal of the dashboard is to make the dataset easier to explore and interpret.

## Limitations

Some historical locations could not be identified with total precision.

Certain place names appear with spelling variations across different archival sources.

The quantity of timber sometimes appears in approximate or incomplete form in the original documentation.

Despite these limitations, the dataset is sufficiently consistent for exploratory analysis and visualisation.