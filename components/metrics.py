import streamlit as st

def render_metrics():
    """Render system metrics"""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Detection Rate", "98.7%", "+2.3%")
    with col2:
        st.metric("False Positive", "1.2%", "-0.5%", delta_color="inverse")
    with col3:
        st.metric("Active Threats", "1,247", "+124", delta_color="inverse")

def render_recent_scans():
    """Render recent scans list"""
    st.markdown("### 🕒 Recent Scans")
    
    recent_scans = [
        {"file": "com.example.app1.apk", "result": "✅ Safe", "score": "0.12"},
        {"file": "unknown_app.apk", "result": "⚠️ Suspicious", "score": "0.45"},
        {"file": "game_mod_v2.apk", "result": "❌ Malware", "score": "0.89"},
        {"file": "utility_tool.apk", "result": "✅ Safe", "score": "0.08"},
    ]
    
    for scan in recent_scans:
        if "Safe" in scan['result']:
            color = "#10B981"
            badge = "badge-safe"
        elif "Malware" in scan['result']:
            color = "#EF4444"
            badge = "badge-danger"
        else:
            color = "#F59E0B"
            badge = "badge-warning"
        
        st.markdown(f"""
        <div style="display: flex; justify-content: space-between; align-items: center; padding: 0.5rem 0; border-bottom: 1px solid rgba(59, 130, 246, 0.1);">
            <span style="font-size: 0.8rem;">{scan['file']}</span>
            <span class="{badge}" style="padding: 0.15rem 0.5rem; font-size: 0.7rem;">{scan['result']}</span>
            <code style="font-size: 0.7rem;">Score: {scan['score']}</code>
        </div>
        """, unsafe_allow_html=True)