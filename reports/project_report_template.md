# Phase 1 Report

## Title
Used Car Price Prediction and Feature Impact Analysis

## Project Overview
This project analyzes a used cars dataset to understand the main factors that influence listing prices and to build predictive models for estimating used car prices from listing features.

## Business Problem
Used car buyers, sellers, and dealerships need realistic pricing guidance. Listing prices are influenced by factors such as vehicle age, mileage, manufacturer, fuel type, transmission, condition, and location. A data-driven approach helps make pricing decisions more consistent and informed.

## Project Goal
The primary goal of this capstone is to predict used car price from listing features. A secondary goal is to identify the most important factors affecting used car prices.

## Dataset Used
- File name: `vehicles.csv`
- Original dataset size: 426,880 rows × 26 columns  
- Sampled dataset used for analysis: 15,000 rows × 26 columns  
- Target variable: `price`

Due to the large size of the dataset, a representative sample of 15,000 rows was used for efficient analysis and model experimentation.

## Dataset Columns
- `id`
- `url`
- `region`
- `region_url`
- `price`
- `year`
- `manufacturer`
- `model`
- `condition`
- `cylinders`
- `fuel`
- `odometer`
- `title_status`
- `transmission`
- `VIN`
- `drive`
- `size`
- `type`
- `paint_color`
- `image_url`
- `description`
- `county`
- `state`
- `lat`
- `long`
- `posting_date`

## Initial Data Quality Findings
- The sampled dataset (15,000 rows) contains missing values across several columns.
- `county` is completely missing and is a strong candidate for removal during cleaning.
- `size`, `cylinders`, `condition`, `VIN`, `drive`, and `paint_color` have large amounts of missing data.
- `manufacturer`, `model`, `fuel`, `odometer`, `lat`, and `long` also contain null values that will need cleaning decisions.
- No duplicate rows were identified in the sampled dataset.

## Highest Null Count Columns (Sampled Dataset)
| Column | Null Count |
|---|---:|
| county | 15000 |
| size | 11074 |
| cylinders | 6215 |
| condition | 6204 |
| VIN | 5599 |
| drive | 4425 |
| paint_color | 4182 |
| type | 3317 |
| manufacturer | 660 |
| title_status | 263 |
| lat | 55 |
| long | 55 |
| model | 215 |
| odometer | 174 |
| fuel | 98 |
Note: All null counts are based on the sampled dataset (15,000 rows) used for analysis.

## Initial Data Type Observations
- `price` is stored as an integer field and is the natural target variable.
- `year`, `odometer`, `lat`, and `long` appear as numeric columns with missing values.
- `posting_date` is currently stored as text and can be converted to datetime during preprocessing.
- Several vehicle attributes are categorical and will require standardization before modeling.

## Roles / Work Buckets
- Project Lead: defines scope, timeline, and final deliverables.
- Data Analyst: performs EDA and visual storytelling.
- Data Engineer: handles cleaning, missing values, and preprocessing.
- ML Engineer: builds and evaluates predictive models.
- Documentation / Presentation Lead: organizes the written report and presentation.

## Phase 1 Summary
Phase 1 established the project objective, identified the target variable, documented the dataset structure, and reviewed the main data quality issues. The dataset is large enough for meaningful analysis, and the missing-value pattern provides a clear basis for the data cleaning stage.

The original dataset is large and rich, and the sampled subset is sufficient for meaningful analysis and modeling.