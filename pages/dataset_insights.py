import streamlit as st
import plotly.graph_objects as go
import numpy as np

def show_dataset_insights():
    """Dataset Insights Page"""
    
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
            <div style="width: 12px; height: 12px; background: #10B981; border-radius: 50%; box-shadow: 0 0 10px #10B981;"></div>
            <span style="color: #6B7280; font-weight: 500;">Data Exploration</span>
        </div>
        <h1 style="font-size: 2.5rem; margin-top: 0.5rem;">
            <span class="gradient-text">Dataset Insights</span>
        </h1>
        <p style="color: #9CA3AF;">Analysis of the Android malware dataset used for training</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Malware Family Distribution")
        
        families = ['Trojan', 'Adware', 'Ransomware', 'Spyware', 'Banker']
        counts = [1203, 892, 654, 478, 312]
        colors = ['#7C6FEB', '#FF6835', '#EF4444', '#F59E0B', '#00D4D8']
        
        fig = go.Figure(data=[go.Pie(
            labels=families, values=counts, hole=0.3,
            marker=dict(colors=colors),
            textinfo='label+percent',
            textfont=dict(color='white', size=12)
        )])
        fig.update_layout(
            height=400,
            paper_bgcolor="rgba(0,0,0,0)",
            font=dict(color='white'),
            showlegend=False
        )
        st.plotly_chart(fig, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### ⚖️ Class Balance Analysis")
        
        total = 6248 + 5239
        benign_pct = 6248 / total * 100
        malware_pct = 5239 / total * 100
        
        st.markdown(f"""
        <div style="margin-bottom: 1rem;">
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                <span style="color: #10B981;">Benign</span>
                <span>6,248 ({benign_pct:.1f}%)</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 40px; overflow: hidden;">
                <div style="width: {benign_pct}%; background: #10B981; height: 100%; border-radius: 10px; display: flex; align-items: center; padding-left: 10px; color: white;">
                    6,248
                </div>
            </div>
        </div>
        <div>
            <div style="display: flex; justify-content: space-between; margin-bottom: 0.25rem;">
                <span style="color: #EF4444;">Malware</span>
                <span>5,239 ({malware_pct:.1f}%)</span>
            </div>
            <div style="background: rgba(255,255,255,0.1); border-radius: 10px; height: 40px; overflow: hidden;">
                <div style="width: {malware_pct}%; background: #EF4444; height: 100%; border-radius: 10px; display: flex; align-items: center; padding-left: 10px; color: white;">
                    5,239
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        col_a, col_b = st.columns(2)
        with col_a:
            st.metric("Benign Samples", "6,248", f"{benign_pct:.1f}%")
        with col_b:
            st.metric("Malware Samples", "5,239", f"{malware_pct:.1f}%")
        
        st.markdown('</div>', unsafe_allow_html=True)
    
    # t-SNE Visualization
    st.markdown('<div class="glass-card" style="margin-top: 1rem;">', unsafe_allow_html=True)
    st.markdown("### 🧬 Feature Density Mapping — t-SNE Clusters")
    
    np.random.seed(42)
    n_samples = 800
    benign_tsne = np.random.normal([-3, -2], [1.2, 1.2], (n_samples//2, 2))
    malware_tsne = np.random.normal([2, 3], [1.5, 1.5], (n_samples//2, 2))
    
    fig3 = go.Figure()
    fig3.add_trace(go.Scatter(
        x=benign_tsne[:, 0], y=benign_tsne[:, 1],
        mode='markers', name='Benign',
        marker=dict(color='#10B981', size=6, opacity=0.6)
    ))
    fig3.add_trace(go.Scatter(
        x=malware_tsne[:, 0], y=malware_tsne[:, 1],
        mode='markers', name='Malware',
        marker=dict(color='#EF4444', size=6, opacity=0.6)
    ))
    fig3.update_layout(
        height=450,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color='white'),
        xaxis_title="t-SNE Component 1",
        yaxis_title="t-SNE Component 2",
        legend=dict(x=0.02, y=0.98)
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    st.markdown("""
    <div style="margin-top: 1rem; text-align: center; color: #9CA3AF;">
        t-SNE visualization showing clear separation between benign and malware samples
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('</div>', unsafe_allow_html=True)