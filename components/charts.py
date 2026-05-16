import streamlit as st
import plotly.graph_objects as go

def create_gauge(value, title="Threat Score", is_malware=False):
    """Create a gauge chart"""
    fig = go.Figure(go.Indicator(
        mode="gauge+number",
        value=value * 100,
        title={"text": title, "font": {"color": "white", "size": 14}},
        gauge={
            "axis": {"range": [0, 100], "tickcolor": "white", "tickfont": {"color": "white"}},
            "bar": {"color": "#EF4444" if is_malware else "#10B981"},
            "bgcolor": "rgba(0,0,0,0.3)",
            "steps": [
                {"range": [0, 33], "color": "rgba(16, 185, 129, 0.2)"},
                {"range": [33, 66], "color": "rgba(245, 158, 11, 0.2)"},
                {"range": [66, 100], "color": "rgba(239, 68, 68, 0.2)"}
            ],
            "threshold": {"line": {"color": "#EF4444", "width": 4}, "value": 65}
        }
    ))
    fig.update_layout(height=300, paper_bgcolor="rgba(0,0,0,0)", font={"color": "white"})
    return fig

def create_feature_bar_chart(features, values, title="Feature Importance"):
    """Create a horizontal bar chart for features"""
    colors = ['#EF4444' if v > 0 else '#10B981' for v in values]
    
    fig = go.Figure()
    fig.add_trace(go.Bar(
        y=features,
        x=values,
        orientation='h',
        marker=dict(color=colors, line=dict(color='white', width=1)),
        text=[f"{'+' if v > 0 else ''}{v:.3f}" for v in values],
        textposition='outside',
        textfont=dict(color='white', size=11)
    ))
    fig.update_layout(
        height=450,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(color='white'),
        xaxis_title="SHAP Value (Impact on Prediction)",
        yaxis_title="Features",
        xaxis=dict(gridcolor='rgba(255,255,255,0.1)')
    )
    fig.add_vline(x=0, line_dash="dash", line_color="white", opacity=0.5)
    return fig