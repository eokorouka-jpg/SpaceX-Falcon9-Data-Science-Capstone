# SpaceX Falcon 9 Landing Prediction — Data Science Capstone

**Author:** Eke Uka Okoro  
**Project:** IBM Data Science Professional Certificate — Applied Data Science Capstone  
**GitHub:** https://github.com/eokorouka-jpg/SpaceX-Falcon9-Data-Science-Capstone

## 1. Project Overview

This project investigates the factors influencing the successful landing of SpaceX Falcon 9 first-stage boosters.

Using Python, SQL, data visualisation, interactive dashboards and machine learning, the project explores historical launch data and develops classification models to predict landing outcomes.

The project demonstrates an end-to-end data science workflow, from data collection and cleaning to exploratory analysis, predictive modelling and communicating business insights.

## 2. Business Problem

SpaceX reduces launch costs by recovering and reusing Falcon 9 first-stage boosters.

Predicting whether a first-stage booster will land successfully can help assess launch outcomes and support cost-related analysis.

**Main research question:**

Can historical launch characteristics be used to predict the successful landing of a Falcon 9 first-stage booster?

## 3. Project Objectives

- Collect Falcon 9 launch data from the SpaceX API and Wikipedia.
- Clean and prepare the data for analysis.
- Investigate relationships between launch characteristics and landing success.
- Analyse launch outcomes using SQL and Python.
- Explore launch-site geography using Folium.
- Build an interactive dashboard using Plotly Dash.
- Train and evaluate machine learning classification models.
- Identify the best-performing models and communicate the findings.

## 4. Technologies and Tools

**Programming:** Python, SQL

**Data analysis:** Pandas, NumPy

**Data visualisation:** Matplotlib, Seaborn, Plotly

**Interactive applications:** Plotly Dash, Folium

**Machine learning:** Scikit-learn

**Development tools:** Jupyter Notebook, VS Code, GitHub

## 5. Project Methodology

### Data Collection

Collected launch information through the SpaceX API and Wikipedia web scraping.

### Data Wrangling

Prepared the datasets by handling missing values, creating landing outcome labels and transforming variables for analysis.

### Exploratory Data Analysis

Used Python visualisations and SQL queries to investigate launch sites, payload mass, orbit types and landing outcomes.

### Interactive Visual Analytics

Created geographical launch-site maps using Folium and an interactive Plotly Dash application with launch-site filters, payload selection and landing success visualisations.

### Predictive Analysis

Prepared 90 launch records with 80 encoded features for machine learning.

The dataset was split into 80% training and 20% testing data.

Four classification algorithms were evaluated using GridSearchCV with 10-fold cross-validation:

1. Logistic Regression
2. Support Vector Machine (SVM)
3. Decision Tree
4. K-Nearest Neighbours (KNN)

## 6. Key Findings

### Launch Site Analysis

In the 56-launch dashboard dataset, KSC LC-39A achieved the highest landing success rate of **76.92%**, with 10 successful landings out of 13 launches.

### Payload Analysis

The 2,000–4,000 kg payload range achieved a landing success rate of **61.90%**, while the 6,000–8,000 kg range recorded 0% success in the dashboard dataset.

These results describe historical observations rather than proving that payload mass alone determines landing success.

### Machine Learning Results

| Model | Test Accuracy |
|---|---:|
| Logistic Regression | 83.33% |
| Support Vector Machine | 83.33% |
| K-Nearest Neighbours | 83.33% |
| Decision Tree | 77.78% |

**Best-performing models:** Logistic Regression, SVM and KNN, each achieving 83.33% test accuracy.

Each of the three models correctly predicted 15 of the 18 test cases.

The confusion matrices showed that false positives were the main classification errors for these models.

## 7. Project Limitations

- The machine learning test dataset contained only 18 launch records.
- Historical performance does not guarantee future landing outcomes.
- Different project stages used datasets of different sizes.
- Additional data and further validation would improve confidence in the results.

## 8. Project Files

This repository contains the project notebooks, Python scripts and datasets covering:

- SpaceX API data collection
- Wikipedia web scraping
- Data wrangling and feature engineering
- SQL exploratory data analysis
- Python exploratory data analysis
- Folium launch-site mapping
- Plotly Dash interactive dashboard
- Machine learning prediction
- Final capstone presentation (PDF)

## 9. Conclusion

The SpaceX Falcon 9 Capstone demonstrates the application of an end-to-end data science workflow to a real-world prediction problem.

The analysis identified differences in historical landing performance across launch sites, payload ranges and booster versions.

Logistic Regression, SVM and KNN achieved the joint-highest test accuracy of 83.33%.

The project strengthened practical skills in Python, SQL, data preparation, exploratory analysis, interactive visualisation, machine learning and communicating analytical findings.

## 10. Author

**Eke Uka Okoro**

Aspiring Data Analyst | Data Scientist | Machine Learning Practitioner

**GitHub:** https://github.com/eokorouka-jpg
