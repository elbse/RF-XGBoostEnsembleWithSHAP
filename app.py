import streamlit as st
from components.sidebar import render_sidebar
from utils.helpers import load_css
from pages import (
    show_threat_scanner,
    show_shap_explainability,
    show_model_analytics,
    show_dataset_insights,
    show_research_comparison,
    show_feature_intelligence
)

# Page configuration
st.set_page_config(
    page_title="Rubik | Android Malware Detector",
    page_icon="🛡️",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Load custom CSS
load_css()

# Initialize session state
if 'current_page' not in st.session_state:
    st.session_state.current_page = "Threat Scanner"
if 'scan_result' not in st.session_state:
    st.session_state.scan_result = None

# Render sidebar
render_sidebar()

# Page routing
current_page = st.session_state.current_page

if current_page == "Threat Scanner":
    show_threat_scanner()
elif current_page == "SHAP Explainability":
    show_shap_explainability()
elif current_page == "Model Analytics":
    show_model_analytics()
elif current_page == "Dataset Insights":
    show_dataset_insights()
elif current_page == "Research Comparison":
    show_research_comparison()
elif current_page == "Feature Intelligence":
    show_feature_intelligence()

# Footer
st.markdown("""
<hr style="border-color: rgba(59, 130, 246, 0.2); margin: 2rem 0 1rem 0;">
<div style="text-align: center; color: #6B7280; font-size: 0.75rem; padding: 1rem;">
    <p>Rubik Android Malware Detector | Powered by RF-XGBoost Ensemble with SHAP Explainability</p>
    <p>© 2024 - Advanced Threat Detection System</p>
</div>
""", unsafe_allow_html=True)