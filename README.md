
#  Bike Sharing Rental Demand Prediction

<p align="center">

![Python](https://img.shields.io/badge/Python-3.11-blue?style=for-the-badge&logo=python)
![Pandas](https://img.shields.io/badge/Pandas-Data%20Analysis-orange?style=for-the-badge&logo=pandas)
![Scikit-Learn](https://img.shields.io/badge/Scikit--Learn-Machine%20Learning-red?style=for-the-badge&logo=scikit-learn)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-FF4B4B?style=for-the-badge&logo=streamlit)
![Status](https://img.shields.io/badge/Project-Completed-success?style=for-the-badge)

</p>

---

#  Project Overview

Bike-sharing systems have become an important mode of urban transportation. Predicting bike rental demand helps companies optimize:

-  Bike availability
-  Pricing strategies
-  Station management
-  Business planning
-  Customer satisfaction

This project develops a complete **Machine Learning Regression Pipeline** to accurately predict bike rental demand based on weather conditions, seasonal information, holidays, working days, and time-based features.

---

#  Business Objective

The objective is to predict the total number of bike rentals (`cnt`) using various environmental and temporal factors.

Accurate prediction enables:

- Better bike allocation
- Reduced customer waiting time
- Improved operational efficiency
- Demand forecasting
- Better inventory planning

---

# 📂 Dataset Information

The dataset contains hourly bike rental information with weather and seasonal data.

### Features

| Feature | Description |
|----------|-------------|
| instant | Record Index |
| dteday | Date |
| season | Season |
| yr | Year |
| mnth | Month |
| hr | Hour |
| holiday | Holiday Indicator |
| weekday | Day of Week |
| workingday | Working Day Indicator |
| weathersit | Weather Condition |
| temp | Temperature |
| atemp | Feeling Temperature |
| hum | Humidity |
| windspeed | Wind Speed |
| casual | Casual Users |
| registered | Registered Users |
| cnt | Total Bike Rentals (Target Variable) |

---

#  Technologies Used

- Python
- Google Colab
- Pandas
- NumPy
- Matplotlib
- Seaborn
- Scikit-Learn
- Joblib
- Streamlit

---

#  Project Workflow

```
Business Understanding
        │
        ▼
Data Collection
        │
        ▼
Exploratory Data Analysis
        │
        ▼
Data Visualization
        │
        ▼
Feature Engineering
        │
        ▼
Model Building
        │
        ▼
Hyperparameter Tuning
        │
        ▼
Model Evaluation
        │
        ▼
Model Deployment
```

---

#  Exploratory Data Analysis

Performed:

- Dataset Exploration
- Missing Value Analysis
- Duplicate Record Detection
- Outlier Detection
- Statistical Summary
- Correlation Analysis
- Target Variable Distribution

---

#  Data Visualization

Visualizations include:

- Histogram
- Scatter Plot
- Line Plot
- Bar Plot
- Box Plot
- Violin Plot
- Pair Plot
- Heatmap
- Time Series Analysis

---

#  Feature Engineering

Implemented:

- Date Feature Extraction
- Peak Hour Identification
- Weekend Indicator
- Temperature Difference
- Weather Mapping
- Season Mapping
- One-Hot Encoding
- Label Encoding
- Feature Scaling
- Min-Max Scaling

---

#  Machine Learning Models

The following regression models were developed:

✅ Decision Tree Regressor

✅ Random Forest Regressor

✅ Gradient Boosting Regressor

---

#  Hyperparameter Tuning

Performed using **GridSearchCV (5-Fold Cross Validation)**.

Optimized parameters:

- max_depth
- n_estimators
- learning_rate
- min_samples_split
- min_samples_leaf
- max_features
- subsample

---

#  Model Evaluation

Evaluation Metrics:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

Additional evaluation:

- Actual vs Predicted Plot
- Residual Plot
- Residual Distribution
- QQ Plot
- Feature Importance

---

#  Deployment

The final optimized model was deployed using **Streamlit**.

Users can:

- Enter input values
- Predict bike rental demand instantly
- View predicted rental count

---

#  Project Structure

```
BikeRental_Project/
│
|-- Dataset.csv
|--BikeRental_Feature_Engineered.csv
|-- BikeRental_Model.pkl
|-- feature_columns.pkl
|-- app.py
|-- Prediction_Results.csv
|-- Model_Evaluation.csv
|-- README.md
|-- requirements.txt
```

---

# ▶️ Installation

Clone the repository

```bash
git clone https://github.com/yourusername/BikeRental_Project.git
```

Move into the project

```bash
cd BikeRental_Project
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# ▶ Run the Application

```bash
streamlit run app.py
```

---

#  Sample Output

```
Bike Rental Demand Prediction

Temperature      : 0.45

Humidity         : 0.62

Wind Speed       : 0.18

Season           : Summer

Working Day      : Yes

Predict

Predicted Bike Rentals

➡️ 326 Bikes
```

---

#  Results

The optimized regression model successfully predicts bike rental demand using weather and temporal information.

The project demonstrates an end-to-end machine learning workflow from data preprocessing to deployment.

---

#  Future Improvements

- Deep Learning Models
- XGBoost
- LightGBM
- CatBoost
- Real-Time Weather API
- Cloud Deployment
- Mobile Application
- Live Prediction Dashboard

---

#  Requirements

```text
pandas
numpy
matplotlib
seaborn
scikit-learn
streamlit
joblib
```

---

# 👨 Author

**Bhuvan Madihalli**

🎓 Information Science Engineering Graduate

💡 Interested in:

- Artificial Intelligence
- Machine Learning
- Data Science
- Software Development

---

=======
# Bike_Sharing_Rental
Developed an end-to-end machine learning pipeline to predict bike rental demand using weather and temporal features. Implemented EDA, feature engineering, Decision Tree, Random Forest, Gradient Boosting, GridSearchCV optimization, model evaluation, and Streamlit deployment.

