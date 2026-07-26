# ==========================================================
# PAGE 3
# BULK CUSTOMER PREDICTION
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

from utils import (
    validate_dataset
)

from services.model_service import (
    predict_bulk
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Bulk Prediction",

    page_icon="📂",

    layout="wide"

)

apply_style()

# ==========================================================
# HEADER
# ==========================================================

banner(

    "📂 Bulk Customer Prediction",

    "Upload a CSV file to predict customer churn for multiple customers."

)

# ==========================================================
# FILE UPLOAD
# ==========================================================

section("📤 Upload Dataset")

uploaded_file = st.file_uploader(

    "Choose CSV File",

    type=["csv"]

)

# ==========================================================
# PART 2 STARTS BELOW
# ==========================================================

# ==========================================================
# LOAD DATASET
# ==========================================================

if uploaded_file is not None:

    try:

        df = pd.read_csv(uploaded_file)

        valid, message = validate_dataset(df)

        if not valid:

            st.error(message)

            st.stop()

        st.success(message)

    except Exception as e:

        st.error(f"Error reading file: {e}")

        st.stop()

# ==========================================================
# DATASET SUMMARY
# ==========================================================

    section("📊 Dataset Summary")

    col1, col2, col3 = st.columns(3)

    col1.metric(
        "Total Customers",
        len(df)
    )

    col2.metric(
        "Total Columns",
        len(df.columns)
    )

    col3.metric(
        "Missing Values",
        int(df.isnull().sum().sum())
    )

# ==========================================================
# DATA PREVIEW
# ==========================================================

    section("👀 Dataset Preview")

    st.dataframe(

        df.head(10),

        use_container_width=True,

        hide_index=True

    )

# ==========================================================
# PREDICT BUTTON
# ==========================================================

    st.divider()

    predict = st.button(

        "🚀 Predict All Customers",

        use_container_width=True

    )

# ==========================================================
# PART 3 STARTS BELOW
# ==========================================================

# ==========================================================
# BULK PREDICTION
# ==========================================================

    if predict:

        try:

            with st.spinner("Predicting customer churn..."):

                result_df = predict_bulk(df)

            st.session_state["bulk_result"] = result_df

            st.success("✅ Prediction completed successfully!")

        except Exception as e:

            st.error(f"Prediction Error: {e}")

# ==========================================================
# DISPLAY RESULTS
# ==========================================================

if "bulk_result" in st.session_state:

    result_df = st.session_state["bulk_result"]

    section("📊 Prediction Summary")

    total = len(result_df)

    churn = int(result_df["Prediction"].sum())

    retained = total - churn

    churn_rate = (churn / total) * 100

    col1, col2, col3, col4 = st.columns(4)

    col1.metric(
        "Total Customers",
        total
    )

    col2.metric(
        "Likely to Churn",
        churn
    )

    col3.metric(
        "Likely to Stay",
        retained
    )

    col4.metric(
        "Churn Rate",
        f"{churn_rate:.2f}%"
    )

# ==========================================================
# RISK DISTRIBUTION
# ==========================================================

    section("⚠ Risk Distribution")

    risk_summary = (

        result_df["Risk Level"]

        .value_counts()

        .reset_index()

    )

    risk_summary.columns = [

        "Risk Level",

        "Customers"

    ]

    st.dataframe(

        risk_summary,

        hide_index=True,

        use_container_width=True

    )

# ==========================================================
# RESULT PREVIEW
# ==========================================================

    section("📋 Prediction Results")

    st.dataframe(

        result_df,

        use_container_width=True,

        hide_index=True

    )

# ==========================================================
# PART 4 STARTS BELOW
# ==========================================================

# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

    csv = result_df.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="📥 Download Prediction Report",

        data=csv,

        file_name="Bulk_Prediction_Report.csv",

        mime="text/csv",

        use_container_width=True

    )

# ==========================================================
# EXECUTIVE INSIGHTS
# ==========================================================

    section("💡 Executive Insights")

    high_risk = len(
        result_df[
            result_df["Risk Level"].str.contains("High")
        ]
    )

    medium_risk = len(
        result_df[
            result_df["Risk Level"].str.contains("Medium")
        ]
    )

    low_risk = len(
        result_df[
            result_df["Risk Level"].str.contains("Low")
        ]
    )

    st.markdown(f"""

### Prediction Summary

- **Total Customers:** {total}
- **Likely to Churn:** {churn}
- **Likely to Stay:** {retained}
- **Overall Churn Rate:** {churn_rate:.2f}%

### Risk Distribution

- 🔴 High Risk Customers: **{high_risk}**
- 🟡 Medium Risk Customers: **{medium_risk}**
- 🟢 Low Risk Customers: **{low_risk}**

""")

# ==========================================================
# BUSINESS RECOMMENDATIONS
# ==========================================================

    section("🏦 Business Recommendations")

    if churn_rate >= 20:

        st.warning("""

### Recommended Actions

✔ Contact high-risk customers immediately

✔ Offer personalized retention plans

✔ Launch customer loyalty campaigns

✔ Improve customer engagement

✔ Assign relationship managers

✔ Review inactive customer accounts

""")

    else:

        st.success("""

### Recommended Actions

✔ Continue customer engagement

✔ Promote premium banking products

✔ Reward loyal customers

✔ Expand cross-selling opportunities

✔ Maintain regular customer satisfaction surveys

""")

# ==========================================================
# FOOTER
# ==========================================================

footer()