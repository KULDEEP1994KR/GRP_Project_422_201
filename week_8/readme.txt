# Rental Bond Dataset

Source: New Zealand Ministry of Business, Innovation & Employment (MBIE), Tenancy Services – Rental Bond Data.

Dataset: Detailed Quarterly Report (Q1 2020 – Q3 2026)

This dataset contains quarterly rental bond statistics for New Zealand, including the number of rental bonds and weekly rent measures for different locations, dwelling types, and bedroom categories.

## Column Descriptions

| Column | Meaning |
|--------|---------|
| TimeFrame | The quarter and year the data represents (e.g., 2026-04-01 = Q2 2026). |
| Location Id | Unique identifier for the geographic location. This should be kept for merging with other datasets. |
| Dwelling Type | Type of rental dwelling (e.g., ALL, apartment, house). |
| Number Of Beds | Number of bedrooms in the dwelling. |
| Total Bonds | Total number of rental bonds lodged during the quarter. |
| Active Bonds | Number of rental bonds that remained active during the quarter. |
| Closed Bonds | Number of rental bonds closed during the quarter. |
| Median Rent | Median weekly rent (NZD). |
| Geometric Mean Rent | Geometric mean of weekly rents (NZD), which reduces the influence of extreme values. |
| Upper Quartile Rent | 75th percentile of weekly rent. |
| Lower Quartile Rent | 25th percentile of weekly rent. |
| Log Std Dev Weekly Rent | Logarithmic standard deviation of weekly rent, indicating rent variability. |