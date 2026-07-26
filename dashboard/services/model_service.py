# ==========================================================
# MODEL SERVICE
# European Bank Customer Churn Prediction System
#
# Developed By:
# Ajay Pratap Singh Hada
# ==========================================================

import pandas as pd
import numpy as np
import joblib

from pathlib import Path

# ==========================================================
# PROJECT PATHS
# ==========================================================

# Current file:
# dashboard/services/model_service.py

SERVICE_DIR = Path(__file__).resolve().parent

DASHBOARD_DIR = SERVICE_DIR.parent

PROJECT_DIR = DASHBOARD_DIR.parent

MODEL_DIR = PROJECT_DIR / "models"

DATA_DIR = PROJECT_DIR / "data"

OUTPUT_DIR = DASHBOARD_DIR / "outputs"

IMAGE_DIR = DASHBOARD_DIR / "images"

# Create outputs folder if it doesn't exist
OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

# ==========================================================
# MODEL FILES
# ==========================================================

RF_MODEL_PATH = MODEL_DIR / "rf_model.pkl"

LR_MODEL_PATH = MODEL_DIR / "lr_model.pkl"

DT_MODEL_PATH = MODEL_DIR / "dt_model.pkl"

GB_MODEL_PATH = MODEL_DIR / "gb_model.pkl"

XGB_MODEL_PATH = MODEL_DIR / "xgb_model.pkl"

SCALER_PATH = MODEL_DIR / "scaler.pkl"

# ==========================================================
# FEATURE ORDER
# (Must match training)
# ==========================================================

MODEL_FEATURES = [

    "CreditScore",

    "Age",

    "Tenure",

    "Balance",

    "NumOfProducts",

    "HasCrCard",

    "IsActiveMember",

    "EstimatedSalary",

    "Geography_Germany",

    "Geography_Spain",

    "Gender_Male",

    "BalanceSalaryRatio",

    "ProductDensity",

    "EngagementProduct",

    "AgeTenure",

    "BalancePerProduct"

]

# ==========================================================
# LOAD MODEL
# ==========================================================

class ModelService:

    def __init__(self):

        self.rf_model = None

        self.lr_model = None

        self.dt_model = None

        self.gb_model = None

        self.xgb_model = None

        self.scaler = None

        self.load_errors = {}

    # ------------------------------------------------------

    def _load_artifact(self, label, path):

        try:

            artifact = joblib.load(path)

            print(f"{label} loaded")

            return artifact

        except Exception as e:

            self.load_errors[label] = str(e)

            print(f"{label}: {e}")

            return None

    def load_models(self):

        self.load_errors = {}

        self.rf_model = self._load_artifact("Random Forest", RF_MODEL_PATH)

        self.lr_model = self._load_artifact("Logistic Regression", LR_MODEL_PATH)

        self.dt_model = self._load_artifact("Decision Tree", DT_MODEL_PATH)

        self.gb_model = self._load_artifact("Gradient Boosting", GB_MODEL_PATH)

        self.xgb_model = self._load_artifact("XGBoost", XGB_MODEL_PATH)

        self.scaler = self._load_artifact("StandardScaler", SCALER_PATH)

# ==========================================================
# CREATE OBJECT
# ==========================================================

model_service = ModelService()

model_service.load_models()

# ==========================================================
# PART 2 STARTS BELOW
# ==========================================================

# ==========================================================
# FEATURE ENGINEERING
# ==========================================================

def create_features(customer):
    """
    Convert raw customer data into model features
    expected by the trained Machine Learning model.
    """

    credit_score = float(customer["CreditScore"])
    age = float(customer["Age"])
    tenure = float(customer["Tenure"])
    balance = float(customer["Balance"])
    products = float(customer["NumOfProducts"])
    has_card = int(customer["HasCrCard"])
    active = int(customer["IsActiveMember"])
    salary = float(customer["EstimatedSalary"])

    geography = str(customer["Geography"]).strip().lower()
    gender = str(customer["Gender"]).strip().lower()

    # ------------------------------------------------------
    # One-Hot Encoding
    # ------------------------------------------------------

    germany = 1 if geography == "germany" else 0
    spain = 1 if geography == "spain" else 0
    male = 1 if gender == "male" else 0

    # ------------------------------------------------------
    # Feature Engineering
    # (Matches the training pipeline)
    # ------------------------------------------------------

    balance_salary_ratio = balance / (salary + 1)

    product_density = products / (tenure + 1)

    engagement_product = active * products

    age_tenure = age * tenure

    balance_per_product = balance / (products + 1)

    data = pd.DataFrame([{

        "CreditScore": credit_score,

        "Age": age,

        "Tenure": tenure,

        "Balance": balance,

        "NumOfProducts": products,

        "HasCrCard": has_card,

        "IsActiveMember": active,

        "EstimatedSalary": salary,

        "Geography_Germany": germany,

        "Geography_Spain": spain,

        "Gender_Male": male,

        "BalanceSalaryRatio": balance_salary_ratio,

        "ProductDensity": product_density,

        "EngagementProduct": engagement_product,

        "AgeTenure": age_tenure,

        "BalancePerProduct": balance_per_product

    }])

    return data[MODEL_FEATURES]


   

# ==========================================================
# SCALE FEATURES
# ==========================================================

def scale_features(feature_df):
    """
    Scale engineered features using the trained StandardScaler.
    """

    if model_service.scaler is None:
        raise ValueError(
            "StandardScaler could not be loaded. Check models/scaler.pkl."
        )

    scaled = model_service.scaler.transform(feature_df)

    scaled_df = pd.DataFrame(
        scaled,
        columns=MODEL_FEATURES
    )

    return scaled_df

