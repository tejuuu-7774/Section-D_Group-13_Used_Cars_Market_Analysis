# Used Cars Price Prediction – Portfolio Case Study

## Problem Statement
Used car pricing is often inconsistent due to multiple influencing factors such as vehicle age, mileage, manufacturer, and condition. Buyers risk overpaying, while sellers may undervalue their vehicles.

This project aims to build a data-driven system to:
- Predict used car prices accurately
- Identify key factors influencing pricing decisions

## Stakeholder Context
- Buyers → want fair market prices
- Sellers → want competitive listing prices
- Dealerships → need pricing strategies to maximize profit

## Dataset Source and Scope
- Dataset: `vehicles.csv`
- Total Records: 426,880
- Total Features: 26
- Data includes:
  - Vehicle attributes (year, manufacturer, condition)
  - Usage metrics (mileage)
  - Listing details (price, location)

## Data Cleaning and Transformation Summary
- Removed duplicate entries
- Handled missing values in key columns (price, year, odometer)
- Converted data types (e.g., year to numeric)
- Filtered unrealistic values (extreme prices, invalid years)
- Standardized categorical variables

## KPI Framework
Key metrics used to evaluate pricing patterns:

- Average Price by Manufacturer
- Price vs Mileage Trend
- Price vs Vehicle Age
- Distribution of Prices by Condition
- Fuel Type and Transmission Impact on Price

## Key Insights
1. Vehicle age has a strong negative correlation with price
2. Mileage significantly reduces vehicle value
3. Certain manufacturers (e.g., premium brands) consistently have higher resale prices
4. Vehicles in excellent condition show disproportionately higher prices
5. Automatic transmission vehicles tend to have slightly higher prices than manual ones

## Tableau Dashboard
The interactive dashboard highlights:
- Price trends across different features
- Comparative analysis of manufacturers
- Distribution of prices across categories

(Add Tableau Public link here)

### Dashboard Preview
(Screenshots should be added in `/tableau/screenshots/`)

## Recommendations
- Sellers should price vehicles based on age and mileage benchmarks
- Buyers should evaluate listings against market trends before purchasing
- Dealerships can optimize pricing strategies using predictive models

## Expected Impact
- More accurate pricing decisions
- Reduced pricing inconsistencies
- Better transparency in the used car market

## Project Repository
[(Add GitHub repository link here)](https://github.com/tejuuu-7774/Section-D_Group-13_Used_Cars_Market_Analysis.git)