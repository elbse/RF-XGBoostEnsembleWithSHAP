import streamlit as st
from datetime import datetime

def render_sidebar():
    """Render the sidebar navigation"""
    with st.sidebar:
        # Logo and title
        st.markdown("""
        <div style="text-align: center; padding: 1rem 0;">
            <div style="width: 60px; height: 60px; margin: 0 auto; background: linear-gradient(135deg, #3B82F6, #8B5CF6); border-radius: 20px; display: flex; align-items: center; justify-content: center;">
                <span style="font-size: 2rem;">🛡️</span>
            </div>
            <h2 class="gradient-text" style="margin-top: 1rem;">Rubik</h2>
            <p style="color: #6B7280; font-size: 0.875rem;">Android Malware Detector</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Model badge
        st.markdown("""
        <div style="background: rgba(59, 130, 246, 0.15); border-radius: 12px; padding: 0.75rem; text-align: center; margin-bottom: 1rem; border: 1px solid rgba(59, 130, 246, 0.3);">
            <span style="color: #3B82F6; font-weight: 700; font-size: 0.9rem;">#RF-XGB-SHAP</span>
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation items
        pages = {
            "🛡️ Threat Scanner": "Threat Scanner",
            "📊 SHAP Explainability": "SHAP Explainability",
            "📈 Model Analytics": "Model Analytics",
            "📁 Dataset Insights": "Dataset Insights",
            "🔬 Research Comparison": "Research Comparison",
            "💡 Feature Intelligence": "Feature Intelligence"
        }
        
        for display, page_name in pages.items():
            if st.button(display, key=page_name, use_container_width=True):
                st.session_state.current_page = page_name
                st.rerun()
        
        st.markdown("---")
        
        # System status
        st.markdown(f"""
        <div class="glass-card" style="padding: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 1rem;">
                <div class="pulse" style="width: 8px; height: 8px; background: #10B981; border-radius: 50%; box-shadow: 0 0 10px #10B981;"></div>
                <span style="color: #10B981; font-size: 0.75rem; font-weight: 600;">SYSTEM ONLINE</span>
            </div>
            <div style="font-size: 0.75rem; color: #9CA3AF;">
                <div>Model: Ensemble RF+XGB</div>
                <div>Version: 2.1.0</div>
                <div>Last Update: {datetime.now().strftime("%Y-%m-%d")}</div>
            </div>
        </div>
        """, unsafe_allow_html=True)