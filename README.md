# 📊 Content Monetization Modeler  

> Predicting YouTube Ad Revenue with Regression Models + Streamlit App  

---

## Project Overview

Content Monetization Modeler is a machine learning project aimed at predicting **YouTube ad revenue** for videos based on various performance and contextual features. This project leverages **regression modeling, feature engineering, EDA, and Streamlit** to help creators and media companies optimize content strategy, forecast revenue, and enhance monetization.

This project aims to provide a **predictive solution** through machine learning.  


---

## 💡 Problem Statement

With creators and media companies relying heavily on YouTube for revenue, it is crucial to predict ad revenue accurately. This project builds a **Linear Regression model** (along with other regression models) to estimate ad revenue per video and integrates it into an interactive **Streamlit app**.

---

## 🎯 Business Use Cases

- **Content Strategy Optimization:** Identify content types that generate higher revenue.  
- **Revenue Forecasting:** Predict expected income from future uploads.  
- **Creator Support Tools:** Provide analytics services to YouTubers.  
- **Ad Campaign Planning:** Forecast ROI for advertisers based on video performance metrics.

---

## 🛠 Skills Learned

- Regression Models (Linear Regression, Decision Tree, Random Forest, Gradient Boosting, XGBoost)  
- Predictive Modeling & Feature Engineering  
- Data Cleaning, Missing Value Handling & Outlier Detection  
- Exploratory Data Analysis (EDA)  
- Data Visualization (Matplotlib, Seaborn, Plotly)  
- Categorical Encoding  
- Model Evaluation (R², RMSE, MAE)  
- Streamlit App Development  
- Python, Pandas, Scikit-learn

---

## 📂 Dataset

- **Name:** YouTube Monetization Modeler  
- **Format:** CSV  
- **Size:** ~122,000 rows  
- **Source:** Synthetic (for learning purposes)  
- **Target Variable:** `ad_revenue_usd`

### Features:

| Column                  | Description                                                      |
|-------------------------|------------------------------------------------------------------|
| video_id                | Unique identifier for video                                       |
| date                    | Upload/report date                                                |
| views, likes, comments  | Performance metrics                                               |
| watch_time_minutes      | Total watch time in minutes                                       |
| video_length_minutes    | Length of the video                                              |
| subscribers             | Channel subscriber count                                          |
| category, device, country | Contextual info                                                 |
| ad_revenue_usd          | Revenue generated (target)                                        |

---

## 🧹 Data Preprocessing

- Removed ~2% duplicate records.  
- Handled ~5% missing values using **mean imputation**.  
- Categorical encoding for `category`, `device`, `country`.  
- Feature scaling using **StandardScaler**.  
- Engineered features:
  - **Engagement Rate:** `(likes + comments) / views`  
  - **Avg Watch Time per View:** `watch_time_minutes / views`  

---

## 📊 Exploratory Data Analysis (EDA)

- Visualized distributions and outliers for `views`, `likes`, `comments`, `watch_time_minutes`, `video_length_minutes`, `subscribers`.  
- Examined correlation matrix to identify key revenue drivers.  
- Boxplots and violin plots to detect outliers and trends.  

---

## 🤖 Model Building & Evaluation

Tested multiple regression models:

| Model               | R²       | RMSE     | MAE      |
|--------------------|----------|----------|----------|
| Linear Regression  | 0.952582 | 13.4789  | 3.0888   |
| Gradient Boosting  | 0.952030 | 13.5571  | 3.6534   |
| XGBoost            | 0.950910 | 13.7145  | 3.6760   |
| Random Forest      | 0.950118 | 13.8246  | 3.5326   |
| Decision Tree      | 0.899897 | 19.5842  | 5.3270   |

- **Best Model:** Linear Regression (highest R², lowest MAE)  
- **Feature Importance:** Engagement rate, views, watch time, likes, and subscribers are top drivers of ad revenue.

---

## 🚀 Streamlit App

The app provides:

- Paste YouTube video URL to fetch analytics using YouTube API.  
- Displays **Views, Likes, Comments, Subscribers, Watch Time, Video Length, Engagement Rate**.  
- Estimates **Ad Revenue** in multiple currencies (USD, INR, BRL, IDR, JPY).  
- Provides actionable **insights** based on engagement rate.

---





