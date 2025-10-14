#!/usr/bin/env python3
"""
GDP per capita visualization using xatra
Processes DOSE_V2.9.csv data and creates a dynamic map showing GDP per capita
by GADM level-1 subdivision over time.
"""

import pandas as pd
import xatra
import numpy as np

from matplotlib.colors import LinearSegmentedColormap
import matplotlib.pyplot as plt
from matplotlib.colors import LogNorm


def load_and_process_data(csv_file):
    """Load and process the DOSE data for GDP per capita visualization."""
    print("Loading data from CSV...")

    # Load the CSV file
    df = pd.read_csv(csv_file)

    # Clean the data - remove rows where year is not numeric
    df = df[pd.to_numeric(df["year"], errors="coerce").notna()]
    df["year"] = pd.to_numeric(df["year"])

    # Filter for recent years (2000-2020) to focus on more complete data
    # df = df[(df['year'] >= 2000) & (df['year'] <= 2020)]

    # Filter for Indian subcontinent countries only
    subcontinent_countries = ["IND", "PAK", "BGD", "LKA", "NPL", "BTN"]
    df = df[df["GID_0"].isin(subcontinent_countries)]

    # Use GDP per capita in USD (grp_pc_usd column)
    # Clean the data - remove rows with missing GDP per capita data
    df = df.dropna(subset=["grp_pc_usd", "GID_1"])

    # Convert GID_1 to proper format for xatra (remove the _1 suffix)
    # Replace specific GID "IND.14_1" with "Z01.14_1"
    df["GID_1"] = df["GID_1"].str.replace("IND.14_1", "Z01.14_1")
    df["GID_1_clean"] = df["GID_1"].str.replace("_1", "")

    print(f"Data loaded: {len(df)} records")
    print(f"Years: {sorted(df['year'].unique())}")
    print(f"Countries: {df['GID_0'].unique()}")
    print(f"Regions: {df['GID_1_clean'].nunique()}")

    return df


def create_dataframe_for_xatra(df):
    """Create a DataFrame in the format expected by xatra.Dataframe()."""
    print("Creating DataFrame for xatra...")

    # Pivot the data to have years as columns
    pivot_df = df.pivot_table(
        index="GID_1_clean",
        columns="year",
        values="grp_pc_usd",
        aggfunc="mean",  # In case there are duplicates
    )

    # Reset index to make GID_1_clean a column
    pivot_df = pivot_df.reset_index()

    # Rename the index column to GID
    pivot_df = pivot_df.rename(columns={"GID_1_clean": "GID"})

    # Set GID as index
    pivot_df = pivot_df.set_index("GID")

    # Track which values were originally missing (before interpolation)
    print("Tracking missing values for interpolation notes...")
    missing_mask = pivot_df.isnull()

    # Ensure columns are numeric for interpolation
    pivot_df.columns = pd.to_numeric(pivot_df.columns)

    # Apply spline interpolation to fill missing values along the columns (years)
    print("Applying spline interpolation to fill missing values...")
    # Transpose to make years the index, apply interpolation, then transpose back
    pivot_df = pivot_df.T.interpolate(
        method="spline", order=2, limit_direction="both", limit_area="inside"
    ).T

    # Fill any remaining missing values with NaN (xatra will handle these)
    pivot_df = pivot_df.fillna(np.nan)

    # Create note columns for interpolated values
    print("Creating note columns for interpolated values...")
    note_df = pd.DataFrame(
        index=pivot_df.index, columns=[f"{col}_note" for col in pivot_df.columns]
    )
    note_df = note_df.astype("object")  # Set object dtype explicitly

    # Set "interpolated" for values that were originally missing
    for col in pivot_df.columns:
        note_col = f"{col}_note"
        note_df.loc[missing_mask[col], note_col] = "interpolated"

    # Combine main data with note data
    combined_df = pd.concat([pivot_df, note_df], axis=1)

    print(f"Combined DataFrame shape: {combined_df.shape}")
    print(f"GDP columns (years): {list(pivot_df.columns)}")
    print(f"Note columns: {list(note_df.columns)}")
    print(f"Sample GIDs: {list(pivot_df.index[:10])}")

    return combined_df


