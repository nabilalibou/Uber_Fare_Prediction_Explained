# Uber Ride Pricing Analysis - January 2023, Paris

This repository contains a Jupyter Notebook detailing an in-depth analysis of Uber's ride pricing algorithm based on historical trip data from Paris during January 2023.  

This project originated as a **challenging homework assignment given by a company in Paris**. I did not end up joining them but i kept the exercice as it provides a good opportunity to practice and apply various data science methodologies. The goal was to explore the provided dataset, build robust predictive models for ride fares, evaluate their performance, and critically analyze the factors influencing pricing, including potential biases or unutilized variables within the data.

**Exercice statement**

*As a newly recruited data scientist member of the XXX team at our XXX company, your first mission is to identify any potential biases in the pricing algorithm of our ride-hailing platform.*  
*You will begin by exploring the dataset and generating the visualizations that you deem relevant.*  
*You will then attempt to model the ride fares using the model(s) of your choice. You will evaluate the quality of your model(s) and produce a critical analysis of the results.*  
*If time permits, you may attempt to answer the following question: Is it possible to identify any biases in the dataset or to determine which variables, among those at your disposal, are not being utilized by our algorithm in its ride fare calculation?*  

## Project Overview

I was provided with a CSV file containing the historical record of **10,000 rides** completed in Paris throughout January 2023. Each entry includes three core variables: `timestamp` (the time of the ride request), `raw_start_location` (the pickup address), and `raw_end_location` (the destination address).

The analysis unfolds in several key stages:

1.  **Exploratory Data Analysis (EDA):**  
Initial exploration of the dataset to understand its structure, distributions, and identify any immediate patterns or anomalies. This involves generating relevant visualizations to highlight key characteristics of Uber trips in Paris.
2.  **Data Preprocessing & Feature Engineering:**  
Extensive cleaning, transformation, and creation of new features from raw timestamp and location data.
3.  **Fare Modeling:**  
Development of advanced machine learning models, culminating in a **stacking ensemble** approach, to predict ride fares. This stage focuses on selecting appropriate models, hyperparameter tuning, and robust evaluation methodologies.
4.  **Critical Analysis of Results:**  
A deep dive into the performance of the developed models, including an examination of feature importances. This analysis aims to interpret model findings in the context of Uber's pricing strategies and identify variables that appear to significantly impact fares.
5.  **Bias Detection & Variable Utilization:**  
An investigation into potential biases within the dataset itself, or an attempt to determine if certain available variables are not being effectively utilized by Uber's actual pricing mechanism.

## Data Sources

To support this analysis, the following supplementary datasets have been provided:

