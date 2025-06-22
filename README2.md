# Uber Ride Pricing Analysis - January 2023, Paris

This repository contains a Jupyter Notebook detailing an in-depth analysis of Uber's ride pricing algorithm based on historical trip data from Paris during January 2023. The project aims to explore the provided dataset, build predictive models for ride fares, evaluate their performance, and critically analyze the factors influencing pricing, including potential biases or unutilized variables within the data.

## Project Overview

As a newly recruited data scientist, my initial mission is to investigate potential biases in the pricing algorithm of a ride-sharing platform. I've been provided with a CSV file containing the historical record of rides completed in Paris throughout January 2023. Each entry includes three core variables: `timestamp` (the time of the ride request), `raw_start_location` (the pickup address), and `raw_end_location` (the destination address).

The analysis unfolds in several key stages:

1.  **Exploratory Data Analysis (EDA):** Initial exploration of the dataset to understand its structure, distributions, and identify any immediate patterns or anomalies. This involves generating relevant visualizations to highlight key characteristics of Uber trips in Paris.
2.  **Fare Modeling:** Development of one or more machine learning models to predict ride fares. This stage focuses on selecting appropriate models, feature engineering, and robust evaluation methodologies to assess model quality.
3.  **Critical Analysis of Results:** A deep dive into the performance of the developed models, including an examination of feature importances. This analysis aims to interpret model findings in the context of Uber's pricing strategies and identify variables that appear to significantly impact fares.
4.  **Bias Detection & Variable Utilization:** An investigation into potential biases within the dataset itself, or an attempt to determine if certain available variables are not being effectively utilized by Uber's actual pricing mechanism.

## Data Sources

To support this analysis, the following supplementary datasets have been provided:

* **Météo-France Weather Data:** Historical temperature and rain levels for Paris during January 2023, recorded on an hourly basis. The `rain_level` column categorizes precipitation from 0 (no rain) to 3 (heavy rain).
* **National Address Database (Base Adresse Nationale) for Paris:** Accessible at [https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-75.csv.gz](https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-75.csv.gz). This comprehensive database provides essential geographical information for Parisian addresses, crucial for enriching our raw location data.

**Note on Address Format:** Addresses in the primary Uber dataset are formatted as `[number][suffix], [street name], [city name]` (e.g., `[rep]` corresponds to suffixes like "bis", "ter", etc., for building numbers). Careful parsing and geocoding will be required to effectively integrate this information.

## Repository Contents

* `uber_pricing_analysis.ipynb`: The main Jupyter Notebook containing all the code for data loading, preprocessing, EDA, model training, evaluation, and feature importance analysis.
* `requirements.txt`: A file listing all the Python dependencies required to run the Jupyter Notebook successfully.

---