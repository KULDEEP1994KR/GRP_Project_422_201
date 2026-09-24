import pandas as pd
import matplotlib.pyplot as plt

# File path
file_path = "/Users/oliverabbott/Desktop/christ_bond_merged.csv"

# Read the merged dataset
data = pd.read_csv(file_path)

# Show the first 5 rows
print(data.head())

# Show all column names
print(data.columns.tolist())

print(data[["area_code", "TimeFrame", "id", "Total Bonds"]].head(20))

# Count the number of Airbnb properties in each area
airbnb_counts = data.groupby("area_code")["id"].nunique()

# Get the number of rental properties in each area
rental_counts = data.groupby("area_code")["Total Bonds"].max()

# Combine the two results
comparison = pd.DataFrame({
    "Airbnb Properties": airbnb_counts,
    "Rental Properties": rental_counts
})

# Show the results
print(comparison)

# Save the comparison as a CSV file
comparison.to_csv("/Users/oliverabbott/Desktop/airbnb_vs_rentals_by_area.csv")

print("Comparison saved to Desktop!")

# Count how many areas have rental data
areas_with_rent = comparison["Rental Properties"].notna().sum()

# Count how many areas do not have rental data
areas_without_rent = comparison["Rental Properties"].isna().sum()

print("Areas with rental data:", areas_with_rent)
print("Areas without rental data:", areas_without_rent)

# Show areas where there is no rental data
missing_rent = comparison[comparison["Rental Properties"].isna()]

print(missing_rent)

# Get the area codes with missing rental data
missing_codes = comparison[comparison["Rental Properties"].isna()].index

# Check whether these area codes exist in the Tenancy data
print("Number of missing area codes:", len(missing_codes))
print("Missing area codes:")
print(missing_codes.tolist())

# Load the original Tenancy data
tenancy_file = "/Users/oliverabbott/Desktop/Detailed-Quarterly-Tenancy-Q1-2020-Q3-2026.csv"

tenancy = pd.read_csv(tenancy_file)

# Make sure Location Id is treated as text
tenancy["Location Id"] = tenancy["Location Id"].astype(str)

# Make the Airbnb area codes text too
missing_codes = missing_codes.astype(str)

# Find missing area codes that DO exist in the Tenancy data
found_in_tenancy = missing_codes[missing_codes.isin(tenancy["Location Id"])]

print("Missing areas that exist in Tenancy data:", len(found_in_tenancy))
print(found_in_tenancy.tolist())

# Count the number of Airbnb properties in each area
airbnb_counts = data.groupby("area_code")["id"].nunique()

# Get the number of rental properties in each area
rental_counts = data.groupby("area_code")["Total Bonds"].max()

# Combine the two results
comparison = pd.DataFrame({
    "Airbnb Properties": airbnb_counts,
    "Rental Properties": rental_counts
})

# Keep only areas where we have both types of data
comparison_complete = comparison.dropna(
    subset=["Rental Properties"]
).copy()

# Convert rental property counts to whole numbers
comparison_complete["Rental Properties"] = (
    comparison_complete["Rental Properties"].astype(int)
)

# Turn area_code from the index into a normal column
comparison_complete = comparison_complete.reset_index()

# Display a clean table
print("\nAirbnb properties vs rental properties by area:")
print(comparison_complete.to_string(index=False))

# SAVE THE TABLE
comparison_complete.to_csv(
    "week_9/airbnb_vs_rentals_by_area.csv",
    index=False
)

# Find the 10 areas with the most Airbnb properties
top_10 = comparison_complete.nlargest(
    10, "Airbnb Properties"
)

# Display the top 10
print("\nTop 10 areas by Airbnb properties:")
print(top_10.to_string(index=False))

# Create a bar chart
top_10.plot(
    x="area_code",
    y=["Airbnb Properties", "Rental Properties"],
    kind="bar",
    figsize=(10, 6)
)

plt.title("Airbnb vs Rental Properties in the 10 Areas with Most Airbnb Listings")
plt.xlabel("Area code")
plt.ylabel("Number of properties")
plt.xticks(rotation=45)
plt.tight_layout()

# Display the graph
plt.show()

# SAVE THE GRAPH
plt.savefig(
    "week_9/airbnb_vs_rentals_top10.png",
    dpi=300,
    bbox_inches="tight"
)

plt.show()