* **Météo-France Weather Data:** Historical temperature and rain levels for Paris during January 2023, recorded on an hourly basis. The `rain_level` column categorizes precipitation from 0 (no rain) to 3 (heavy rain).
* **National Address Database (Base Adresse Nationale) for Paris:** Accessible at [https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-75.csv.gz](https://adresse.data.gouv.fr/data/ban/adresses/latest/csv/adresses-75.csv.gz). This comprehensive database provides essential geographical information for Parisian addresses, crucial for enriching our raw location data.

**Note on Address Format:** Addresses in the primary Uber dataset are formatted as `[number][suffix], [street name], [city name]` (e.g., `[rep]` corresponds to suffixes like "bis", "ter", etc., for building numbers). Careful parsing and geocoding was required to effectively integrate this information.

## Repository Contents

* `uber_pricing_analysis.ipynb`: The main Jupyter Notebook containing all the code for data loading, preprocessing, EDA, model training, evaluation, and feature importance analysis.
* `requirements.txt`: A file listing all the Python dependencies required to run the Jupyter Notebook successfully.

## ⚙️ Installation

To get this project up and running on your local machine, follow these simple steps:

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/nabilalibou/Uber_Fare_Prediction_Explained.git](https://github.com/nabilalibou/Uber_Fare_Prediction_Explained.git)
    ```
2.  **Navigate to the project directory:**
    ```bash
    cd Uber_Fare_Prediction_Explained
    ```
3.  **Install the required Python dependencies:**
    ```bash
    pip install -r requirements.txt
    ```
4.  **Launch Jupyter Notebook and open `uber_pricing_analysis.ipynb`:**
    ```bash
    jupyter notebook
    ```

---

## Key Stages & Summary of Findings

### 1. Initial Data Loading & Inspection
This phase involved understanding the raw dataset's structure, identifying data types, and initial observations regarding the target variable's distribution and potential limitations for direct modeling.

### 2. Basic Data Cleaning & Feature Engineering
Extensive preprocessing was performed on the `timestamp` and `raw_location` data. This included:
* Parsing timestamps to extract temporal features (hour, day of week, etc.).
* Geocoding raw addresses using the National Address Database to obtain precise latitude/longitude coordinates.
* Calculating trip distances from coordinates.

### 3. Outlier Handling & Fee Distribution
Analysis of the `fee` (fare) distribution revealed skewness and the presence of outliers. Log transformation (`np.log1p`) of the `fee` was applied to mitigate the impact of outliers and normalize the distribution for better model performance.

### 4. Analysis of Temporal Patterns and Pricing Behavior
Explored how fares vary by time of day, day of the week, and other temporal factors, identifying peak demand periods and potential pricing strategies.

### 5. Merging Weather Data
Integrated external hourly weather data (temperature, rain levels) for Paris to investigate its correlation with ride fares.

### 6. Preparing Spatial Data
Further refined geographical features by extracting arrondissement information from coordinates and exploring spatial relationships.

### 7. Overall Correlation Matrix & Feature Selection
A correlation heatmap was generated to understand relationships between features and the target variable, guiding feature selection decisions.

### 8. Quick Prediction Tests & Metric Selection
Initial basic predictive tests were conducted using subsets of features. **Mean Absolute Error (MAE)** was chosen as the primary evaluation metric.

### 9. Feature Importance Analysis
Key findings included:
* The overwhelming influence of **`hour`** (when one-hot encoded).
* The significant but contrasting roles of **`distance`**.
* High importance of **location specificity** (coordinates and arrondissements).
* **Low importance** for environmental factors (weather) and standard weekday indicators.

### 10. Model Selection & Individual Hyperparameter Tuning
A diverse set of individual regression models were explored and their hyperparameters fine-tuned, serving as strong base learners for the subsequent ensemble:
* **Linear Models:** Capable of capturing linear relationships.
* **Distance-Based Models:** Such as SVR, for their ability to model complex non-linear boundaries.
* **Tree-Based Models:** Like CatBoost, known for handling categorical features and complex interactions.
* **Neural Network Models:** MLPRegressor, for its flexibility in approximating highly non-linear functions.

### 11. Ensemble Modeling: Stacking Architecture & Final Meta-Model

To achieve superior predictive performance, a **stacking ensemble** approach was implemented. This method combines the predictions of several diverse base models using a "meta-learner" to make the final prediction.

The final ensemble is a **`StackingRegressor`** with a **`GradientBoostingRegressor`** serving as its meta-learner. This architecture utilizes the strengths of four distinct base models:

1.  **PolynomialFeatures + Ridge:** A L2-regularized **linear model** operating in a transformed, higher-dimensional feature space, chosen for its ability to capture explicit polynomial non-linearities. Features utilized: all, excluding `weekday_num`.

2.  **SVR with Radial Basis Function (RBF) Kernel:** A **kernel-based non-linear model**, inherently capable of modeling complex relationships and tunable for robustness to outliers (with an $\epsilon$ parameter). Features utilized: all, excluding `weekday_num` and `temperature`.

3.  **CatBoostRegressor:** A robust **gradient boosting machine** (tree-based ensemble), renowned for its powerful handling of heterogeneous data (especially categorical features) and strong generalization capabilities. Features utilized: all available.

4.  **PolynomialFeatures + MLPRegressor:** A highly flexible **non-linear neural network model**, trained on a transformed feature space (`PolynomialFeatures` of degree 2) to approximate intricate non-linear relationships. Features utilized: all, excluding `weekday_num`.

The `GradientBoostingRegressor` meta-learner was then fine-tuned using **Bayesian Optimization (`skopt.BayesSearchCV`)** to find its optimal hyperparameters (e.g., `n_estimators`, `learning_rate`, `max_depth`, `subsample`).

### 12. Final Model Performance

The performance of the final fine-tuned meta-model, **`STACKING_GradientBoosting`**, on cross-validation is:
* **CV MAE: 1.2593 ± 0.0284**

### 13. Evaluation of the fully-trained Meta-Model on the Holdout Set

The final, fully-trained ensemble model was evaluated on a completely unseen holdout test set to assess its true generalization capability. Key visualizations generated include:

* **1. Actual vs. Predicted Values Plot:** To visually assess the model's accuracy and identify any systematic biases across the range of fares.
* **2. Residuals vs. Predicted Values Plot:** To check for patterns in the errors (e.g., heteroscedasticity or non-linearity in residuals) that might indicate uncaptured relationships.
* **3. Distribution of Residuals:** To inspect the normality and spread of the prediction errors.