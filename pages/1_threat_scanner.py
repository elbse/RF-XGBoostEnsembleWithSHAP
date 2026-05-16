import streamlit as st
import time
from datetime import datetime
from utils import get_prediction, format_bytes, calculate_hash

def show_threat_scanner():
    """Threat Scanner Page"""
    
    # Header
    st.markdown("""
    <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 2rem;">
        <div>
            <div style="display: flex; align-items: center; gap: 0.75rem;">
                <div style="width: 12px; height: 12px; background: #3B82F6; border-radius: 50%; box-shadow: 0 0 10px #3B82F6;"></div>
                <span style="color: #6B7280; font-weight: 500;">Threat Analysis System</span>
            </div>
            <h1 style="font-size: 2.5rem; margin-top: 0.5rem;">
                <span class="gradient-text">Threat Scanner</span>
            </h1>
            <p style="color: #9CA3AF;">Upload APK files for real-time malware detection using RF-XGBoost ensemble</p>
        </div>
        <div class="badge-safe">
            <span class="pulse" style="display: inline-block; width: 8px; height: 8px; background: #10B981; border-radius: 50%; margin-right: 6px;"></span>
            Active
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1], gap="large")
    
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📱 Upload APK File")
        st.caption("Supported format: .apk files only")
        
        uploaded_file = st.file_uploader(
            "Choose an APK file to scan",
            type=['apk'],
            label_visibility="collapsed"
        )
        
        if uploaded_file:
            file_size = len(uploaded_file.getvalue())
            st.info(f"""
            **File Details:**
            - Name: `{uploaded_file.name}`
            - Size: `{format_bytes(file_size)}`
            - Type: APK Package
            """)
            
            if st.button("🔍 Start Security Scan", type="primary", use_container_width=True):
                with st.spinner("Performing deep scan..."):
                    # Simulate scanning phases
                    progress_bar = st.progress(0)
                    
                    phases = [
                        "Extracting APK metadata...",
                        "Analyzing permissions...",
                        "Checking API calls...",
                        "Running ML inference...",
                        "Generating report..."
                    ]
                    
                    for i, phase in enumerate(phases):
                        status = st.status(phase, expanded=False)
                        time.sleep(0.5)
                        status.update(label=f"✓ {phase}", state="complete")
                        progress_bar.progress((i + 1) * 20)
                    
                    # Get prediction
                    file_content = uploaded_file.getvalue()
                    file_hash = calculate_hash(file_content)
                    result = get_prediction(file_hash)
                    
                    st.session_state.scan_result = {
                        'threat_score': result['threat_score'],
                        'is_malware': result['is_malware'],
                        'confidence': result['confidence'],
                        'file_name': uploaded_file.name,
                        'file_hash': file_hash[:16],
                        'timestamp': datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                        'suspicious_features': result['suspicious_features']
                    }
                    st.rerun()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📊 System Status")
        
        # Metrics
        from components import render_metrics
        render_metrics()
        
        st.markdown("---")
        
        # Recent scans
        from components import render_recent_scans
        render_recent_scans()
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Display scan results
    if st.session_state.get('scan_result'):
        st.markdown("---")
        st.markdown("### 🔍 Scan Results")
        
        result = st.session_state.scan_result
        
        col_r1, col_r2 = st.columns([1, 1])
        
        with col_r1:
            from components import create_gauge
            fig = create_gauge(result['threat_score'], "Threat Level", result['is_malware'])
            st.plotly_chart(fig, use_container_width=True)
        
        with col_r2:
            if result['is_malware']:
                st.error(f"""
                ### 🚨 MALWARE DETECTED
                
                | Metric | Value |
                |--------|-------|
                | **Threat Score** | `{result['threat_score']:.1%}` |
                | **Confidence** | `{result['confidence']:.1%}` |
                | **File** | `{result['file_name']}` |
                | **Hash** | `{result['file_hash']}` |
                
                ⚠️ **Recommended Action:** Quarantine and remove immediately.
                """)
            else:
                st.success(f"""
                ### ✅ CLEAN - Safe File
                
                | Metric | Value |
                |--------|-------|
                | **Security Score** | `{(1 - result['threat_score']):.1%}` |
                | **Confidence** | `{result['confidence']:.1%}` |
                | **File** | `{result['file_name']}` |
                | **Hash** | `{result['file_hash']}` |
                
                ✓ The file appears to be safe.
                """)
        
        # Suspicious features
        if result.get('suspicious_features'):
            st.markdown("#### ⚠️ Suspicious Features Detected")
            cols = st.columns(min(len(result['suspicious_features']), 5))
            for idx, feature in enumerate(result['suspicious_features'][:5]):
                with cols[idx % 5]:
                    st.markdown(f"""
                    <div style="background: rgba(239, 68, 68, 0.1); border-radius: 8px; padding: 0.5rem; text-align: center; border: 1px solid rgba(239, 68, 68, 0.3);">
                        <span style="color: #EF4444; font-size: 0.7rem;">{feature.replace('_', ' ')}</span>
                    </div>
                    """, unsafe_allow_html=True)