# Used Cars Price Prediction Capstone

## Project Overview
This project analyzes a used cars dataset to understand the main factors that influence listing prices and to build predictive models for estimating used car prices from listing features.

The dataset used in this project is `vehicles.csv`, which contains 15,000 sampled rows and 26 columns. This provides a strong foundation for dataset understanding, data cleaning, exploratory data analysis (EDA), feature preparation, model building, and evaluation.

## Business Problem
Used car buyers, sellers, and dealerships need realistic pricing guidance. Listing prices are influenced by many factors such as vehicle age, mileage, manufacturer, fuel type, transmission, condition, and location. Without a data-driven approach, pricing decisions can be inconsistent and inefficient.

This project aims to build a model that can predict used car prices and identify the features that most strongly affect price.

## Project Goal
The primary goal of this capstone is:

**Predict used car price from listing features**

A secondary goal is:

**Identify the most important factors affecting used car prices**

## Objectives
- Inspect and understand the dataset structure and column meanings.
- Identify the target variable for prediction.
- Assess missing values, duplicate rows, incorrect data types, and outliers.
- Clean and standardize the dataset.
- Perform EDA to uncover price trends and patterns.
- Build baseline machine learning models for price prediction.
- Compare model performance using regression metrics.
- Present business insights and recommendations.

## Project Workflow
1. Define the problem and success criteria.
2. Understand the dataset and data quality issues.
3. Clean and preprocess the data.
4. Perform exploratory data analysis.
5. Engineer features for modeling.
6. Train baseline and tree-based regression models.
7. Evaluate models using MAE, RMSE, and R-squared.
8. Summarize findings and recommendations.

## Suggested Research Questions
- How does mileage affect used car price?
- How does model year affect price?
- Which manufacturers or vehicle categories command higher prices?
- How do condition, fuel type, and transmission influence price?
- Which features are most useful for predicting price?

## Models To Start With
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- XGBoost Regressor (if allowed)

## Evaluation Metrics
- MAE
- RMSE
- R-squared

## Project Structure
```text
Section-D_Group-13_Used_Cars_Market_Analysis/
├── DVA-focused-Portfolio/
├── DVA-oriented-Resume/
├── data/
│   ├── raw/
│   └── processed/
├── docs/
├── notebooks/
├── reports/
├── scripts/
├── tableau/
│   └── screenshots/
├── README.md
├── requirements.txt
└── .gitignore
```

## Roles / Work Buckets
Even for a solo capstone, these can be used as responsibility areas:

- Project Lead: defines scope, timeline, and final deliverables.
- Data Analyst: performs EDA and visual storytelling.
- Data Engineer: handles cleaning, null values, and preprocessing.
- ML Engineer: builds and evaluates predictive models.
- Documentation / Presentation Lead: prepares the README, report, and presentation.

## Deliverables
- Cleaned dataset or documented cleaning workflow
- EDA notebook with visual insights
- Baseline regression models
- Final comparison of model results
- Capstone report / presentation

## Dataset Note
The raw dataset is stored locally in `data/raw/vehicles.csv`. Because of its size, it should remain out of version control and be referenced in project documentation instead of being uploaded to GitHub directly.
