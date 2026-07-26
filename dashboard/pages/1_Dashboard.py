# ==========================================================
# PAGE 1
# EUROPEAN BANK DASHBOARD
# Developed By:
# Ajay Pratap Singh Hada
# ==========================================================

import streamlit as st
import pandas as pd
import plotly.express as px

from style import (
    apply_style,
    banner,
    section,
    insight,
    success_box,
    warning,
    divider,
    footer
)

from utils import load_dataset

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="Dashboard",
    page_icon="🏦",
    layout="wide"
)

apply_style()

# ==========================================================
# LOAD DATA
# ==========================================================

df = load_dataset()

if df is None or df.empty:
    st.error("Dataset could not be loaded.")
    st.stop()

# ==========================================================
# HEADER
# ==========================================================

banner(
    "🏦 European Bank Customer Churn Analytics",
    "AI Powered Business Intelligence Dashboard"
)

left, right = st.columns([3,1])

with left:

    st.markdown("""

## 📊 Executive Dashboard

This dashboard provides an interactive overview of customer behaviour,
financial performance, customer churn and business insights using
Machine Learning and Business Analytics.

""")

with right:

    st.info("""

### Dashboard

**Version:** 3.0

**Developer**

Ajay Pratap Singh Hada

MBA (Business Analytics)

Prestige Institute of Management & Research

""")

divider()

# ==========================================================
# KPI CALCULATIONS
# ==========================================================

total_customers = len(df)

churn_customers = int(df["Exited"].sum())

retained_customers = total_customers - churn_customers

churn_rate = (churn_customers / total_customers) * 100

retention_rate = 100 - churn_rate

active_members = int(df["IsActiveMember"].sum())

inactive_members = total_customers - active_members

credit_card_holders = int(df["HasCrCard"].sum())

average_age = df["Age"].mean()

average_credit = df["CreditScore"].mean()

average_balance = df["Balance"].mean()

average_salary = df["EstimatedSalary"].mean()

total_balance = df["Balance"].sum()

# ==========================================================
# EXECUTIVE KPI
# ==========================================================

section("📈 Executive Key Performance Indicators")

c1, c2, c3 = st.columns(3)

with c1:

    st.metric(
        "👥 Total Customers",
        f"{total_customers:,}"
    )

    st.metric(
        "🟢 Active Members",
        f"{active_members:,}"
    )

with c2:

    st.metric(
        "🔴 Churn Rate",
        f"{churn_rate:.2f}%"
    )

    st.metric(
        "💳 Credit Card Holders",
        f"{credit_card_holders:,}"
    )

with c3:

    st.metric(
        "💰 Average Balance",
        f"₹ {average_balance:,.0f}"
    )

    st.metric(
        "💵 Average Salary",
        f"₹ {average_salary:,.0f}"
    )

divider()

# ==========================================================
# EXECUTIVE OVERVIEW
# ==========================================================

section("📊 Executive Overview")

left,right = st.columns([2,1])

with left:

    churn_df = pd.DataFrame({

        "Status":[
            "Retained",
            "Churn"
        ],

        "Customers":[
            retained_customers,
            churn_customers
        ]

    })

    fig = px.pie(

        churn_df,

        names="Status",

        values="Customers",

        hole=0.60,

        color="Status",

        color_discrete_map={

            "Retained":"green",

            "Churn":"red"

        }

    )

    fig.update_layout(height=420)

    st.plotly_chart(
        fig,
        use_container_width=True
    )

with right:

    st.metric(
        "💰 Total Bank Balance",
        f"₹ {total_balance:,.0f}"
    )

    st.metric(
        "🟢 Retention Rate",
        f"{retention_rate:.2f}%"
    )

    st.metric(
        "👥 Retained Customers",
        f"{retained_customers:,}"
    )

    st.metric(
        "🔴 Churn Customers",
        f"{churn_customers:,}"
    )

divider()

# ==========================================================
# PART 2 STARTS BELOW
# ==========================================================

