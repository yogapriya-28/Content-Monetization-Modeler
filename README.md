# 📊 Content Monetization Modeler  

> Predicting YouTube Ad Revenue with Regression Models + Streamlit App  

---

## 📖 Overview  
With the growing reliance on YouTube as a revenue source, accurately estimating **ad revenue per video** is critical for creators and media companies.  
This project builds and compares multiple **regression models** to predict ad revenue (`ad_revenue_usd`) using video performance and contextual features.  
A simple **Streamlit web app** is also developed for interactive predictions.  

---

## 🎯 Problem Statement  
YouTube creators and media businesses need tools to:  
- Forecast income from upcoming videos  
- Optimize content strategy for better ROI  
- Support advertiser planning and campaign design  

This project aims to provide a **predictive solution** through machine learning.  

---

## 🚀 Features  
✔️ Exploratory Data Analysis (EDA)  
✔️ Data Cleaning & Preprocessing  
✔️ Feature Engineering (e.g., Engagement Rate)  
✔️ Regression Models: Linear, Ridge, Lasso, Random Forest, Gradient Boosting  
✔️ Evaluation Metrics: R², RMSE, MAE  
✔️ Insights on revenue-driving features  
✔️ Streamlit App for interactive predictions  

---

## 📂 Dataset  
- **Name:** YouTube Monetization Modeler  
- **Size:** ~122,000 rows  
- **Format:** CSV (synthetic dataset)  
- **Target Variable:** `ad_revenue_usd`  
- **Key Features:**  
  - `views`, `likes`, `comments`  
  - `watch_time_minutes`, `video_length_minutes`  
  - `subscribers`, `category`, `device`, `country`  
  - `date`, `video_id`  

---

## 🔧 Tech Stack  
- **Language:** Python  
- **Libraries:** Pandas, NumPy, Scikit-learn, Matplotlib, Seaborn  
- **App:** Streamlit  
- **Version Control:** Git & GitHub  

---

## 📊 Project Workflow  
1. **Dataset Exploration & EDA**  
2. **Preprocessing & Missing Value Handling**  
3. **Feature Engineering**  
4. **Model Building & Tuning**  
5. **Model Evaluation (R², RMSE, MAE)**  
6. **Streamlit App Development**  
7. **Insights & Documentation**  

---

## 📈 Results  
- Best Model: ✅ (e.g., Ridge / Lasso / Random Forest → update after evaluation)  
- R² ≈ *0.95+*  
- RMSE ≈ *13.4*  
- MAE ≈ *3.0*  
- Engagement rate, watch time, and subscribers were **strong predictors** of revenue.  

---

## 🖥️ Streamlit App  
To run the app locally:  

```bash
# Clone repo
git clone https://github.com/your-username/content-monetization-modeler.git

# Navigate to folder
cd content-monetization-modeler

# Install dependencies
pip install -r requirements.txt

# Run Streamlit app
streamlit run app.py
