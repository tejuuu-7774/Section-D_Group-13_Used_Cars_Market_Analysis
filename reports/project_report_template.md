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
- Rows: 426,880
- Columns: 26
- Target variable: `price`

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
- The dataset contains substantial missing values in several columns.
- `county` is completely missing and is a strong candidate for removal during cleaning.
- `size`, `cylinders`, `condition`, `VIN`, `drive`, and `paint_color` have large amounts of missing data.
- `manufacturer`, `model`, `fuel`, `odometer`, `lat`, and `long` also contain null values that will need cleaning decisions.
- No duplicate rows were identified in the initial within-chunk scan.

## Highest Null Count Columns
| Column | Null Count |
|---|---:|
| county | 426,880 |
| size | 306,361 |
| cylinders | 177,678 |
| condition | 174,104 |
| VIN | 161,042 |
| drive | 130,567 |
| paint_color | 130,203 |
| type | 92,858 |
| manufacturer | 17,646 |
| title_status | 8,242 |
| lat | 6,549 |
| long | 6,549 |
| model | 5,277 |
| odometer | 4,400 |
| fuel | 3,013 |

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
