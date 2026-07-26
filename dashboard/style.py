# ==========================================================
# STYLE
# European Bank Customer Churn Prediction
# Developed By:
# Ajay Pratap Singh Hada
# ==========================================================

import streamlit as st

PRIMARY = "#0F4C81"
SECONDARY = "#2A9D8F"
SUCCESS = "#2E7D32"
WARNING = "#F9A825"
ERROR = "#C62828"
BACKGROUND = "#F7F9FC"
CARD = "#FFFFFF"
TEXT = "#1F2937"
TEXT_LIGHT = "#6B7280"
SIDEBAR = "#082B4A"
SIDEBAR_TEXT = "#FFFFFF"
BORDER = "#D8E0EA"

CSS = f"""
<style>
html, body, [class*="css"] {{
    background:{BACKGROUND};
    color:{TEXT};
    font-family:'Segoe UI',sans-serif;
}}
.block-container {{
    padding-top:1.2rem;
    padding-left:2rem;
    padding-right:2rem;
    max-width:1320px;
}}
[data-testid="stSidebar"] {{
    background:{SIDEBAR};
    border-right:1px solid rgba(255,255,255,.08);
}}
[data-testid="stSidebar"] * {{
    color:{SIDEBAR_TEXT} !important;
}}
[data-testid="stMetric"] {{
    background:#FFFFFF;
    border:1px solid {BORDER};
    border-radius:8px;
    padding:16px;
    box-shadow:0 2px 8px rgba(15,76,129,.08);
}}
[data-testid="stMetricLabel"] {{
    color:#374151 !important;
    font-size:15px !important;
    font-weight:600 !important;
}}
[data-testid="stMetricValue"] {{
    color:{PRIMARY} !important;
    font-size:30px !important;
    font-weight:700 !important;
}}
.stButton>button {{
    width:100%;
    background:{SECONDARY};
    color:white;
    border:none;
    border-radius:8px;
    padding:.75rem;
    font-weight:700;
}}
.stButton>button:hover {{
    background:{PRIMARY};
}}
.stDownloadButton>button {{
    width:100%;
    background:{SUCCESS};
    color:white;
    border:none;
    border-radius:8px;
}}
.stDownloadButton>button:hover {{
    background:#1B5E20;
}}
thead tr th {{
    background:{PRIMARY};
    color:white !important;
}}
tbody tr:nth-child(even) {{
    background:#F8FAFC;
}}
tbody tr:hover {{
    background:#E3F2FD;
}}
[data-testid="stFileUploader"] {{
    border:2px dashed {SECONDARY};
    border-radius:8px;
    padding:15px;
}}
::-webkit-scrollbar {{
    width:10px;
}}
::-webkit-scrollbar-thumb {{
    background:{SECONDARY};
    border-radius:10px;
}}
</style>
"""


def apply_style():
    st.markdown(CSS, unsafe_allow_html=True)


def banner(title, subtitle=""):
    st.markdown(
        f"""<div style="background:linear-gradient(135deg,{PRIMARY},{SECONDARY});padding:24px;border-radius:8px;margin-bottom:25px;box-shadow:0 3px 12px rgba(15,76,129,.16);">
<h1 style="color:white;margin:0;font-size:34px;font-weight:700;line-height:1.2;">{title}</h1>
<p style="color:#EAF4FF;margin:10px 0 0 0;font-size:16px;">{subtitle}</p>
</div>""",
        unsafe_allow_html=True,
    )


def section(title):
    st.markdown(
        f"""<div style="font-size:25px;font-weight:700;color:{PRIMARY};margin-top:25px;margin-bottom:18px;border-bottom:3px solid {SECONDARY};padding-bottom:8px;">{title}</div>""",
        unsafe_allow_html=True,
    )


