# ==========================================================
# UTILS
# European Bank Customer Churn Prediction
#
# Developed By:
# Ajay Pratap Singh Hada
# ==========================================================

from pathlib import Path
import pandas as pd
import streamlit as st

# ==========================================================
# PROJECT PATHS
# ==========================================================

UTILS_DIR = Path(__file__).resolve().parent

DASHBOARD_DIR = UTILS_DIR

PROJECT_DIR = DASHBOARD_DIR.parent

DATA_DIR = PROJECT_DIR / "data"

MODEL_DIR = PROJECT_DIR / "models"

OUTPUT_DIR = DASHBOARD_DIR / "outputs"

IMAGE_DIR = DASHBOARD_DIR / "images"

OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

IMAGE_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# DATASET
# ==========================================================

DATASET_PATH = DATA_DIR / "European_Bank.csv"

# ==========================================================
# LOAD DATASET
# ==========================================================

@st.cache_data
def load_dataset():

    if not DATASET_PATH.exists():

        raise FileNotFoundError(

            f"Dataset not found:\n{DATASET_PATH}"

        )

    return pd.read_csv(DATASET_PATH)

# ==========================================================
# LOAD CSV
# ==========================================================

def load_csv(uploaded_file):

    try:

        df = pd.read_csv(uploaded_file)

        return df

    except Exception as e:

        st.error(e)

        return None

# ==========================================================
# IMAGE PATH
# ==========================================================

def get_image(name):

    file = IMAGE_DIR / name

    if file.exists():

        return str(file)

    return None

# ==========================================================
# PART 2 STARTS BELOW
# ==========================================================
# ==========================================================
# REQUIRED COLUMNS
# ==========================================================

REQUIRED_COLUMNS = [

    "CreditScore",

    "Age",

    "Tenure",

    "Balance",

    "NumOfProducts",

    "HasCrCard",

    "IsActiveMember",

    "EstimatedSalary",

    "Geography",

    "Gender"

]

# ==========================================================
# VALIDATE DATASET
# ==========================================================

def validate_dataset(df):
    """
    Validate uploaded dataset.
    """

    if df is None:

        return False, "Dataset is empty."

    if df.empty:

        return False, "Dataset contains no records."

    missing_columns = [

        column

        for column in REQUIRED_COLUMNS

        if column not in df.columns

    ]

    if len(missing_columns) > 0:

        return (

            False,

            f"Missing Columns: {', '.join(missing_columns)}"

        )

    numeric_columns_to_check = [

        "CreditScore",

        "Age",

        "Tenure",

        "Balance",

        "NumOfProducts",

        "HasCrCard",

        "IsActiveMember",

        "EstimatedSalary"

    ]

    invalid_numeric = [

        column

        for column in numeric_columns_to_check

        if pd.to_numeric(df[column], errors="coerce").isna().any()

    ]

    if invalid_numeric:

        return (

            False,

            f"Invalid numeric values found in: {', '.join(invalid_numeric)}"

        )

    valid_geographies = {"france", "germany", "spain"}

    invalid_geography = ~df["Geography"].astype(str).str.lower().isin(valid_geographies)

    if invalid_geography.any():

        return False, "Geography must be France, Germany, or Spain."

    valid_genders = {"male", "female"}

    invalid_gender = ~df["Gender"].astype(str).str.lower().isin(valid_genders)

    if invalid_gender.any():

        return False, "Gender must be Male or Female."

    return True, "Dataset validation successful."


# ==========================================================
# MISSING VALUES
# ==========================================================

def missing_values(df):
    """
    Return missing values summary.
    """

    return df.isnull().sum().reset_index().rename(

        columns={

            "index": "Column",

            0: "Missing Values"

        }

    )


# ==========================================================
# DATA SUMMARY
# ==========================================================

def dataset_summary(df):
    """
    Return dataset summary.
    """

    return {

        "Rows": len(df),

        "Columns": len(df.columns),

        "Missing Values": int(df.isnull().sum().sum()),

        "Duplicate Rows": int(df.duplicated().sum())

    }


# ==========================================================
# NUMERIC COLUMNS
# ==========================================================

def numeric_columns(df):

    return df.select_dtypes(

        include=["int64", "float64"]

    ).columns.tolist()


# ==========================================================
# CATEGORICAL COLUMNS
# ==========================================================

def categorical_columns(df):

    return df.select_dtypes(

        include=["object", "category"]

    ).columns.tolist()


# ==========================================================
# SAVE CSV
# ==========================================================

def save_csv(df, filename):

    filepath = OUTPUT_DIR / filename

    df.to_csv(

        filepath,

        index=False

    )

    return filepath


# ==========================================================
# FILE EXISTS
# ==========================================================

def file_exists(filepath):

    return Path(filepath).exists()


# ==========================================================
# PART 3 STARTS BELOW
# ==========================================================
# ==========================================================
# FORMAT HELPERS
# ==========================================================

def format_currency(value):
    """Format a number as currency."""
    try:
        return f"₹ {float(value):,.2f}"
    except Exception:
        return "₹ 0.00"


def format_percentage(value):
    """Format a number as percentage."""
    try:
        return f"{float(value):.2f}%"
    except Exception:
        return "0.00%"


def format_number(value):
    """Format integer with commas."""
    try:
        return f"{int(value):,}"
    except Exception:
        return "0"


# ==========================================================
# STREAMLIT MESSAGE HELPERS
# ==========================================================

def success(message):
    st.success(message)


def info(message):
    st.info(message)


def warning(message):
    st.warning(message)


def error(message):
    st.error(message)


# ==========================================================
# SESSION STATE
# ==========================================================

def initialize_session():

    defaults = {

        "prediction_done": False,

        "bulk_prediction_done": False,

        "uploaded_data": None,

        "prediction_result": None

    }

    for key, value in defaults.items():

        if key not in st.session_state:

            st.session_state[key] = value


# ==========================================================
# DOWNLOAD REPORT
# ==========================================================

def download_csv(df, filename):

    csv = df.to_csv(index=False).encode("utf-8")

    st.download_button(

        label="📥 Download Report",

        data=csv,

        file_name=filename,

        mime="text/csv",

        use_container_width=True

    )


# ==========================================================
# PROJECT DETAILS
# ==========================================================

PROJECT = {

    "Name": "European Bank Customer Churn Prediction",

    "Developer": "Ajay Pratap Singh Hada",

    "Course": "MBA (Business Analytics)",

    "Institute": "Prestige Institute of Management & Research",

    "Framework": "Streamlit",

    "Language": "Python",

    "Machine Learning": "Random Forest"

}


# ==========================================================
# APPLICATION INFORMATION
# ==========================================================

def application_information():

    return PROJECT


# ==========================================================
# PAGE TITLE
# ==========================================================

def page_title(title, subtitle=""):

    st.title(title)

    if subtitle:

        st.caption(subtitle)


# ==========================================================
# FOOTER
# ==========================================================

def footer():

    st.markdown("---")

    st.markdown(

        """
<div style="text-align:center; color:gray; font-size:13px;">

European Bank Customer Churn Prediction

Developed by **Ajay Pratap Singh Hada**

MBA (Business Analytics)

Prestige Institute of Management & Research

</div>

""",

        unsafe_allow_html=True

    )


# ==========================================================
# VERSION
# ==========================================================

VERSION = "2.0"

# ==========================================================
# END OF FILE
# ==========================================================