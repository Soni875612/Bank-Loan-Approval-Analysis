# 🏦Bank-Loan-Approval-Analysis🏦

## AI-Powered Credit Risk Intelligence Platform

An end-to-end Machine Learning application that predicts loan approval decisions using financial risk modeling and provides business intelligence through an interactive web dashboard.

---

## 📌 Problem Statement

Financial institutions must assess loan applications while minimizing default risk and bias. Manual decision-making can be inconsistent, slow, and prone to human bias.

This project builds a data-driven AI system to:

* Predict loan approval probability
* Quantify risk exposure
* Improve transparency through model explainability
* Analyze fairness across demographic groups

---

## 🧠 Solution Architecture

```
Data → Preprocessing → Model Training → Model Serialization → Streamlit App → Interactive Analytics
```

### Core Components

* Data Cleaning & Feature Engineering
* Model Training (Random Forest Classifier)
* Probability-Based Risk Scoring
* Explainable AI (Feature Importance)
* Fairness Evaluation
* Real-time Simulation Engine

---

## 🤖 Machine Learning Model

**Algorithm:** Random Forest Classifier
**Training Split:** 80% Training / 20% Testing
**Target Variable:** Loan_Status

### 📊 Features Used

* ApplicantIncome
* LoanAmount
* Credit_History

### ⚙️ Data Processing

* Missing value imputation (Mean strategy)
* Label encoding for target variable (Y → 1, N → 0)
* Feature selection for optimal performance

### 🎯 Model Capabilities

* Binary Classification (Approved / Rejected)
* Probability-Based Risk Score
* Confidence Score Calculation
* Feature Importance Extraction

---

## 🚀 Application Modules

### 1️⃣ Executive Dashboard

* Total Applications
* Approval Rate
* Loan Distribution
* Real-time Metrics

### 2️⃣ Prediction Engine

Input financial attributes and returns:

* Approval Decision
* Approval Probability (%)
* Confidence Score
* Risk Indicator

### 3️⃣ AI Insights Module

* Feature importance ranking
* Model transparency visualization

### 4️⃣ Fairness & Bias Analysis

* Gender-based approval comparison
* Detects potential bias patterns

### 5️⃣ Loan Scenario Simulator

* Modify applicant income & loan amount
* Observe real-time probability changes
* Business decision testing tool

### 6️⃣ Executive Summary Panel

* Business explanation
* Model overview
* Strategic value
## 📂 Dataset

The dataset used in this project contains applicant financial details such as income, loan amount, and credit history.

---

## 🏗 Tech Stack

| Category        | Technology    |
| --------------- | ------------- |
| Programming     | Python        |
| Data Processing | Pandas, NumPy |
| ML Framework    | Scikit-learn  |
| Algorithm       | Random Forest |
| Web Framework   | Streamlit     |
| Model Storage   | Pickle        |

---

## 📂 Project Structure

```
Bank-Loan-Approval-Analysis/
│
├── app.py                # Streamlit Web Application
├── train_model.py        # Model Training Pipeline
├── data.csv              # Dataset
├── model.pkl             # Trained ML Model
├── accuracy.pkl          # Stored Accuracy Score
├── cm.pkl                # Confusion Matrix
├── features.pkl          # Feature List
├── model_name.pkl        # Model Metadata
├── requirements.txt      # Project Dependencies
└── README.md             # Documentation
```

---

## ⚙️ Installation & Execution

### 1. Clone Repository

```
git clone https://github.com/your-username/Bank-Loan-Approval-Analysis.git
cd Bank-Loan-Approval-Analysis
```

### 2. Install Dependencies

```
pip install -r requirements.txt
```

### 3. Launch Application

```
streamlit run app.py
```

---

## 📈 Business Impact

* Reduces manual loan screening time
* Enables data-driven approval decisions
* Improves risk assessment accuracy
* Enhances transparency in AI-based systems
* Supports financial strategy planning

---

## 🔍 Key Learnings

* End-to-End ML Workflow
* Data Cleaning & Feature Selection
* Model Evaluation & Probability Scoring
* Building Interactive ML Applications
* Implementing Fairness Analysis
* Deployable AI Systems

---

## 🌍 Future Roadmap

* Add advanced models (XGBoost, Gradient Boosting)
* SHAP-based explainability
* REST API integration
* Cloud deployment (AWS / Streamlit Cloud)
* Model performance comparison dashboard
* Authentication & Role-based Access

---
## Project screenshot
<img width="1918" height="892" alt="image" src="https://github.com/user-attachments/assets/8a5526a6-ff15-413b-90f7-c0c126038da9" />



## 👨‍💻 Author

**Soni**
Data Science Enthusiast | Machine Learning Developer