# ==========================================================
# CUSTOMER ANALYTICS
# ==========================================================

section("📊 Customer Analytics")

col1, col2 = st.columns(2)

# ----------------------------------------------------------
# GEOGRAPHY ANALYSIS
# ----------------------------------------------------------

with col1:

    geography = (
        df["Geography"]
        .value_counts()
        .reset_index()
    )

    geography.columns = [
        "Geography",
        "Customers"
    ]

    fig = px.bar(
        geography,
        x="Geography",
        y="Customers",
        color="Geography",
        text="Customers",
        title="Customers by Geography"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        height=420,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------------
# GENDER DISTRIBUTION
# ----------------------------------------------------------

with col2:

    gender = (
        df["Gender"]
        .value_counts()
        .reset_index()
    )

    gender.columns = [
        "Gender",
        "Customers"
    ]

    fig = px.pie(
        gender,
        names="Gender",
        values="Customers",
        hole=0.50,
        title="Gender Distribution"
    )

    fig.update_layout(
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# CUSTOMER PROFILE
# ==========================================================

section("👥 Customer Profile")

left, right = st.columns(2)

# ----------------------------------------------------------
# AGE DISTRIBUTION
# ----------------------------------------------------------

with left:

    fig = px.histogram(
        df,
        x="Age",
        nbins=25,
        color="Exited",
        title="Age Distribution by Churn"
    )

    fig.update_layout(
        height=420
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------------
# PRODUCTS
# ----------------------------------------------------------

with right:

    products = (
        df["NumOfProducts"]
        .value_counts()
        .sort_index()
        .reset_index()
    )

    products.columns = [
        "Products",
        "Customers"
    ]

    fig = px.bar(
        products,
        x="Products",
        y="Customers",
        color="Products",
        text="Customers",
        title="Products per Customer"
    )

    fig.update_traces(
        textposition="outside"
    )

    fig.update_layout(
        height=420,
        showlegend=False
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ==========================================================
# FINANCIAL ANALYTICS
# ==========================================================

section("💰 Financial Analytics")

left, right = st.columns(2)

# ----------------------------------------------------------
# BALANCE VS SALARY
# ----------------------------------------------------------

with left:

    fig = px.scatter(
        df,
        x="Balance",
        y="EstimatedSalary",
        color="Exited",
        hover_data=[
            "Age",
            "CreditScore",
            "NumOfProducts"
        ],
        title="Balance vs Estimated Salary"
    )

    fig.update_layout(
        height=430
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

# ----------------------------------------------------------
# CREDIT SCORE
# ----------------------------------------------------------

with right:

    fig = px.box(
        df,
        y="CreditScore",
        color="Exited",
        title="Credit Score Distribution"
    )

    fig.update_layout(
        height=430
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )

divider()

# ==========================================================
# PART 3 STARTS BELOW
# ==========================================================

# ==========================================================
# EXECUTIVE INSIGHTS
# ==========================================================

section("🧠 Executive Insights")

left, right = st.columns(2)

with left:

    highest_geo = df["Geography"].value_counts().idxmax()
    highest_products = int(df["NumOfProducts"].mode()[0])

    insight(f"""
### 📈 Business Insights

✔ Total Customers : **{total_customers:,}**

✔ Churn Rate : **{churn_rate:.2f}%**

✔ Retention Rate : **{retention_rate:.2f}%**

✔ Highest Customer Base : **{highest_geo}**

✔ Average Customer Age : **{average_age:.1f} Years**

✔ Average Credit Score : **{average_credit:.1f}**

✔ Most Preferred Products : **{highest_products}**

""")

with right:

    st.warning(f"""

### ⚠ Customer Risk Summary

🔴 Churn Customers : **{churn_customers:,}**

🟢 Retained Customers : **{retained_customers:,}**

👥 Active Members : **{active_members:,}**

🚫 Inactive Members : **{inactive_members:,}**

💳 Credit Card Holders : **{credit_card_holders:,}**

💰 Total Bank Balance :

**₹ {total_balance:,.0f}**

""")

divider()

# ==========================================================
# BUSINESS RECOMMENDATIONS
# ==========================================================

section("🏦 Business Recommendations")

if churn_rate >= 20:

    st.warning("""

### High Customer Churn Detected

Recommended Actions

✔ Launch customer retention campaigns

✔ Reward loyal customers

✔ Improve customer engagement

✔ Offer personalized banking services

✔ Monitor inactive customers

✔ Assign relationship managers

""")

else:

    success_box("""

### Customer Churn is Healthy

Recommended Actions

✔ Continue customer engagement

✔ Increase product adoption

✔ Improve digital banking

✔ Promote premium banking services

✔ Reward loyal customers

""")

divider()

# ==========================================================
# EXECUTIVE STATISTICS
# ==========================================================

section("📋 Executive Statistics")

statistics = pd.DataFrame({

    "Metric":[

        "Total Customers",

        "Retained Customers",

        "Churn Customers",

        "Retention Rate",

        "Average Age",

        "Average Credit Score",

        "Average Balance",

        "Average Salary"

    ],

    "Value":[

        f"{total_customers:,}",

        f"{retained_customers:,}",

        f"{churn_customers:,}",

        f"{retention_rate:.2f}%",

        f"{average_age:.1f} Years",

        f"{average_credit:.1f}",

        f"₹ {average_balance:,.2f}",

        f"₹ {average_salary:,.2f}"

    ]

})

st.dataframe(

    statistics,

    hide_index=True,

    use_container_width=True

)

divider()

# ==========================================================
# PART 4 STARTS BELOW
# ==========================================================

# ==========================================================
# CEO DECISION PANEL
# ==========================================================

section("🏆 Executive Decision Panel")

left, right = st.columns(2)

with left:

    success_box("""

### Key Business Findings

✔ Random Forest achieved the best prediction performance.

✔ Active customers have significantly lower churn.

✔ Customers with multiple products show higher loyalty.

✔ Customer behaviour varies across different geographies.

✔ Business Analytics enables proactive churn prevention.

""")

with right:

    insight("""

### Strategic Recommendations

• Focus on high-risk customers.

• Improve loyalty programs.

• Increase customer engagement.

• Promote premium banking products.

• Monitor inactive members regularly.

• Use ML predictions for retention campaigns.

""")

divider()

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

section("📘 Project Information")

project = pd.DataFrame({

    "Field":[

        "Project",

        "Developer",

        "Course",

        "Specialization",

        "Institute",

        "Machine Learning",

        "Framework"

    ],

    "Details":[

        "European Bank Customer Churn Prediction",

        "Ajay Pratap Singh Hada",

        "MBA",

        "Business Analytics",

        "Prestige Institute of Management & Research, Gwalior",

        "Random Forest Classifier",

        "Streamlit"

    ]

})

st.dataframe(

    project,

    hide_index=True,

    use_container_width=True

)

divider()

# ==========================================================
# DASHBOARD SUMMARY
# ==========================================================

section("📊 Dashboard Summary")

col1, col2 = st.columns(2)

with col1:

    st.success(f"""

### Project Highlights

✔ Customers Analysed : **{total_customers:,}**

✔ Customer Churn Rate : **{churn_rate:.2f}%**

✔ Retention Rate : **{retention_rate:.2f}%**

✔ Average Credit Score : **{average_credit:.1f}**

✔ Average Balance : **₹ {average_balance:,.0f}**

✔ Average Salary : **₹ {average_salary:,.0f}**

""")

with col2:

    st.info("""

### Technologies Used

🐍 Python

📊 Pandas

📈 Plotly

🤖 Scikit-Learn

⚡ XGBoost

🌐 Streamlit

💾 Joblib

""")

divider()



# ==========================================================
# FOOTER
# ==========================================================

footer()