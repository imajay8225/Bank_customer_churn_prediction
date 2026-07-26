# Bank Customer Churn Prediction — Streamlit App

**Developed by:** Ajay Pratap Singh Hada · MBA Business Analytics

---

## Project Structure

```
churn_app/
├── app.py                  ← Home page (entry point)
├── utils.py                ← Shared helpers: load_model, engineer_features, etc.
├── models/
│   ├── rf_model.pkl        ← Your trained Random Forest model
│   └── scaler.pkl          ← Your fitted StandardScaler
└── pages/
    ├── 1_Dashboard.py
    ├── 2_Single_Prediction.py
    ├── 3_Bulk_Prediction.py
    ├── 4_Model_Comparison.py
    └── 5_About.py
```

---

## Setup

### 1. Install dependencies

```bash
pip install streamlit pandas numpy matplotlib scikit-learn xgboost joblib
```

### 2. Add your model files

Copy your trained model and scaler into the `models/` folder:

```
churn_app/models/rf_model.pkl
churn_app/models/scaler.pkl
```

> If your files are elsewhere, update the `MODEL_PATH` and `SCALER_PATH`
> variables at the top of `utils.py`.

### 3. Run the app

```bash
cd churn_app
streamlit run app.py
```

---

## Key Improvements Over Original

| Area | Before | After |
|------|--------|-------|
| **Code duplication** | Model loaded in every page separately | `utils.py` — loaded once, cached |
| **Feature engineering** | Copy-pasted in 2 pages | Single `engineer_features()` function |
| **Hard-coded paths** | Windows absolute paths (`C:\Users\...`) | Relative paths that work anywhere |
| **Design** | Plain default Streamlit | Consistent blue/navy theme, metric cards |
| **Model comparison** | 5 separate bar charts | Side-by-side + radar chart |
| **Risk gauge** | `st.progress()` bar | Colour-coded HTML progress bar |
| **Bulk charts** | `import matplotlib` missing | Fixed + pie + bar charts working |
| **Error handling** | App crashes if model missing | Graceful error message |
| **Input form** | Basic number inputs | Sliders + radios for better UX |
