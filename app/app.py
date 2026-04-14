import pandas as pd
import streamlit as st
import streamlit.components.v1 as components
import geopandas as gpd
import folium
from streamlit_folium import st_folium
from pathlib import Path




st.set_page_config(
    page_title="Timber Supply for the Spanish Naval Industry",
    page_icon="🌲",
    layout="wide"
)

st.markdown(
    """
    <style>
    button[data-baseweb="tab"] {
        font-size: 1.2rem;
        font-weight: 600;
        padding: 0.75rem 1.5rem;
    }

    div[data-testid="stTabs"] button {
        height: 3.2rem;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.title("Timber Supply for the Spanish Naval Industry (Cádiz Maritime Department, 1748–1751)")

st.caption(
    "Exploratory dashboard on timber extraction, landownership and forest supply for the eighteenth-century Spanish Armada."
)

st.markdown(
    """
    This project forms part of a broader study in the fields of naval and environmental history concerning the supply of forest resources for the shipbuilding and ship maintenance industry of the eighteenth-century Spanish Armada.

    The dataset covers the period between 1748 and 1751 and documents the exploitation of forests and woodlands located in Andalusia for the Maritime Department of Cádiz, based in the Arsenal of La Carraca.

    The historical information was extracted from correspondence, accounts and reports exchanged between the officers of the Maritime Department of Cádiz and the Navy Secretary during the large-scale felling campaigns promoted by the Spanish state under the reforms of Zénon Somodevilla, Marqués de la Ensenada.

    These fellings formed part of a broader policy of state-promoted naval construction and raw material procurement during one of the most productive phases of the Bourbon naval reforms. Between 1748 and 1754, the Spanish Crown intensified the construction and maintenance of warships of different classes, requiring large quantities of timber.

    The documentation used in this dataset corresponds exclusively to the felling operations carried out through direct administration by the state. As a result, the records provide detailed information about cutting areas, municipalities, landownership, tree species, landowners and timber quantities procured for naval purposes.

    The sources used in this dataset are historical manuscripts preserved in the Archivo General de Simancas, especially in the Secretaría de Marina section, including the subsections Arsenales (315, 317–320, 327), Montes y sus Incidencias (558), Asientos (608), and Tribunal Mayor de Cuentas (4104, 4108, 4112).

    The variables felling_toponymy_MTN25, latitude and longitude were created through the identification of historical cutting areas in the Iberpix cartographic viewer of the Instituto Geográfico Nacional (IGN):
    https://www.ign.es/iberpix/visor/ (Mapa Topográfico Nacional 1:25,000).

    Province and municipality polygons were adapted from shapefiles downloaded from the IGN Centro de Descargas:
    https://centrodedescargas.cnig.es/CentroDescargas/home

    The project combines data cleaning, exploratory analysis, statistical charts, spatial visualization and interactive historical mapping in order to explore questions such as:

    - How were felling locations distributed geographically?
    - Which municipalities and provinces supplied the greatest quantities of timber?
    - Which tree species were most frequently procured?
    - What types of landownership were most represented?
    - Which landowners contributed the highest number of felled trees?
    - What were the most productive years and territories?

    This dashboard allows users to explore the dataset through filters, summary indicators, charts and interactive maps.
    """
)

from pathlib import Path

def load_data():
    base_path = Path(__file__).resolve().parent.parent
    file_path = base_path / "data" / "cleaned" / "dataset_maderas_final.xlsx"
    df = pd.read_excel(file_path)

    df.columns = (
        df.columns
        .str.strip()
        .str.lower()
    )

    return df

df = load_data()




st.sidebar.header("Filters")

province_options = sorted(df["province"].dropna().unique())
municipality_options = sorted(df["municipality"].dropna().unique())
species_options = sorted(df["tree_species"].dropna().unique())
ownership_options = sorted(df["landownership"].dropna().unique())
landowner_options = sorted(df["landowner_name"].dropna().unique())
period_options = sorted(df["felling_period"].dropna().astype(str).unique())

selected_province = st.sidebar.multiselect(
    "Province",
    province_options
)

selected_municipality = st.sidebar.multiselect(
    "Municipality",
    municipality_options
)

selected_species = st.sidebar.multiselect(
    "Species",
    species_options
)

selected_ownership = st.sidebar.multiselect(
    "Ownership type",
    ownership_options
)

selected_landowner = st.sidebar.multiselect(
    "Landowner name",
    landowner_options
)

selected_period = st.sidebar.multiselect(
    "Felling period",
    period_options
)

general_search = st.sidebar.text_input("General search")

filtered_df = df.copy()

if selected_province:
    filtered_df = filtered_df[filtered_df["province"].isin(selected_province)]

if selected_municipality:
    filtered_df = filtered_df[filtered_df["municipality"].isin(selected_municipality)]

if selected_species:
    filtered_df = filtered_df[filtered_df["tree_species"].isin(selected_species)]

if selected_ownership:
    filtered_df = filtered_df[filtered_df["landownership"].isin(selected_ownership)]

if selected_landowner:
    filtered_df = filtered_df[filtered_df["landowner_name"].isin(selected_landowner)]

if selected_period:
    filtered_df = filtered_df[
        filtered_df["felling_period"].astype(str).isin(selected_period)
    ]
    
if general_search:
    search_mask = (
        filtered_df["felling_toponymy_source"].astype(str).str.contains(general_search, case=False, na=False) |
        filtered_df["felling_toponymy_mtn25"].astype(str).str.contains(general_search, case=False, na=False) |
        filtered_df["municipality"].astype(str).str.contains(general_search, case=False, na=False) |
        filtered_df["province"].astype(str).str.contains(general_search, case=False, na=False) |
        filtered_df["tree_species"].astype(str).str.contains(general_search, case=False, na=False) |
        filtered_df["landownership"].astype(str).str.contains(general_search, case=False, na=False) |
        filtered_df["landowner_name"].astype(str).str.contains(general_search, case=False, na=False) |
        filtered_df["felling_period"].astype(str).str.contains(general_search, case=False, na=False)
    )

    filtered_df = filtered_df[search_mask]


st.subheader("Summary metrics")

col1, col2, col3, col4, col5 = st.columns(5)

col1.metric("Total records", len(filtered_df))

col2.metric(
    "Total tree quantity",
    int(filtered_df["tree_quantity"].sum())
)

col3.metric(
    "Provinces",
    filtered_df["province"].nunique()
)

col4.metric(
    "Municipalities",
    filtered_df["municipality"].nunique()
)

col5.metric(
    "Landowners",
    filtered_df["landowner_name"].nunique()
)

csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download filtered data as CSV",
    data=csv,
    file_name="filtered_timber_data.csv",
    mime="text/csv"
)

tab1, tab2, tab3 = st.tabs(["Data", "Charts", "Maps"])

with tab1:
    st.subheader("Dataset preview")
    st.dataframe(filtered_df, width="stretch")

with tab2:
    st.subheader("Tree quantities by province")

    province_chart = (
        filtered_df.groupby("province", as_index=False)["tree_quantity"]
        .sum()
        .sort_values(by="tree_quantity", ascending=False)
    )

    st.bar_chart(
        province_chart,
        x="province",
        y="tree_quantity",
        width="stretch"
    )

    st.subheader("Tree quantities by municipality")

    municipality_chart = (
        filtered_df.groupby("municipality", as_index=False)["tree_quantity"]
        .sum()
        .sort_values(by="tree_quantity", ascending=False)
    )

    st.bar_chart(
        municipality_chart,
        x="municipality",
        y="tree_quantity",
        width="stretch"
    )

    st.subheader("Tree quantities by species")

    species_chart = (
        filtered_df.groupby("tree_species", as_index=False)["tree_quantity"]
        .sum()
        .sort_values(by="tree_quantity", ascending=False)
    )

    st.bar_chart(
        species_chart,
        x="tree_species",
        y="tree_quantity",
        width="stretch"
    )

    st.subheader("Tree quantities by landownership type")

    ownership_chart = (
        filtered_df.groupby("landownership", as_index=False)["tree_quantity"]
        .sum()
        .sort_values(by="tree_quantity", ascending=False)
    )

    st.bar_chart(
        ownership_chart,
        x="landownership",
        y="tree_quantity",
        width="stretch"
    )

    st.subheader("Tree quantities by landowner")

    owner_chart = (
        filtered_df.groupby("landowner_name", as_index=False)["tree_quantity"]
        .sum()
        .sort_values(by="tree_quantity", ascending=False)
    )

    st.bar_chart(
        owner_chart,
        x="landowner_name",
        y="tree_quantity",
        width="stretch"
    )

with tab3:
    st.subheader("Interactive maps")

    st.subheader("Filtered map")

    base_path = Path(__file__).resolve().parent.parent

    municipality_name_corrections = {
        "HUÉVAR": "HUÉVAR DEL ALJARAFE",
        "LA GRANADA DEL RÍO TINTO": "LA GRANADA DE RÍO-TINTO",
        "ZAHARA DE LA SIERRA": "ZAHARA"
    }

    dynamic_map_df = filtered_df[
        filtered_df["latitude"].notna() &
        filtered_df["longitude"].notna()
    ].copy()

    if not dynamic_map_df.empty:
        provinces_path = base_path / "data" / "boundaries" / "lineas_limite" / "SHP_ETRS89" / "recintos_provinciales_inspire_peninbal_etrs89" / "recintos_provinciales_inspire_peninbal_etrs89.shp"

        municipalities_path = base_path / "data" / "boundaries" / "lineas_limite" / "SHP_ETRS89" / "recintos_municipales_inspire_peninbal_etrs89" / "recintos_municipales_inspire_peninbal_etrs89.shp"

        provinces_dynamic = gpd.read_file(provinces_path)
        provinces_dynamic = provinces_dynamic.to_crs(epsg=4326)
        provinces_dynamic["NAMEUNIT"] = (
            provinces_dynamic["NAMEUNIT"]
            .astype(str)
            .str.upper()
            .str.strip()
        )

        dataset_provinces = (
            dynamic_map_df["province"]
            .dropna()
            .astype(str)
            .str.upper()
            .str.strip()
            .unique()
        )

        provinces_dynamic = provinces_dynamic[
            provinces_dynamic["NAMEUNIT"].isin(dataset_provinces)
        ].copy()

        municipalities_dynamic = gpd.read_file(municipalities_path)
        municipalities_dynamic = municipalities_dynamic.to_crs(epsg=4326)
        municipalities_dynamic["NAMEUNIT"] = (
            municipalities_dynamic["NAMEUNIT"]
            .astype(str)
            .str.upper()
            .str.strip()
        )

        dataset_municipalities = [
            municipality_name_corrections.get(m.upper().strip(), m.upper().strip())
            for m in dynamic_map_df["municipality"].dropna().astype(str).unique()
        ]

        municipalities_dynamic = municipalities_dynamic[
            municipalities_dynamic["NAMEUNIT"].isin(dataset_municipalities)
        ].copy()

        map_center = [
            dynamic_map_df["latitude"].mean(),
            dynamic_map_df["longitude"].mean()
        ]

        m_boundaries = folium.Map(
            location=map_center,
            zoom_start=7,
            tiles="CartoDB positron"
        )

        folium.GeoJson(
            provinces_dynamic,
            name="Provinces",
            style_function=lambda feature: {
                "fillColor": "transparent",
                "color": "darkred",
                "weight": 2
            },
            tooltip=folium.GeoJsonTooltip(
                fields=["NAMEUNIT"],
                aliases=["Province:"]
            )
        ).add_to(m_boundaries)

        folium.GeoJson(
            municipalities_dynamic,
            name="Municipalities",
            style_function=lambda feature: {
                "fillColor": "transparent",
                "color": "steelblue",
                "weight": 1
            },
            tooltip=folium.GeoJsonTooltip(
                fields=["NAMEUNIT"],
                aliases=["Municipality:"]
            )
        ).add_to(m_boundaries)

        for _, row in dynamic_map_df.iterrows():
            popup_text = f"""
            <b>Province:</b> {row['province']}<br>
            <b>Municipality:</b> {row['municipality']}<br>
            <b>Species:</b> {row['tree_species']}<br>
            <b>Ownership:</b> {row['landownership']}<br>
            <b>Landowner:</b> {row['landowner_name']}<br>
            <b>Quantity:</b> {row['tree_quantity']}<br>
            <b>Toponymy:</b> {row['felling_toponymy_mtn25']}<br>
            <b>Period:</b> {row['felling_period']}
            """

            folium.CircleMarker(
                location=[row["latitude"], row["longitude"]],
                radius=5,
                popup=folium.Popup(popup_text, max_width=300),
                color="darkgreen",
                fill=True,
                fill_opacity=0.8
            ).add_to(m_boundaries)

        folium.LayerControl().add_to(m_boundaries)

        st_folium(m_boundaries, width=1200, height=650)

    else:
        st.info("No records with valid coordinates for the current filters.")

    st.subheader("Choropleth map")

total_map_path = base_path / "img" / "maps" / "total_combined_map.html"

if total_map_path.exists():
    html_content = total_map_path.read_text(encoding="utf-8")
    components.html(html_content, height=700, scrolling=True)
else:
    st.warning("Total combined map file not found.")