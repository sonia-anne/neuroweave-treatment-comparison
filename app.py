import streamlit as st
import plotly.graph_objects as go
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="NEUROWEAVE – Comparative Intelligence Panel", layout="wide", page_icon="🧠")

# --- Estilo Oscuro Personalizado ---
st.markdown("""
    <style>
        .main { background-color: #0f172a; color: white; }
        .block-container { padding: 2rem; }
        h1, h2, h3, h4 { color: #3b82f6; text-align: center; }
        .card { background-color: #1e293b; border-radius: 12px; padding: 1.5rem; margin: 0.5rem 0; }
        ul { list-style: none; padding: 0; }
        li::before { content: "• "; color: #60a5fa; }
    </style>
""", unsafe_allow_html=True)

# --- Encabezado ---
st.image("https://cdn-icons-png.flaticon.com/512/2700/2700656.png", width=80)
st.title("NEUROWEAVE vs Traditional Shunt Systems")
st.markdown("#### Matrix comparison + heatmap + panel cards — powered by real data and regenerative vision")

# --- Tabla comparativa tipo heatmap ---
data = {
    "Criterion": [
        "Effectiveness (%)",
        "Failure Rate (2 yrs)",
        "Risk of Complications",
        "Fluid Strategy",
        "Reinterventions",
        "Patient Cost (USD)",
        "Accessibility",
        "Tissue Regeneration",
        "Real-time Monitoring",
        "AI Integration",
        "Socioeconomic Impact"
    ],
    "Traditional Shunt": [
        50, 50, 90,
        1, 85, 10000,
        20, 0, 0, 0, 30
    ],
    "NEUROWEAVE": [
        92.3, 7, 10,
        2, 5, 1200,
        70, 100, 100, 100, 95
    ]
}
df = pd.DataFrame(data)

fig = go.Figure(data=go.Heatmap(
    z=df.iloc[:, 1:].values,
    x=df.columns[1:],
    y=df["Criterion"],
    colorscale="Viridis",
    colorbar=dict(title="Score"),
    hoverongaps=False
))
fig.update_layout(
    title="🧪 Performance Matrix – Visual Comparison",
    font=dict(color="white"), plot_bgcolor="#0f172a", paper_bgcolor="#0f172a",
    title_font_size=22, margin=dict(t=60, l=50, r=50, b=50)
)
fig.update_xaxes(tickfont=dict(color="white"))
fig.update_yaxes(tickfont=dict(color="white"))
st.plotly_chart(fig, use_container_width=True)

# --- Panel Visual Tipo Tarjeta ---
st.markdown("### 🧠 Strategic Comparison Panel")

col1, col2 = st.columns(2)
with col1:
    st.markdown("#### 💉 Traditional Shunt")
    st.markdown("""
    <div class="card">
        <ul>
        <li><b>Effectiveness:</b> 50%</li>
        <li><b>Reinterventions:</b> Every 2–3 years</li>
        <li><b>Complications:</b> High (infections, obstruction)</li>
        <li><b>Monitoring:</b> ❌ None</li>
        <li><b>Neuroregeneration:</b> ❌ None</li>
        <li><b>Cost:</b> $5,000–$15,000</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("#### 🤖 NEUROWEAVE Nanotech")
    st.markdown("""
    <div class="card">
        <ul>
        <li><b>Effectiveness:</b> 92.3% (COMSOL)</li>
        <li><b>Reinterventions:</b> One-time delivery</li>
        <li><b>Complications:</b> Minimal (biodegradable)</li>
        <li><b>Monitoring:</b> ✅ Real-time AR interface</li>
        <li><b>Neuroregeneration:</b> ✅ BDNF & VEGF</li>
        <li><b>Cost:</b> ~$1,200</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

# --- Diagrama Radar ---
radar_data = pd.DataFrame({
    "Criteria": ["Efficiency", "Cost", "Complication Risk", "AI Assist", "Neuroregeneration", "Accessibility"],
    "Traditional Shunt": [50, 20, 30, 0, 0, 10],
    "NEUROWEAVE": [92, 95, 90, 100, 100, 80]
})

radar_fig = px.line_polar(
    radar_data.melt(id_vars=["Criteria"], var_name="Treatment", value_name="Score"),
    r="Score", theta="Criteria", color="Treatment", line_close=True,
    color_discrete_map={"Traditional Shunt": "#f43f5e", "NEUROWEAVE": "#3b82f6"},
    title="📊 Multivariable Radar Chart Comparison"
)
radar_fig.update_layout(paper_bgcolor="#0f172a", font=dict(color="white"))
st.plotly_chart(radar_fig, use_container_width=True)

# --- Pie de Página ---
st.markdown("---")
st.success("This is not a dream. It's NEUROWEAVE — a real shift in neuroregenerative surgery.")
st.caption("Created by Annette — Young Global Scientist from Ecuador. 🧠")