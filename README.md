# Climate & Mental Health Analysis

## Project Overview
This study investigates the impact of climate-related disasters on mental health, specifically focusing on the 2021 Heat Dome and Atmospheric River (Floods) in British Columbia. 

The analysis utilizes the **Kessler Psychological Distress Scale (K6)**, a 6-item psychometric tool (scoring 0-24) that measures symptoms of anxiety, depression, and functional impairment.

## Dataset Information
The analysis is based on the **Climate Distress Monitoring Survey (CDMS)**. 
* **Source:** Mental Health and Climate Change Alliance (MHCCA)
* **Link:** [MHCCA Datasets](https://mhcca.ca/datasets)
* **Description:** This dataset provides comprehensive insights into the mental health impacts of climate events, enabling researchers to identify trends and vulnerable populations.

## Research Focus
The project examines the correlation between K6 scores and:
* **Actual Exposure:** Direct impact from the 2021 Heat Dome and Flooding events.
* **Risk Perception:** Individual perception of environmental threats.
* **Demographics:** Gender identity, age, income levels, and education.

## Methodology
To ensure statistical rigor, the following methods were implemented:
* **Independent Samples T-test:** To compare mean distress levels between two distinct groups.
* **One-Way ANOVA:** To evaluate differences in mental distress across multiple categorical groups (e.g., income brackets, age groups).
* **Multiple Linear Regression:** To estimate the simultaneous effect of socio-demographic variables and identify key predictors of psychological distress.

## Key Statistical Results
* **Heat Dome Impact:** Statistically significant correlation with increased K6 scores ($F = 24.39, p < 0.001$).
* **Flood Impact:** Statistically significant correlation with mental distress ($F = 16.89, p < 0.001$).
* **Vulnerable Groups:** Regression analysis identified **Genderfluid**, **Trans woman**, and **Non-binary** individuals as groups with significantly higher distress levels.
* **Protective Factors:** Higher annual income ($100,000+) and older age (65+) were strong predictors of lower psychological distress.

## Technologies Used
* **Language:** Python
* **Libraries:** Pandas, Statsmodels, Scipy, Seaborn, Matplotlib

## How to Run
1. Ensure Python is installed.
2. Install dependencies: `pip install pandas seaborn statsmodels scipy matplotlib`
3. Run the analysis script: `python CDMS_K6_Analysis_Code.py`
