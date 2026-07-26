# ==========================================================
# EUROPEAN BANK
# BANK CUSTOMER CHURN PREDICTION SYSTEM
#
# Developed By:
# Ajay Pratap Singh Hada
# MBA (Business Analytics)
#
# Version : 2.0
# ==========================================================

import streamlit as st
import pandas as pd
from pathlib import Path

from style import (
    apply_style,
    banner,
    section,
    insight,
    success_box,
    warning,
    kpi_card,
    footer
)

# ==========================================================
# PAGE CONFIGURATION
# ==========================================================

st.set_page_config(
    page_title="European Bank Customer Churn Prediction",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

apply_style()

# ==========================================================
# PROJECT PATH
# ==========================================================

BASE_DIR = Path(__file__).resolve().parent

IMAGE_DIR = BASE_DIR / "images"

# ==========================================================
# SIDEBAR
# ==========================================================

with st.sidebar:

    st.markdown("# 🏦 European Bank")

    st.markdown("### Customer Analytics")

    st.markdown("---")

    st.success("Welcome to the Customer Churn Prediction Dashboard")

    st.markdown("## 📌 Navigation")

    st.info("""
Use the sidebar to access:

• Dashboard

• Single Prediction

• Bulk Prediction

• Model Comparison

• About
""")

    st.markdown("---")

    st.markdown("## 📊 Project")

    st.write("Predictive Modelling")

    st.write("Customer Risk Scoring")

    st.write("Business Analytics")

    st.markdown("---")

    st.markdown("## 👨‍🎓 Developer")

    st.write("Ajay Pratap Singh Hada")

    st.write("MBA (Business Analytics)")

    st.write("Prestige Institute of Management & Research")

# ==========================================================
# HEADER
# ==========================================================

banner(
    "🏦 European Bank Customer Churn Prediction System",
    "Machine Learning Based Customer Risk Analysis"
)

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

section("📖 Project Overview")

st.write("""
The objective of this project is to identify customers who are
likely to leave the bank by using Machine Learning algorithms.

The prediction model helps management identify high-risk
customers and take proactive retention actions before churn
actually occurs.
""")

# ==========================================================
# KPI CARDS
# ==========================================================

section("📊 Project Statistics")

c1, c2, c3, c4 = st.columns(4)

kpi_card(
    c1,
    "Customers",
    "10,000",
    "green"
)

kpi_card(
    c2,
    "Features",
    "16",
    ""
)

kpi_card(
    c3,
    "ML Models",
    "5",
    ""
)

kpi_card(
    c4,
    "Best Accuracy",
    "88%",
    "green"
)

# ==========================================================
# APPLICATION MODULES
# ==========================================================

section("🚀 Dashboard Modules")

modules = pd.DataFrame({

    "Module":[

        "📊 Dashboard",

        "👤 Single Prediction",

        "📂 Bulk Prediction",

        "📈 Model Comparison",

        "ℹ️ About"

    ],

    "Purpose":[

        "Dataset Analysis & KPIs",

        "Predict one customer",

        "Predict multiple customers",

        "Compare Machine Learning models",

        "Project Information"

    ]

})

st.dataframe(
    modules,
    use_container_width=True,
    hide_index=True
)

# ==========================================================
# MACHINE LEARNING MODELS
# ==========================================================

section("🤖 Machine Learning Models")

m1,m2,m3,m4,m5 = st.columns(5)

kpi_card(m1,"Logistic Regression","81%","")
kpi_card(m2,"Decision Tree","84%","")
kpi_card(m3,"Random Forest","87%","green")
kpi_card(m4,"Gradient Boosting","86%","")
kpi_card(m5,"XGBoost","88%","green")

# ==========================================================
# PART 2 STARTS BELOW
# ==========================================================

# ==========================================================
# PROJECT WORKFLOW
# ==========================================================

section("⚙️ Project Workflow")

st.code("""
                Raw Banking Dataset
                        │
                        ▼
              Data Cleaning & Validation
                        │
                        ▼
             Exploratory Data Analysis (EDA)
                        │
                        ▼
              Feature Engineering
                        │
                        ▼
            Data Preprocessing & Scaling
                        │
                        ▼
           Machine Learning Model Training
                        │
                        ▼
              Model Performance Evaluation
                        │
                        ▼
             Customer Churn Prediction
                        │
                        ▼
            Business Risk Classification
                        │
                        ▼
      Interactive Streamlit Dashboard
""")

# ==========================================================
# BUSINESS OBJECTIVES
# ==========================================================

section("🎯 Business Objectives")

col1, col2 = st.columns(2)

with col1:

    success_box("""
    ✔ Predict customer churn accurately

    ✔ Improve customer retention

    ✔ Reduce revenue loss

    ✔ Support business decision making

    ✔ Identify high-risk customers
    """)

with col2:

    success_box("""
    ✔ Improve customer loyalty

    ✔ Generate customer risk score

    ✔ Help marketing campaigns

    ✔ Increase profitability

    ✔ Data-driven management
    """)

# ==========================================================
# BUSINESS BENEFITS
# ==========================================================

section("💼 Business Benefits")

b1,b2,b3 = st.columns(3)

kpi_card(
    b1,
    "Retention",
    "Improve",
    "green"
)

kpi_card(
    b2,
    "Risk Analysis",
    "Real-Time",
    ""
)

kpi_card(
    b3,
    "Decision Making",
    "AI Driven",
    ""
)

insight("""

Banks lose millions of dollars every year because customers leave.

This Machine Learning system predicts customer churn before it
actually happens so the bank can contact valuable customers,
offer retention plans, and improve long-term profitability.

""")

# ==========================================================
# WHY MACHINE LEARNING
# ==========================================================

section("🤖 Why Machine Learning?")

st.write("""

Traditional business rules cannot identify complex customer
behavior patterns.

Machine Learning learns hidden relationships between customer
attributes and churn behavior, allowing the bank to make
accurate predictions automatically.

""")

# ==========================================================
# DATASET INFORMATION
# ==========================================================

section("📂 Dataset Summary")

d1,d2,d3,d4 = st.columns(4)

d1.metric("Customers","10000")

d2.metric("Original Features","14")

d3.metric("Engineered Features","16")

d4.metric("Target","Exited")

# ==========================================================
# APPLICATION FEATURES
# ==========================================================

section("🚀 Application Features")

features = [

"✔ Executive Dashboard",

"✔ Single Customer Prediction",

"✔ Bulk CSV Prediction",

"✔ Machine Learning Comparison",

"✔ Customer Risk Score",

"✔ Probability Prediction",

"✔ CSV Report Download",

"✔ Business Recommendations",

"✔ Interactive Charts",

"✔ Professional UI"

]

for item in features:

    st.write(item)

# ==========================================================
# FUTURE SCOPE
# ==========================================================

section("🔮 Future Scope")

warning("""

Future enhancements may include:

• Real-time API Prediction

• CRM Integration

• Live SQL Database

• Cloud Deployment

• Deep Learning Models

• SHAP Explainability

• Power BI Integration

• Customer Lifetime Value Prediction

""")

# ==========================================================
# DEVELOPER
# ==========================================================

section("👨‍💻 Developer")

st.info("""

Name

Ajay Pratap Singh Hada

------------------------------------

Course

MBA (Business Analytics)

------------------------------------

Institute

Prestige Institute of Management & Research

------------------------------------

Project

European Bank Customer Churn Prediction

------------------------------------

Technology

Python

Streamlit

Scikit-Learn

XGBoost

Random Forest

Pandas

NumPy

""")

# ==========================================================
# THANK YOU
# ==========================================================

st.markdown("<br>", unsafe_allow_html=True)

success_box("""

🎉 Thank you for using the

European Bank Customer Churn Prediction System.

Use the navigation menu on the left to explore all
dashboard modules.

""")

# ==========================================================
# FOOTER
# ==========================================================

footer()