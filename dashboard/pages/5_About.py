# ==========================================================
# PAGE 5
# ABOUT PROJECT
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

# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(

    page_title="About",

    page_icon="📘",

    layout="wide"

)

apply_style()

# ==========================================================
# HEADER
# ==========================================================

banner(

    "📘 About the Project",

    "European Bank Customer Churn Prediction System"

)

# ==========================================================
# PROJECT OVERVIEW
# ==========================================================

section("📖 Project Overview")

st.markdown("""

The **European Bank Customer Churn Prediction System**
is a Machine Learning-based application developed to
predict whether a customer is likely to leave the bank.

The application helps banks identify high-risk customers,
improve retention strategies, and make better business
decisions using data analytics.

""")

# ==========================================================
# PROJECT OBJECTIVES
# ==========================================================

section("🎯 Project Objectives")

objectives = pd.DataFrame({

    "Objectives":[

        "Predict customer churn",

        "Reduce customer attrition",

        "Support business decisions",

        "Improve customer retention",

        "Increase profitability",

        "Provide interactive analytics"

    ]

})

st.dataframe(

    objectives,

    hide_index=True,

    use_container_width=True

)

# ==========================================================
# PART 2 STARTS BELOW
# ==========================================================

# ==========================================================
# TECHNOLOGIES USED
# ==========================================================

section("🛠 Technologies Used")

technology = pd.DataFrame({

    "Technology":[

        "Python",

        "Pandas",

        "NumPy",

        "Scikit-Learn",

        "XGBoost",

        "Plotly",

        "Streamlit",

        "Joblib"

    ],

    "Purpose":[

        "Programming Language",

        "Data Analysis",

        "Numerical Computing",

        "Machine Learning",

        "Boosting Algorithm",

        "Interactive Visualization",

        "Web Dashboard",

        "Model Serialization"

    ]

})

st.dataframe(

    technology,

    hide_index=True,

    use_container_width=True

)

# ==========================================================
# MACHINE LEARNING MODELS
# ==========================================================

section("🤖 Machine Learning Models")

models = pd.DataFrame({

    "Model":[

        "Logistic Regression",

        "Decision Tree",

        "Random Forest",

        "Gradient Boosting",

        "XGBoost"

    ],

    "Purpose":[

        "Baseline Classification",

        "Tree-based Classification",

        "Final Prediction Model",

        "Ensemble Learning",

        "Advanced Boosting"

    ]

})

st.dataframe(

    models,

    hide_index=True,

    use_container_width=True

)

# ==========================================================
# PROJECT MODULES
# ==========================================================

section("📂 Project Modules")

modules = pd.DataFrame({

    "Module":[

        "Dashboard",

        "Single Prediction",

        "Bulk Prediction",

        "Model Comparison",

        "About"

    ],

    "Description":[

        "Business analytics dashboard",

        "Predict one customer",

        "Predict multiple customers",

        "Compare ML models",

        "Project documentation"

    ]

})

st.dataframe(

    modules,

    hide_index=True,

    use_container_width=True

)

# ==========================================================
# PROJECT FEATURES
# ==========================================================

section("⭐ Key Features")

st.markdown("""

### Features Included

- 📊 Interactive Business Dashboard

- 🎯 Single Customer Churn Prediction

- 📂 Bulk Customer Prediction

- 📈 Machine Learning Model Comparison

- 📥 Download Prediction Reports

- ⚡ Fast Prediction Engine

- 📊 Interactive Charts

- 🏦 Business Recommendations

- 🎨 Professional Streamlit Interface

""")

# ==========================================================
# PART 3 STARTS BELOW
# ==========================================================

# ==========================================================
# DEVELOPER INFORMATION
# ==========================================================

section("👨‍💻 Developer Information")

developer = pd.DataFrame({

    "Field":[

        "Developer",

        "Course",

        "Specialization",

        "Institute",

        "Project",

        "Programming Language",

        "Framework"

    ],

    "Details":[

        "Ajay Pratap Singh Hada",

        "MBA",

        "Business Analytics",

        "Prestige Institute of Management & Research, Gwalior",

        "European Bank Customer Churn Prediction",

        "Python",

        "Streamlit"

    ]

})

st.dataframe(

    developer,

    hide_index=True,

    use_container_width=True

)

# ==========================================================
# FUTURE SCOPE
# ==========================================================

section("🚀 Future Scope")

st.info("""

### Future Enhancements

✔ Live Bank Database Integration

✔ Real-time Customer Churn Prediction

✔ Email & SMS Alert System

✔ Customer Segmentation Dashboard

✔ AI-based Customer Recommendation System

✔ Cloud Deployment (AWS / Azure)

✔ Power BI Integration

✔ Mobile Application Support

""")

# ==========================================================
# BUSINESS IMPACT
# ==========================================================

section("🏦 Business Impact")

st.success("""

### Expected Benefits

• Improve customer retention

• Reduce customer churn

• Increase customer satisfaction

• Improve business decision making

• Increase bank profitability

• Support strategic planning

• Enable proactive customer engagement

""")

# ==========================================================
# ACKNOWLEDGEMENT
# ==========================================================

section("🙏 Acknowledgement")

st.markdown("""

This project was developed as part of the **MBA (Business Analytics)** program.

Special thanks to the faculty members of **Prestige Institute of Management & Research, Gwalior** for their guidance and support throughout the project.

""")

# ==========================================================
# PROJECT VERSION
# ==========================================================

section("📌 Project Version")

version = pd.DataFrame({

    "Information":[

        "Project Version",

        "Application",

        "Machine Learning",

        "Dashboard",

        "Status"

    ],

    "Details":[

        "Version 3.0",

        "Streamlit",

        "Random Forest Classifier",

        "Interactive Business Intelligence",

        "Completed"

    ]

})

st.dataframe(

    version,

    hide_index=True,

    use_container_width=True

)


# ==========================================================
# FOOTER
# ==========================================================

footer()