import streamlit as st
import hashlib
from pathlib import Path

def load_css():
    """Load global CSS file"""
    css_file = Path("assets/style.css")
    if css_file.exists():
        with open(css_file, 'r', encoding='utf-8') as f:
            st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
    else:
        # Fallback CSS if file doesn't exist
        st.markdown("""
        <style>
        .glass-card {
            background: rgba(18, 25, 45, 0.7);
            backdrop-filter: blur(10px);
            border-radius: 20px;
            border: 1px solid rgba(59, 130, 246, 0.2);
            padding: 1.5rem;
            margin: 1rem 0;
        }
        .gradient-text {
            background: linear-gradient(135deg, #3B82F6, #10B981, #8B5CF6);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        </style>
        """, unsafe_allow_html=True)

def format_bytes(size):
    """Format bytes to human readable"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if size < 1024.0:
            return f"{size:.2f} {unit}"
        size /= 1024.0
    return f"{size:.2f} GB"

def calculate_hash(content):
    """Calculate SHA256 hash of file content"""
    return hashlib.sha256(content).hexdigest()

def get_shap_values():
    """Return SHAP values for features"""
    return {
        'SEND SMS': 0.42,
        'READ CONTACTS': 0.31,
        'getDeviceId': 0.28,
        'sendTextMessage': 0.19,
        'INTERNET': 0.178,
        'target_sdk': -0.12,
        'CAMERA': 0.09,
        'RECORD_AUDIO': 0.05
    }

def get_feature_importance():
    """Return feature importance data"""
    return {
        'SEND_SMS': 0.92,
        'READ_CONTACTS': 0.88,
        'INTERNET': 0.75,
        'CAMERA': 0.68,
        'RECORD_AUDIO': 0.62,
        'ACCESS_FINE_LOCATION': 0.58,
        'READ_PHONE_STATE': 0.45,
        'WRITE_EXTERNAL_STORAGE': 0.42
    }