def kpi_card(column, label, value, color="blue"):
    border = SECONDARY
    if color.lower() == "green":
        border = SUCCESS
    elif color.lower() == "red":
        border = ERROR
    elif color.lower() == "amber":
        border = WARNING

    column.markdown(
        f"""<div style="background:{CARD};border-left:6px solid {border};border-radius:8px;padding:20px;min-height:118px;box-shadow:0 2px 8px rgba(15,76,129,.08);">
<div style="color:{TEXT_LIGHT};font-size:13px;font-weight:700;text-transform:uppercase;margin-bottom:10px;">{label}</div>
<div style="color:{PRIMARY};font-size:30px;font-weight:700;line-height:1.15;">{value}</div>
</div>""",
        unsafe_allow_html=True,
    )


def metric_row(items):
    cols = st.columns(len(items))
    for col, item in zip(cols, items):
        kpi_card(col, item["label"], item["value"], item.get("color", "blue"))


def success_box(text):
    st.markdown(box(text, "#ECFDF5", SUCCESS), unsafe_allow_html=True)


def warning(text):
    st.markdown(box(text, "#FFF8E1", WARNING), unsafe_allow_html=True)


def error_box(text):
    st.markdown(box(text, "#FDECEC", ERROR), unsafe_allow_html=True)


def insight(text):
    st.markdown(box(text, "#E8F4FD", SECONDARY), unsafe_allow_html=True)


def info_box(text):
    st.markdown(box(text, "#EEF6FF", PRIMARY), unsafe_allow_html=True)


def box(text, background, border):
    return f"""<div style="background:{background};border-left:6px solid {border};padding:18px;border-radius:8px;color:{TEXT};margin-bottom:15px;box-shadow:0 2px 8px rgba(15,76,129,.06);">{text}</div>"""


def status_card(title, value, color="green"):
    border = SUCCESS
    if color == "red":
        border = ERROR
    elif color == "amber":
        border = WARNING
    elif color == "blue":
        border = SECONDARY

    st.markdown(
        f"""<div style="background:white;border-left:6px solid {border};border-radius:8px;padding:18px;margin-bottom:15px;box-shadow:0 2px 8px rgba(15,76,129,.08);">
<h4 style="margin:0;color:{PRIMARY};font-size:18px;">{title}</h4>
<p style="margin:10px 0 0 0;font-size:28px;font-weight:700;color:{TEXT};">{value}</p>
</div>""",
        unsafe_allow_html=True,
    )


def page_title(title, subtitle=""):
    st.markdown(
        f"""<div style="margin-bottom:25px;"><h1 style="color:{PRIMARY};font-size:34px;font-weight:700;margin-bottom:6px;">{title}</h1><p style="color:{TEXT_LIGHT};font-size:16px;margin-top:0;">{subtitle}</p></div>""",
        unsafe_allow_html=True,
    )


def divider():
    st.markdown(f"""<hr style="border:1px solid {BORDER};margin-top:25px;margin-bottom:25px;">""", unsafe_allow_html=True)


def space(lines=1):
    for _ in range(lines):
        st.write("")


def loading(text="Loading..."):
    return st.spinner(text)


def footer():
    divider()
    st.markdown(
        f"""<div style="text-align:center;color:{TEXT_LIGHT};padding:20px;font-size:14px;">
🏦 <b>European Bank Customer Churn Prediction System</b><br><br>
Developed by<br><b>Ajay Pratap Singh Hada</b><br>
MBA (Business Analytics)<br>
Prestige Institute of Management & Research, Gwalior<br><br>
<span style="font-size:12px;">Version 3.0 | © 2026 All Rights Reserved</span>
</div>""",
        unsafe_allow_html=True,
    )


PROJECT_INFO = {
    "Project": "European Bank Customer Churn Prediction",
    "Version": "3.0",
    "Developer": "Ajay Pratap Singh Hada",
    "Course": "MBA (Business Analytics)",
    "Institute": "Prestige Institute of Management & Research, Gwalior",
}


def application_info():
    return PROJECT_INFO
