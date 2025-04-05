import streamlit as st
import plotly.graph_objects as go

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="NEUROWEAVE Radar Chart", layout="wide", page_icon="🧠")

# --- ESTILO OSCURO PERSONALIZADO ---
st.markdown("""
    <style>
        .main {
            background-color: #0f172a;
            color: white;
        }
        h1, h2 {
            color: #60a5fa;
            text-align: center;
        }
        .block-container {
            padding: 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- TÍTULO ---
st.title("🕸️ NEUROWEAVE vs Existing Treatments – Radar Chart")
st.markdown("### Spider chart comparing key performance metrics of hydrocephalus treatments")

# --- CRITERIOS DE COMPARACIÓN ---
criteria = [
    "Efficacy", "Durability", "Complication Risk (Inverse)", "Cost Efficiency",
    "Tissue Regeneration", "Precision", "Real-Time Monitoring", "Accessibility"
]

# --- VALORES PARA CADA TRATAMIENTO ---
neuro = [92, 95, 90, 85, 100, 95, 100, 80]
traditional_shunt = [50, 40, 20, 50, 0, 30, 0, 40]
programmable_valve = [55, 60, 40, 30, 0, 50, 10, 35]
endoscopic_surgery = [70, 75, 60, 65, 10, 80, 40, 50]

# --- CREACIÓN DEL GRÁFICO ---
fig = go.Figure()

fig.add_trace(go.Scatterpolar(
    r=neuro,
    theta=criteria,
    fill='toself',
    name='NEUROWEAVE',
    line=dict(color='#00FFAB', width=4)
))

fig.add_trace(go.Scatterpolar(
    r=traditional_shunt,
    theta=criteria,
    fill='toself',
    name='Traditional Shunt',
    line=dict(color='crimson', width=2)
))

fig.add_trace(go.Scatterpolar(
    r=programmable_valve,
    theta=criteria,
    fill='toself',
    name='Programmable Valve',
    line=dict(color='#F59E0B', width=2)
))

fig.add_trace(go.Scatterpolar(
    r=endoscopic_surgery,
    theta=criteria,
    fill='toself',
    name='Endoscopic Surgery',
    line=dict(color='#3B82F6', width=2)
))

# --- DISEÑO GENERAL ---
fig.update_layout(
    polar=dict(
        bgcolor="#0f172a",
        radialaxis=dict(
            visible=True,
            range=[0, 100],
            gridcolor="gray",
            linecolor="white",
            tickfont=dict(color='white'),
        ),
        angularaxis=dict(
            tickfont=dict(color='white')
        )
    ),
    showlegend=True,
    legend=dict(
        orientation='h',
        yanchor='top',
        y=1.1,
        xanchor='center',
        x=0.5,
        font=dict(color='white')
    ),
    paper_bgcolor='#0f172a',
    plot_bgcolor='#0f172a',
    font=dict(color='white'),
    title='NEUROWEAVE vs Existing Hydrocephalus Treatments – Radar Comparison',
    title_font_size=22
)

# --- MOSTRAR EN STREAMLIT ---
st.plotly_chart(fig, use_container_width=True)

# --- PIE DE PÁGINA ---
st.markdown("---")
st.success("NEUROWEAVE outperforms current treatments by combining regeneration, precision, and ethical tech.")
st.caption("Created by Annette — Young Global Researcher from Ecuador.")