# ==========================================================
# PREPARE CUSTOMER
# ==========================================================

def prepare_customer(customer):
    """
    Complete preprocessing pipeline.

    Raw Customer
            ↓
    Feature Engineering
            ↓
    Scaling
            ↓
    Ready for Prediction
    """

    feature_df = create_features(customer)

    scaled_df = scale_features(feature_df)

    return scaled_df

# ==========================================================
# PART 3 STARTS BELOW
# ==========================================================

# ==========================================================
# PREDICT CUSTOMER
# ==========================================================

def predict_customer(customer):
    """
    Predict customer churn.
    """

    if model_service.rf_model is None:
        raise ValueError(
            "Random Forest model is not loaded. Check models/rf_model.pkl."
        )

    processed = prepare_customer(customer)

    prediction = int(
        model_service.rf_model.predict(processed)[0]
    )

    probability = float(
        model_service.rf_model.predict_proba(processed)[0][1]
    )

    probability = round(probability * 100, 2)

    return {

        "Prediction": prediction,

        "Probability": probability,

        "Risk": risk_level(probability),

        "Recommendation":
            business_recommendation(probability)

    }

# ==========================================================
# RISK LEVEL
# ==========================================================

def risk_level(probability):

    if probability < 30:

        return "Low"

    elif probability < 70:

        return "Medium"

    else:

        return "High"


# ==========================================================
# BUSINESS RECOMMENDATION
# ==========================================================

def business_recommendation(probability):

    if probability < 30:

        return (
            "Customer has a low churn risk. "
            "Maintain regular engagement and "
            "explore cross-selling opportunities."
        )

    elif probability < 70:

        return (
            "Customer has a medium churn risk. "
            "Offer personalized products, "
            "loyalty rewards, and monitor activity."
        )

    else:

        return (
            "Customer has a high churn risk. "
            "Assign a relationship manager, "
            "contact the customer immediately, "
            "and provide retention offers."
        )


# ==========================================================
# MODEL INFORMATION
# ==========================================================

def model_information():

    return {

        "Model": "Random Forest",

        "Algorithm": "Classification",

        "Features": len(MODEL_FEATURES),

        "Scaler": "StandardScaler",

        "Target": "Customer Churn"

    }


# ==========================================================
# TEST MODEL STATUS
# ==========================================================

def check_model():

    return {

        "RandomForest": model_service.rf_model is not None,

        "Scaler": model_service.scaler is not None,

        "FeatureCount": len(MODEL_FEATURES)

    }


# ==========================================================
# PART 4 STARTS BELOW
# ==========================================================

# ==========================================================
# BULK PREDICTION
# ==========================================================

def predict_bulk(df):
    """
    Predict churn for an uploaded raw customer dataset.
    """

    results = []

    for _, row in df.iterrows():

        customer = row.to_dict()

        result = predict_customer(customer)

        results.append(result)

    output = df.copy()

    output["Prediction"] = [

        r["Prediction"]

        for r in results

    ]

    output["Probability (%)"] = [

        r["Probability"]

        for r in results

    ]

    output["Risk Level"] = [

        r["Risk"]

        for r in results

    ]

    output["Recommendation"] = [

        r["Recommendation"]

        for r in results

    ]

    return output


# ==========================================================
# SAVE REPORT
# ==========================================================

def save_prediction_report(df,
                           filename="Prediction_Report.csv"):
    """
    Save prediction report.
    """

    filepath = OUTPUT_DIR / filename

    df.to_csv(

        filepath,

        index=False

    )

    return filepath


# ==========================================================
# FEATURE NAMES
# ==========================================================

def get_feature_names():

    return MODEL_FEATURES.copy()


# ==========================================================
# AVAILABLE MODELS
# ==========================================================

def available_models():

    models = {

        "Random Forest":

            model_service.rf_model,

        "Logistic Regression":

            model_service.lr_model,

        "Decision Tree":

            model_service.dt_model,

        "Gradient Boosting":

            model_service.gb_model,

        "XGBoost":

            model_service.xgb_model

    }

    return {

        name:model

        for name,model in models.items()

        if model is not None

    }


# ==========================================================
# PROJECT STATUS
# ==========================================================

def project_status():

    return {

        "Random Forest":

            model_service.rf_model is not None,

        "Logistic Regression":

            model_service.lr_model is not None,

        "Decision Tree":

            model_service.dt_model is not None,

        "Gradient Boosting":

            model_service.gb_model is not None,

        "XGBoost":

            model_service.xgb_model is not None,

        "Scaler":

            model_service.scaler is not None,

        "Output Folder":

            OUTPUT_DIR.exists(),

        "Images Folder":

            IMAGE_DIR.exists(),

        "Data Folder":

            DATA_DIR.exists()

    }


# ==========================================================
# MODEL INFORMATION
# ==========================================================

PROJECT_INFO = {

    "Project":

        "European Bank Customer Churn Prediction",

    "Developer":

        "Ajay Pratap Singh Hada",

    "Course":

        "MBA (Business Analytics)",

    "Institute":

        "Prestige Institute of Management & Research",

    "Framework":

        "Streamlit",

    "Language":

        "Python",

    "Algorithm":

        "Random Forest"

}


# ==========================================================
# VERSION
# ==========================================================

VERSION = "3.0"

AUTHOR = "Ajay Pratap Singh Hada"

# ==========================================================
# END OF FILE
# ==========================================================
