import streamlit as st
from utils import get_feature_importance

def show_feature_intelligence():
    """Feature Intelligence Page"""
    
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
            <div style="width: 12px; height: 12px; background: #10B981; border-radius: 50%; box-shadow: 0 0 10px #10B981;"></div>
            <span style="color: #6B7280; font-weight: 500;">Feature Analysis</span>
        </div>
        <h1 style="font-size: 2.5rem; margin-top: 0.5rem;">
            <span class="gradient-text">Feature Intelligence</span>
        </h1>
        <p style="color: #9CA3AF;">Understanding which Android permissions and features indicate malicious behavior</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 🔑 Permission Risk Analysis")
        
        feature_importance = get_feature_importance()
        
        for permission, score in sorted(feature_importance.items(), key=lambda x: x[1], reverse=True):
            if score >= 0.8:
                risk = "Critical"
                color = "#EF4444"
            elif score >= 0.6:
                risk = "High"
                color = "#F59E0B"
            else:
                risk = "Medium"
                color = "#10B981"
            
            width_pct = score * 100
            
            st.markdown(f"""
            <div style="margin-bottom: 1rem;">
                <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                    <div>
                        <span style="font-weight: 500;">{permission}</span>
                        <span style="margin-left: 0.5rem; font-size: 0.7rem; color: {color};">{risk}</span>
                    </div>
                    <span>{score:.0%}</span>
                </div>
                <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 30px; overflow: hidden;">
                    <div style="width: {width_pct}%; background: linear-gradient(90deg, #3B82F6, {color}); height: 100%; border-radius: 10px; display: flex; align-items: center; padding-left: 10px; color: white; font-size: 0.8rem;">
                        {score:.0%}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Risk Distribution")
        
        st.markdown("""
        <div style="margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                <span style="color: #EF4444;">Critical Risk</span>
                <span>2 permissions</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 30px; overflow: hidden;">
                <div style="width: 25%; background: #EF4444; height: 100%; border-radius: 10px; display: flex; align-items: center; padding-left: 10px; color: white;">
                    2
                </div>
            </div>
        </div>
        <div style="margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                <span style="color: #F59E0B;">High Risk</span>
                <span>2 permissions</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 30px; overflow: hidden;">
                <div style="width: 25%; background: #F59E0B; height: 100%; border-radius: 10px; display: flex; align-items: center; padding-left: 10px; color: white;">
                    2
                </div>
            </div>
        </div>
        <div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                <span style="color: #10B981;">Medium Risk</span>
                <span>4 permissions</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 30px; overflow: hidden;">
                <div style="width: 50%; background: #10B981; height: 100%; border-radius: 10px; display: flex; align-items: center; padding-left: 10px; color: white;">
                    4
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Suspicious permission patterns
    st.markdown('<div class="glass-card" style="margin-top: 1rem;">', unsafe_allow_html=True)
    st.markdown("### 🚨 Suspicious Permission Combinations")
    
    patterns = [
        {"pattern": "SEND_SMS + INTERNET", "risk": "Critical", "description": "Can send premium SMS and exfiltrate data"},
        {"pattern": "READ_CONTACTS + SEND_SMS", "risk": "Critical", "description": "Can access contacts and send messages"},
        {"pattern": "CAMERA + INTERNET", "risk": "High", "description": "Can capture and upload images"},
    ]
    
    for pattern in patterns:
        risk_color = "#EF4444" if pattern['risk'] == "Critical" else "#F59E0B"
        st.markdown(f"""
        <div style="background: rgba(59, 130, 246, 0.05); border-radius: 8px; padding: 0.75rem; margin-bottom: 0.5rem; border-left: 3px solid {risk_color};">
            <div style="display: flex; justify-content: space-between;">
                <span style="font-weight: 600;">⚠️ {pattern['pattern']}</span>
                <span style="color: {risk_color};">{pattern['risk']}</span>
            </div>
            <div style="font-size: 0.75rem; color: #9CA3AF; margin-top: 0.25rem;">{pattern['description']}</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)
    
    # Recommendations
    st.markdown('<div class="glass-card" style="margin-top: 1rem;">', unsafe_allow_html=True)
    st.markdown("### 💡 Security Recommendations")
    
    st.markdown("""
    <div style="background: rgba(16, 185, 129, 0.1); border-radius: 12px; padding: 1rem;">
        <div style="display: flex; align-items: center; gap: 0.5rem; margin-bottom: 0.5rem;">
            <span style="font-size: 1.25rem;">🛡️</span>
            <span style="font-weight: 600;">Best Practices for Users</span>
        </div>
        <ul style="margin: 0.5rem 0 0 1rem; color: #D1D5DB; font-size: 0.875rem;">
            <li>Review app permissions before installation</li>
            <li>Avoid apps requesting SMS and Contacts permissions unnecessarily</li>
            <li>Download apps only from official Google Play Store</li>
            <li>Use Rubik scanner for suspicious APK files</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)