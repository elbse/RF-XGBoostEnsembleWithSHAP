import streamlit as st
import plotly.graph_objects as go
from utils import get_shap_values

def show_shap_explainability():
    """SHAP Explainability Page"""
    
    st.markdown("""
    <div style="margin-bottom: 2rem;">
        <div style="display: flex; align-items: center; gap: 0.75rem;">
            <div style="width: 12px; height: 12px; background: #F59E0B; border-radius: 50%; box-shadow: 0 0 10px #F59E0B;"></div>
            <span style="color: #6B7280; font-weight: 500;">Model Explainability</span>
        </div>
        <h1 style="font-size: 2.5rem; margin-top: 0.5rem;">
            <span class="gradient-text">SHAP Explainability</span>
        </h1>
        <p style="color: #9CA3AF;">Understanding feature contributions using SHAP (SHapley Additive exPlanations)</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📊 Feature Contribution Analysis — Waterfall")
        
        shap_values = get_shap_values()
        features = list(shap_values.keys())
        values = list(shap_values.values())
        
        from components import create_feature_bar_chart
        fig = create_feature_bar_chart(features, values)
        st.plotly_chart(fig, use_container_width=True)
        
        st.markdown("""
        <div style="display: flex; gap: 2rem; justify-content: center; margin-top: 1rem;">
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <div style="width: 20px; height: 20px; background: #EF4444; border-radius: 4px;"></div>
                <span style="font-size: 0.875rem;">Increases malware risk</span>
            </div>
            <div style="display: flex; align-items: center; gap: 0.5rem;">
                <div style="width: 20px; height: 20px; background: #10B981; border-radius: 4px;"></div>
                <span style="font-size: 0.875rem;">Decreases malware risk</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    with col2:
        st.markdown('<div class="glass-card">', unsafe_allow_html=True)
        st.markdown("### 📈 Global Feature Importance")
        
        # Global importance (mean absolute SHAP)
        global_importance = [abs(v) for v in values]
        sorted_idx = sorted(range(len(global_importance)), key=lambda i: global_importance[i], reverse=True)
        
        fig2 = go.Figure()
        fig2.add_trace(go.Bar(
            x=[global_importance[i] for i in sorted_idx[:7]],
            y=[features[i] for i in sorted_idx[:7]],
            orientation='h',
            marker=dict(color='#3B82F6', line=dict(color='white', width=1)),
            text=[f"{global_importance[i]:.3f}" for i in sorted_idx[:7]],
            textposition='outside'
        ))
        fig2.update_layout(
            height=450,
            paper_bgcolor="rgba(0,0,0,0)",
            plot_bgcolor="rgba(0,0,0,0)",
            font=dict(color='white'),
            xaxis_title="Mean |SHAP Value|",
            yaxis_title="Features"
        )
        st.plotly_chart(fig2, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # Waterfall plot for single prediction
    st.markdown('<div class="glass-card" style="margin-top: 1rem;">', unsafe_allow_html=True)
    st.markdown("### 🌊 Waterfall Plot — Single Prediction Explanation")
    
    base_value = 0.487
    final_value = base_value + sum(values[:7])
    
    fig3 = go.Figure(go.Waterfall(
        name="SHAP Values",
        orientation="v",
        measure=["absolute"] + ["relative"] * len(features[:7]),
        x=["Base Value"] + features[:7],
        y=[base_value] + values[:7],
        text=[f"{base_value:.3f}"] + [f"{v:+.3f}" for v in values[:7]],
        textposition="outside",
        connector={"line": {"color": "rgba(255,255,255,0.3)"}},
        increasing={"marker": {"color": "#EF4444"}},
        decreasing={"marker": {"color": "#10B981"}}
    ))
    fig3.update_layout(
        height=500,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color='white'),
        title="Prediction Path Explanation",
        xaxis_title="Features",
        yaxis_title="Cumulative SHAP Value"
    )
    st.plotly_chart(fig3, use_container_width=True)
    
    col_a, col_b, col_c = st.columns(3)
    with col_a:
        st.metric("Base Value", f"{base_value:.3f}", help="Expected model output without any features")
    with col_b:
        st.metric("Final Prediction", f"{final_value:.3f}", help="Actual model output with all features")
    with col_c:
        st.metric("Net SHAP Impact", f"{final_value - base_value:+.3f}", help="Total contribution from all features")
    
    st.markdown('</div>', unsafe_allow_html=True)