def create_gdp_visualization(df_pivot):
    """Create the xatra visualization for GDP per capita data."""
    print("Creating xatra visualization...")

    # Create the map
    map_obj = xatra.Map()

    # Add base map options
    map_obj.BaseOption("OpenStreetMap", default=True)
    map_obj.BaseOption("Esri.WorldImagery")
    map_obj.BaseOption("OpenTopoMap")
    map_obj.BaseOption("Esri.WorldPhysical")

    # # Set up a custom colormap for GDP data (green to red gradient)
    # colors = ['#2E8B57', '#32CD32', '#FFD700', '#FF8C00', '#FF4500', '#DC143C']
    # colors = ['green', 'yellow', 'red']
    colors = ['white', 'blue', 'black']
    custom_cmap = LinearSegmentedColormap.from_list('gdp_colormap', colors)
    map_obj.DataColormap(custom_cmap)
    map_obj.DataColormap(colormap=custom_cmap,norm=LogNorm())

    # Add the DataFrame data
    map_obj.Dataframe(df_pivot)

    # Add administrative boundaries for context
    # Add level-1 admin boundaries for Indian subcontinent countries
    subcontinent_countries = ["IND", "PAK", "BGD", "LKA", "NPL", "BTN"]
    for country in subcontinent_countries:
        try:
            map_obj.Admin(gadm=country, level=1, classes="admin-boundaries")
        except:
            # Skip if country data not available
            continue

    # Add rivers for geographical context
    map_obj.AdminRivers(sources=["naturalearth"], classes="rivers")

    # Add title and description
    map_obj.TitleBox("""
    <h2>GDP per Capita - Indian Subcontinent</h2>
    <p><b>Data Source:</b> <a href="https://zenodo.org/records/13773040">DOSE V2.9 Database</a></p>
    <p><b>Countries:</b> India, Pakistan, Bangladesh, Sri Lanka, Nepal, Bhutan</p>
    <p><b>Years:</b> 1980-2020</p>
    <p><b>Level:</b> GADM Level-1 Subdivisions (States/Provinces)</p>
    <p><b>Values:</b> GDP per capita in USD (constant prices)</p>
    <p>Use the time slider to explore changes over time. 
    Regions with missing data appear in gray.</p>
    """)

    # Set up the time slider for the dynamic map
    # map_obj.slider(start=2000, end=2020, speed=2.0)

    # Add custom CSS styling
    map_obj.CSS("""
    /* Admin boundaries styling */
    .admin-boundaries {
        stroke: #333333;
        stroke-width: 0.5;
        fill: none;
        opacity: 0.6;
    }
    
    /* Rivers styling */
    .rivers {
        stroke: #0066cc;
        stroke-width: 1;
        opacity: 0.7;
    }
    
    /* Title box styling */
    #title {
        background: rgba(255, 255, 255, 0.95);
        border: 2px solid #333;
        padding: 15px 20px;
        border-radius: 10px;
        max-width: 450px;
        font-family: Arial, sans-serif;
        box-shadow: 0 4px 8px rgba(0,0,0,0.1);
    }
    
    #title h2 {
        margin: 0 0 10px 0;
        color: #2c3e50;
        font-size: 20px;
    }
    
    #title p {
        margin: 5px 0;
        font-size: 14px;
        line-height: 1.4;
    }
    
    /* Time controls styling */
    #controls {
        background: rgba(255, 255, 255, 0.9);
        padding: 15px;
        border-radius: 8px;
        border: 1px solid #ccc;
        box-shadow: 0 2px 4px rgba(0,0,0,0.1);
    }
    
    #controls input {
        width: 100%;
        margin: 5px 0;
    }
    
    /* Data visualization styling */
    .data {
        stroke: #ffffff;
        stroke-width: 0.5;
        opacity: 0.8;
    }
    
    .data:hover {
        stroke: #000000;
        stroke-width: 1;
        opacity: 1;
    }
    """)

    return map_obj


def main():
    """Main function to create the GDP visualization."""
    print("Starting GDP per capita visualization...")

    # Load and process data
    df = load_and_process_data("DOSE_V2.9.csv")

    # Create DataFrame for xatra
    df_pivot = create_dataframe_for_xatra(df)

    # Create visualization
    map_obj = create_gdp_visualization(df_pivot)

    # Export the map
    print("Exporting map...")
    map_obj.show(
        out_json="docs/subcontinent_gdp_pc.json",
        out_html="docs/subcontinent_gdp_pc.html",
    )

    print("Visualization complete!")
    print("Files created:")
    print("- subcontinent_gdp_pc.html")
    print("- subcontinent_gdp_pc.json")


if __name__ == "__main__":
    main()
