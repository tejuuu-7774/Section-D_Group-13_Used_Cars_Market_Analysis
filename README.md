# US Used Cars Market Analysis (Craigslist Dataset)

## Overview

This project presents an interactive data visualization dashboard built using Tableau to analyze the US used car market based on Craigslist listings.

The analysis is structured into three focused dashboards to provide a complete understanding of the market:
1. Market Overview
2. Pricing Insights
3. Market Segmentation

Each dashboard highlights different aspects of pricing, distribution, vehicle behavior, and customer preferences.

---

## Objectives

- Understand overall market trends and distribution
- Analyze pricing behavior and influencing factors
- Identify customer preferences and listing patterns
- Provide interactive filtering for deeper exploration

---

## Dataset

- Cleaned rows and columns - (27987, 23) out of sampled dataset (50k rows , 26 columns)
- Source: Craigslist US Used Cars Dataset (2021)
- Fields used include:
  - Price
  - Odometer (Mileage)
  - Year
  - State / State Full Name
  - Vehicle Type
  - Manufacturer
  - Fuel Type
  - Transmission
  - Condition
  - Cylinders

---

## Dashboard 1: Market Overview

### Purpose
Provides a high-level summary of the used car market across the US.

### KPIs
- Total Listings → COUNT(Id)
- Average Price → AVG(Price)
- Median Price → MEDIAN(Price)
- Average Car Age → AVG(Car Age)
- Common Manufacturer → MODE/Top Manufacturer

### Charts Used
- Listings by State → Horizontal Bar Chart
- Price Trend by Manufacturing Year → Line Chart
- State vs Vehicle Type → Heatmap
- Price vs State vs Type → Grouped Bar Chart
- Price Distribution → Histogram
- Price Category Distribution → Donut Chart

### Key Insight
The market is concentrated in a few key states, with clear pricing trends based on vehicle age and category.

---

## Dashboard 2: Pricing Insights

### Purpose
Analyzes how different factors influence vehicle pricing.

### KPIs
- Average Mileage → AVG(Odometer)
- Max Price Type → Vehicle Type with highest AVG(Price)
- Min Price Type → Vehicle Type with lowest AVG(Price)
- Top Fuel → Fuel Type with highest COUNT(Id)

### Charts Used
- Fuel vs Price Category Distribution → 100% Stacked Bar Chart
- Price Category Trend Over Time → Area Chart
- Price by Vehicle Condition → Bar Chart
- Price Decline with Mileage → Line Chart (Binned Odometer)
- Price by Engine Power (Cylinders) → Bar Chart

### Key Insight
Vehicle price decreases consistently with mileage, while condition, fuel type, and engine power significantly impact pricing.

---

## Dashboard 3: Market Segmentation

### Purpose
Explores customer preferences and listing behavior across regions.

### KPIs
- Dominant Type → Vehicle Type with highest COUNT(Id)
- Leading State → State with highest listings
- Condition Leader → Most common condition
- Fuel Leader → Most common fuel type

### Charts Used
- Listings by State → Filled Map
- Condition Mix → Bar Chart
- Transmission Preference → Pie Chart
- Top Brands → Horizontal Bar Chart (Top Manufacturers)

### Key Insight
Market demand is driven by a few dominant vehicle types, brands, and regions, with strong user preference for automatic transmission and well-maintained vehicles.

---

## Filters

The dashboards include interactive filters for deeper analysis:

- State
- Vehicle Type
- Price Category
- Year (Range Slider)
- Fuel Type (optional)

All filters are applied globally across relevant sheets.

---

## Design Approach

- Consistent color theme (purple gradient) for visual harmony
- Minimal and clean layout to improve readability
- Avoided redundant charts across dashboards
- Used varied chart types to improve storytelling
- Focused on insight-driven visuals rather than decorative elements

---

## Tools Used

- Tableau Public (Visualization)
- CSV Dataset (Data Source)

---

## Conclusion

This project demonstrates how structured dashboards can transform raw data into meaningful insights. By dividing the analysis into overview, pricing behavior, and segmentation, the dashboards provide a clear and logical understanding of the used car market.

---