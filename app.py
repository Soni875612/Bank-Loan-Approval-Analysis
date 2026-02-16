import streamlit as st
import pandas as pd
import pickle
import numpy as np

st.set_page_config(page_title="AI Loan Intelligence", layout="wide")

# Load data
df = pd.read_csv("data.csv")
df['Loan_Status'] = df['Loan_Status'].map({'Y':1,'N':0})

# Load model
model = pickle.load(open("model.pkl","rb"))

st.sidebar.title("🏦 AI Loan Intelligence Platform")

page = st.sidebar.radio(
    "Navigation",
    ["Dashboard","Prediction","AI Insights","Fairness Analysis","Simulator","Executive Summary"]
)

st.sidebar.markdown("---")
st.sidebar.write("Model: Random Forest")

# ---------------- DASHBOARD ----------------
if page == "Dashboard":

    st.title("📊 Loan Analytics Dashboard")

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Applications", len(df))
    col2.metric("Approved Loans", len(df[df['Loan_Status']==1]))
    col3.metric("Approval Rate",
                str(round(len(df[df['Loan_Status']==1])/len(df)*100,2))+"%")

    st.subheader("Loan Status Distribution")
    st.bar_chart(df['Loan_Status'].value_counts())

# ---------------- PREDICTION ----------------
elif page == "Prediction":

    st.title("🤖 Loan Approval Prediction")

    income = st.slider("Applicant Income", 0, 10000, 5000)
    loan_amount = st.slider("Loan Amount", 0, 500, 100)
    credit = st.selectbox("Credit History", [1.0, 0.0])

    if st.button("Predict Loan Status"):

        input_data = np.array([[income, loan_amount, credit]])

        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[0][1]

        risk_score = round(probability*100,2)
        confidence = round(abs(probability-0.5)*200,2)

        if prediction[0] == 1:
            st.success("✅ Loan Approved")
        else:
            st.error("❌ Loan Rejected")

        st.info(f"Approval Probability: {risk_score}%")
        st.metric("Confidence Level", str(confidence)+"%")

# ---------------- AI INSIGHTS ----------------
elif page == "AI Insights":

    st.title("🧠 AI Model Insights")

    importances = model.feature_importances_
    feature_names = model.feature_names_in_

    importance_df = pd.DataFrame({
        "Feature": feature_names,
        "Importance": importances
    }).sort_values("Importance", ascending=False)

    st.dataframe(importance_df)
    st.bar_chart(importance_df.set_index("Feature"))

# ---------------- FAIRNESS ----------------
elif page == "Fairness Analysis":

    st.title("⚖️ AI Fairness Analysis")

    if "Gender" in df.columns:
        gender_approval = df.groupby("Gender")["Loan_Status"].mean()
        st.bar_chart(gender_approval)
    else:
        st.warning("Gender column not found in dataset.")

# ---------------- SIMULATOR ----------------
elif page == "Simulator":

    st.title("🎮 Loan Scenario Simulator")

    income = st.slider("Change Income", 0, 10000, 4000)
    loan = st.slider("Change Loan Amount", 0, 500, 150)
    credit = st.selectbox("Credit History", [1.0, 0.0])

    input_data = np.array([[income, loan, credit]])

    probability = model.predict_proba(input_data)[0][1]

    st.metric("Live Approval Chance", str(round(probability*100,2))+"%")

# ---------------- SUMMARY ----------------
elif page == "Executive Summary":

    st.title("📘 Project Executive Summary")

    st.write("""
    ### Problem
    Loan approval involves financial risk assessment.

    ### Solution
    AI-based Loan Approval Prediction using Machine Learning.

    ### Model Used
    Random Forest Classifier

    ### Features Used
    - Applicant Income
    - Loan Amount
    - Credit History

    ### Advanced Capabilities
    - Risk Score
    - Confidence Score
    - AI Feature Importance
    - Fairness Analysis
    - Scenario Simulation
    """)
