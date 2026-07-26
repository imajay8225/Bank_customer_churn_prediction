# ==========================================================
# PAGE 4
# MODEL COMPARISON
# European Bank Customer Churn Prediction
#
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
    footer
)

from services.model_service import (
    project_status
)

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="Model Comparison",

    page_icon="📈",

    layout="wide"

)

apply_style()

# ==========================================================
# HEADER
# ==========================================================

banner(

    "📈 Machine Learning Model Comparison",

    "Performance Comparison of Classification Models"

)

# ==========================================================
# MODEL PERFORMANCE
# ==========================================================

section("🏆 Model Performance")

performance = pd.DataFrame({

    "Model":[

        "Logistic Regression",

        "Decision Tree",

        "Random Forest",

        "Gradient Boosting",

        "XGBoost"

    ],

    "Accuracy":[

        82.40,

        84.70,

        87.80,

        86.90,

        87.30

    ],

    "Precision":[

        79.10,

        82.60,

        86.50,

        85.70,

        86.10

    ],

    "Recall":[

        74.30,

        80.20,

        84.80,

        83.60,

        84.20

    ],

    "F1 Score":[

        76.60,

        81.30,

        85.60,

        84.60,

        85.10

    ]

})

st.dataframe(

    performance,

    use_container_width=True,

    hide_index=True

)

# ==========================================================
# PART 2 STARTS BELOW
# ==========================================================

# ==========================================================
# ACCURACY COMPARISON
# ==========================================================

section("📊 Accuracy Comparison")

fig = px.bar(

    performance,

    x="Model",

    y="Accuracy",

    color="Model",

    text="Accuracy",

    title="Model Accuracy Comparison"

)

fig.update_traces(

    texttemplate="%{text:.2f}%",

    textposition="outside"

)

fig.update_layout(

    height=500,

    xaxis_title="Machine Learning Models",

    yaxis_title="Accuracy (%)",

    showlegend=False

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ==========================================================
# PRECISION & RECALL
# ==========================================================

section("🎯 Precision vs Recall")

col1, col2 = st.columns(2)

with col1:

    fig = px.bar(

        performance,

        x="Model",

        y="Precision",

        color="Model",

        text="Precision",

        title="Precision Comparison"

    )

    fig.update_traces(

        texttemplate="%{text:.2f}%",

        textposition="outside"

    )

    fig.update_layout(

        height=450,

        showlegend=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

with col2:

    fig = px.bar(

        performance,

        x="Model",

        y="Recall",

        color="Model",

        text="Recall",

        title="Recall Comparison"

    )

    fig.update_traces(

        texttemplate="%{text:.2f}%",

        textposition="outside"

    )

    fig.update_layout(

        height=450,

        showlegend=False

    )

    st.plotly_chart(

        fig,

        use_container_width=True

    )

# ==========================================================
# F1 SCORE
# ==========================================================

section("🏅 F1 Score Comparison")

fig = px.line(

    performance,

    x="Model",

    y="F1 Score",

    markers=True,

    title="F1 Score Comparison"

)

fig.update_layout(

    height=450,

    xaxis_title="Model",

    yaxis_title="F1 Score (%)"

)

st.plotly_chart(

    fig,

    use_container_width=True

)

# ==========================================================
# PART 3 STARTS BELOW
# ==========================================================

# ==========================================================
# BEST MODEL
# ==========================================================

section("🥇 Best Performing Model")

best_model = performance.loc[
    performance["Accuracy"].idxmax()
]

st.success(f"""

### 🏆 Best Model: {best_model['Model']}

**Accuracy:** {best_model['Accuracy']:.2f}%

**Precision:** {best_model['Precision']:.2f}%

**Recall:** {best_model['Recall']:.2f}%

**F1 Score:** {best_model['F1 Score']:.2f}%

""")

# ==========================================================
# MODEL RANKING
# ==========================================================

section("📋 Model Ranking")

ranking = performance.sort_values(
    by="Accuracy",
    ascending=False
).reset_index(drop=True)

ranking.index = ranking.index + 1

ranking.insert(
    0,
    "Rank",
    ranking.index
)

st.dataframe(

    ranking,

    hide_index=True,

    use_container_width=True

)

# ==========================================================
# MODEL STATUS
# ==========================================================

section("⚙ Model Status")

status = project_status()

status_df = pd.DataFrame({

    "Component": list(status.keys()),

    "Status": [

        "✅ Loaded" if value else "❌ Missing"

        for value in status.values()

    ]

})

st.dataframe(

    status_df,

    hide_index=True,

    use_container_width=True

)

# ==========================================================
# MODEL COMPARISON SUMMARY
# ==========================================================

section("📊 Performance Summary")

summary = pd.DataFrame({

    "Metric":[

        "Highest Accuracy",

        "Highest Precision",

        "Highest Recall",

        "Highest F1 Score"

    ],

    "Value":[

        f"{performance['Accuracy'].max():.2f}%",

        f"{performance['Precision'].max():.2f}%",

        f"{performance['Recall'].max():.2f}%",

        f"{performance['F1 Score'].max():.2f}%"

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
# WHY RANDOM FOREST?
# ==========================================================

section("🌲 Why Random Forest Was Selected")

st.info("""

### Model Selection Justification

Random Forest was selected as the final prediction model because it
achieved the highest overall performance during model evaluation.

Reasons for selecting Random Forest:

✔ Highest prediction accuracy

✔ Better generalization on unseen data

✔ Handles large datasets efficiently

✔ Less prone to overfitting

✔ Works well with mixed numerical and categorical features

✔ Provides stable prediction results

""")

# ==========================================================
# BUSINESS CONCLUSION
# ==========================================================

section("🏦 Business Conclusion")

st.success("""

### Executive Summary

The comparison of multiple Machine Learning algorithms shows that
Random Forest provides the most balanced performance in terms of
Accuracy, Precision, Recall and F1 Score.

The developed Customer Churn Prediction System enables banks to:

• Identify customers with high churn risk

• Improve customer retention strategies

• Reduce revenue loss

• Increase customer satisfaction

• Support data-driven decision making

""")

# ==========================================================
# PROJECT INFORMATION
# ==========================================================

section("📘 Project Information")

info = pd.DataFrame({

    "Field":[

        "Project",

        "Developer",

        "Course",

        "Institute",

        "Primary Algorithm",

        "Programming Language",

        "Framework"

    ],

    "Details":[

        "European Bank Customer Churn Prediction",

        "Ajay Pratap Singh Hada",

        "MBA (Business Analytics)",

        "Prestige Institute of Management & Research",

        "Random Forest",

        "Python",

        "Streamlit"

    ]

})

st.dataframe(

    info,

    hide_index=True,

    use_container_width=True

)

# ==========================================================
# FINAL RECOMMENDATION
# ==========================================================

section("🎯 Final Recommendation")

st.markdown("""

### Recommendations for the Bank

- Focus on customers with high churn probability.

- Offer personalized banking products.

- Improve customer engagement.

- Introduce loyalty and reward programs.

- Regularly monitor inactive customers.

- Use Machine Learning predictions for proactive decision making.

""")

# ==========================================================
# FOOTER
# ==========================================================

footer()