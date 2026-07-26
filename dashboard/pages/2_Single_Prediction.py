# ==========================================================
# PAGE 2
# SINGLE CUSTOMER PREDICTION
# European Bank Customer Churn Prediction
#
# Developed By:
# Ajay Pratap Singh Hada
# ==========================================================

import streamlit as st
import pandas as pd

from style import (
    apply_style,
    banner,
    section,
    footer
)

from services.model_service import (
    predict_customer
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Single Prediction",

    page_icon="🎯",

    layout="wide"

)

apply_style()

# ==========================================================
# HEADER
# ==========================================================

banner(

    "🎯 Customer Churn Prediction",

    "Predict whether a customer is likely to leave the bank."

)

# ==========================================================
# CUSTOMER INFORMATION
# ==========================================================

section("📝 Customer Information")

col1, col2 = st.columns(2)
with col1:

    credit_score = st.number_input(
        "Credit Score",
        min_value=300,
        max_value=900,
        value=650
    )

    age = st.number_input(
        "Age",
        min_value=18,
        max_value=100,
        value=35
    )

    tenure = st.number_input(
        "Tenure (Years)",
        min_value=0,
        max_value=10,
        value=5
    )

    balance = st.number_input(
        "Account Balance",
        min_value=0.0,
        value=50000.0,
        step=1000.0
    )

    geography = st.selectbox(

        "Geography",

        [

            "France",

            "Germany",

            "Spain"

        ]

    )

with col2:

    products = st.selectbox(

        "Number of Products",

        [1, 2, 3, 4]

    )

    has_card = st.selectbox(

        "Has Credit Card",

        [

            1,

            0

        ],

        format_func=lambda x:
            "Yes" if x == 1 else "No"

    )

    active = st.selectbox(

        "Active Member",

        [

            1,

            0

        ],

        format_func=lambda x:
            "Yes" if x == 1 else "No"

    )

    salary = st.number_input(

        "Estimated Salary",

        min_value=0.0,

        value=50000.0,

        step=1000.0

    )

    gender = st.selectbox(

        "Gender",

        [

            "Male",

            "Female"

        ]

    )

# ==========================================================
# PREDICT BUTTON
# ==========================================================

st.divider()

predict = st.button(

    "🔍 Predict Customer Churn",

    use_container_width=True

)

# ==========================================================
# PART 2 STARTS BELOW
# ==========================================================

# ==========================================================
# PREDICTION
# ==========================================================

if predict:

    try:

        customer = {

            "CreditScore": credit_score,

            "Age": age,

            "Tenure": tenure,

            "Balance": balance,

            "NumOfProducts": products,

            "HasCrCard": has_card,

            "IsActiveMember": active,

            "EstimatedSalary": salary,

            "Geography": geography,

            "Gender": gender

        }

        result = predict_customer(customer)

        prediction = result["Prediction"]

        probability = result["Probability"]

        risk = result["Risk"]

        recommendation = result["Recommendation"]

        st.session_state["prediction_result"] = {

            "customer": customer,

            "prediction": prediction,

            "probability": probability,

            "risk": risk,

            "recommendation": recommendation

        }

    except Exception as e:

        st.error(f"Prediction Error: {e}")

# ==========================================================
# DISPLAY RESULT
# ==========================================================

if "prediction_result" in st.session_state:

    result = st.session_state["prediction_result"]

    prediction = result["prediction"]

    probability = result["probability"]

    risk = result["risk"]

    recommendation = result["recommendation"]

# ==========================================================
# PART 3 STARTS BELOW
# ==========================================================

# ==========================================================
# PREDICTION RESULT
# ==========================================================

if "prediction_result" in st.session_state:

    result = st.session_state["prediction_result"]

    prediction = result["prediction"]

    probability = result["probability"]

    risk = result["risk"]

    recommendation = result["recommendation"]

    section("📊 Prediction Results")

    col1, col2, col3 = st.columns(3)

    # ------------------------------------------------------
    # Prediction
    # ------------------------------------------------------

    with col1:

        if prediction == 1:

            st.error("🔴 Customer Likely to Churn")

        else:

            st.success("🟢 Customer Likely to Stay")

    # ------------------------------------------------------
    # Probability
    # ------------------------------------------------------

    with col2:

        st.metric(

            label="Churn Probability",

            value=f"{probability:.2f}%"

        )

    # ------------------------------------------------------
    # Risk
    # ------------------------------------------------------

    with col3:

        st.metric(

            label="Risk Level",

            value=risk

        )

# ==========================================================
# BUSINESS RECOMMENDATION
# ==========================================================

    section("💡 Business Recommendation")

    if prediction == 1:

        st.warning(recommendation)

    else:

        st.success(recommendation)

# ==========================================================
# CUSTOMER SUMMARY
# ==========================================================

    section("👤 Customer Summary")

    summary = pd.DataFrame({

        "Field":[

            "Credit Score",

            "Age",

            "Tenure",

            "Balance",

            "Products",

            "Credit Card",

            "Active Member",

            "Estimated Salary",

            "Geography",

            "Gender"

        ],

        "Value":[

    result["customer"]["CreditScore"],

    result["customer"]["Age"],

    result["customer"]["Tenure"],

    result["customer"]["Balance"],

    result["customer"]["NumOfProducts"],

    "Yes" if result["customer"]["HasCrCard"] else "No",

    "Yes" if result["customer"]["IsActiveMember"] else "No",

    result["customer"]["EstimatedSalary"],

    result["customer"]["Geography"],

    result["customer"]["Gender"]

]

    })

    st.dataframe(

        summary,

        hide_index=True,

        use_container_width=True

    )

# ==========================================================
# PART 4 STARTS BELOW
# ==========================================================

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

    report = pd.DataFrame({

        "Field":[

            "Prediction",

            "Probability (%)",

            "Risk Level",

            "Recommendation"

        ],

        "Value":[

            "Likely to Churn" if prediction == 1 else "Likely to Stay",

            probability,

            risk,

            recommendation

        ]

    })

    csv = report.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="📥 Download Prediction Report",

        data=csv,

        file_name="Single_Customer_Prediction.csv",

        mime="text/csv",

        use_container_width=True

    )

# ==========================================================
# EXECUTIVE SUMMARY
# ==========================================================

    section("📋 Executive Summary")

    if prediction == 1:

        st.error("""

### High Churn Risk

This customer is predicted to leave the bank.

Recommended actions:

✔ Contact the customer immediately

✔ Offer retention benefits

✔ Assign a relationship manager

✔ Recommend personalized banking products

✔ Monitor future engagement

""")

    else:

        st.success("""

### Low Churn Risk

This customer is likely to remain with the bank.

Recommended actions:

✔ Maintain regular engagement

✔ Promote premium banking services

✔ Offer cross-selling opportunities

✔ Continue loyalty rewards

✔ Monitor customer satisfaction

""")

# ==========================================================
# FOOTER
# ==========================================================

footer()