#!/usr/bin/env python3
"""
Plot GDP per capita ratios for selected Indian states relative to Maharashtra
"""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def load_and_process_data(csv_file):
    """Load and process the DOSE data for GDP per capita visualization."""
    print("Loading data from CSV...")
    
    # Load the CSV file
    df = pd.read_csv(csv_file)
    
    # Clean the data - remove rows where year is not numeric
    df = df[pd.to_numeric(df["year"], errors="coerce").notna()]
    df["year"] = pd.to_numeric(df["year"])
    
    # Filter for Indian subcontinent countries only
    subcontinent_countries = ["IND", "PAK", "BGD", "LKA", "NPL", "BTN"]
    df = df[df["GID_0"].isin(subcontinent_countries)]
    
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

def create_ratios_plot(df):
    """Create a plot showing GDP per capita ratios relative to Maharashtra."""
    
    # Define the states to plot
    states = {
        "IND.16": "Karnataka",
        "IND.2": "Andhra Pradesh", 
        "IND.17": "Kerala",
        "IND.31": "Tamil Nadu"
    }
    reference_state = "IND.20"  # Maharashtra
    
    # Pivot the data to have years as columns
    pivot_df = df.pivot_table(
        index="GID_1_clean",
        columns="year", 
        values="grp_pc_usd",
        aggfunc="mean"
    )
    
    # Apply spline interpolation to fill missing values
    pivot_df.columns = pd.to_numeric(pivot_df.columns)
    pivot_df = pivot_df.T.interpolate(
        method="spline", order=2, limit_direction="both", limit_area="inside"
    ).T
    pivot_df = pivot_df.fillna(np.nan)
    
    # Check if reference state exists
    if reference_state not in pivot_df.index:
        print(f"Warning: Reference state {reference_state} (Maharashtra) not found in data")
        print("Available states:", sorted(pivot_df.index))
        return
    
    # Get reference values (Maharashtra)
    reference_values = pivot_df.loc[reference_state]
    
    # Create the plot
    plt.figure(figsize=(12, 8))
    
    # Plot ratios for each state
    for state_id, state_name in states.items():
        if state_id in pivot_df.index:
            state_values = pivot_df.loc[state_id]
            # Calculate ratio relative to Maharashtra
            ratios = state_values / reference_values
            # Only plot where both values are not NaN
            valid_mask = ~(state_values.isna() | reference_values.isna())
            years = pivot_df.columns[valid_mask]
            valid_ratios = ratios[valid_mask]
            
            plt.plot(years, valid_ratios, marker='o', linewidth=2, label=state_name)
        else:
            print(f"Warning: State {state_id} ({state_name}) not found in data")
    
    # Add reference line at 1.0 (Maharashtra baseline)
    plt.axhline(y=1.0, color='red', linestyle='--', alpha=0.7, label='Maharashtra (baseline)')
    
    # Customize the plot
    plt.xlabel('Year', fontsize=12)
    plt.ylabel('GDP per Capita Ratio (relative to Maharashtra)', fontsize=12)
    plt.title('GDP per Capita Ratios: Selected States vs Maharashtra', fontsize=14, fontweight='bold')
    plt.legend(fontsize=10)
    plt.grid(True, alpha=0.3)
    
    # Set y-axis limits for better visualization
    plt.ylim(0, 1.5)
    
    # Add some statistics
    print("\nGDP per Capita Statistics (USD):")
    print("=" * 50)
    
    # Show final year statistics
    final_year = pivot_df.columns[-1]
    print(f"Final year ({final_year}) GDP per capita:")
    
    if reference_state in pivot_df.index:
        maharashtra_gdp = pivot_df.loc[reference_state, final_year]
        print(f"Maharashtra (IND.20): ${maharashtra_gdp:,.0f}")
    
    for state_id, state_name in states.items():
        if state_id in pivot_df.index:
            state_gdp = pivot_df.loc[state_id, final_year]
            ratio = state_gdp / maharashtra_gdp if reference_state in pivot_df.index else np.nan
            print(f"{state_name} ({state_id}): ${state_gdp:,.0f} (ratio: {ratio:.2f})")
    
    plt.tight_layout()
    
    # Save the plot
    output_file = "docs/state_gdp_ratios.png"
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    print(f"\nPlot saved as: {output_file}")
    
    # Show the plot
    plt.show()

def main():
    """Main function to create the ratios plot."""
    print("Creating GDP per capita ratios plot...")
    
    # Load and process data
    df = load_and_process_data("DOSE_V2.9.csv")
    
    # Create the ratios plot
    create_ratios_plot(df)
    
    print("Plot creation complete!")

if __name__ == "__main__":
    main()
