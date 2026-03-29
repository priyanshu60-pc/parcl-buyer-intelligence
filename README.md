# 🏠 Parcl Buyer Intelligence Dashboard

🚀 **Live App:**  
https://parcl-buyer-intelligence-ycgmdyktjkxanappvy7ehxu.streamlit.app/

---

## 📌 Project Overview

This project implements an **AI-driven buyer segmentation and investment profiling system** for the real estate domain.

Using **unsupervised machine learning (clustering)**, the system identifies hidden patterns in buyer behavior and categorizes clients into meaningful segments. These insights help real estate platforms like Parcl improve **marketing strategies, customer targeting, and investment decision-making**.

---

## 🎯 Problem Statement

Parcl lacked a data-driven understanding of:

- Different types of property buyers  
- Investment motivations across demographics  
- Geographic variations in buyer behavior  
- Financing patterns (loan vs self-funded buyers)  

This resulted in:

- Inefficient marketing spend  
- Generic recommendations  
- Poor investor targeting  

---

## 🧠 Solution Approach

We applied **Machine Learning (Clustering Algorithms)** to segment buyers based on behavioral and demographic data.

### ✔ Key Steps:
1. Data Cleaning  
2. Feature Encoding  
3. Feature Scaling  
4. Clustering (K-Means + Hierarchical)  
5. Cluster Evaluation (Elbow Method, Silhouette Score)  
6. Cluster Interpretation  

---

## 📊 Dataset Features

| Feature | Description |
|--------|------------|
| client_id | Unique client identifier |
| client_type | Individual / Corporate |
| gender | Buyer gender |
| country | Country of residence |
| region | Geographic region |
| date_of_birth | Age indicator |
| acquisition_purpose | Investment / Personal |
| loan_applied | Financing indicator |
| referral_channel | Acquisition source |
| satisfaction_score | Customer rating |

---

## ⚙️ Machine Learning Pipeline

### 🔹 Feature Engineering
- One-Hot Encoding
- Label Encoding

### 🔹 Scaling
- StandardScaler / MinMaxScaler

### 🔹 Models Used
- K-Means Clustering  
- Hierarchical Clustering  

### 🔹 Evaluation Metrics
- Elbow Method  
- Silhouette Score  

---

## 📌 Identified Buyer Segments

| Cluster | Segment Name | Description |
|--------|-------------|------------|
| C1 | Global Investors | High-income, investment-focused buyers |
| C2 | First-Time Buyers | Younger, loan-dependent buyers |
| C3 | Corporate Buyers | Businesses purchasing multiple properties |
| C4 | Luxury Investors | High satisfaction, premium investments |

---

## 📊 Streamlit Dashboard Features

### ✔ Buyer Segmentation Overview
- Cluster distribution visualization  

### ✔ Investor Behavior Dashboard
- Investment patterns by segment  

### ✔ Geographic Analysis
- Buyer distribution across regions  

### ✔ Segment Insights Panel
- Statistics per cluster  

---

## 🎛 User Controls

Users can filter data by:

- Country  
- Region  
- Acquisition Purpose  
- Client Type  

---

## 🧩 Tech Stack

- Python 🐍  
- Pandas, NumPy  
- Scikit-learn  
- Streamlit  
- Plotly / Matplotlib  

---

## 🚀 How to Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/parcl-buyer-intelligence.git

# Navigate to project
cd parcl-buyer-intelligence

# Install dependencies
pip install -r requirements.txt

# Run the app
streamlit run app.py
