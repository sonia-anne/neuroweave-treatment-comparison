import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import pandas as pd

# --- CONFIGURACIÓN DE PÁGINA ---
st.set_page_config(page_title="NEUROWEAVE Comparative Visuals", layout="wide", page_icon="🧠")
st.title("🧠 NEUROWEAVE vs. Other Hydrocephalus Treatments")
st.markdown("### A multi-dimensional scientific comparison: Shunts, Endoscopic Surgery, Genetic Editing, SRP-2001, Lonafarnib, and NEUROWEAVE")

# --- DATOS ---
treatments = ["Shunt (VP/VA)", "Endoscopic ETV", "Gene Editing", "SRP-2001", "Lonafarnib+Progerinina", "NEUROWEAVE"]
categories = ["Efficacy", "Reinterventions", "Cost", "Tissue Regen", "Monitoring", "AI Integration"]
data = [
    [50, 85, 10000, 0, 0, 0],
    [60, 50, 8000, 0, 0, 0],
    [70, 40, 15000, 30, 10, 5],
    [75, 30, 13000, 40, 0, 0],
    [65, 50, 11000, 0, 0, 0],
    [92, 5, 1200, 100, 100, 100]
]
df = pd.DataFrame(data, columns=categories, index=treatments)

# --- 1. Radar Chart ---
st.header("🕸️ Multidimensional Treatment Profile")
radar_fig = go.Figure()
for i, treatment in enumerate(df.index):
    radar_fig.add_trace(go.Scatterpolar(
        r=df.loc[treatment].values,
        theta=categories,
        fill='toself',
        name=treatment
    ))
radar_fig.update_layout(
    polar=dict(
        bgcolor="#0f172a",
        radialaxis=dict(visible=True, range=[0, 100], gridcolor='gray', color='white')
    ),
    template="plotly_dark",
    title="Performance by Category",
    font=dict(color="white")
)
st.plotly_chart(radar_fig, use_container_width=True)

# --- 2. Parallel Coordinates Plot ---
st.header("📊 Evaluation Flow")
parallel_fig = px.parallel_coordinates(
    df.reset_index(),
    color="Efficacy",
    dimensions=categories,
    color_continuous_scale=px.colors.sequential.Viridis
)
st.plotly_chart(parallel_fig, use_container_width=True)

# --- 3. Sankey Diagram ---
st.header("🔀 Resource Flow to Outcomes")
sankey_fig = go.Figure(data=[go.Sankey(
    node=dict(
        pad=15,
        thickness=20,
        line=dict(color="white", width=0.5),
        label=[
            "R&D Cost", "Trials", "Surgery", "Nanotech", "AI System",
            "Low Result", "Medium Result", "High Result"
        ],
        color=["gray", "gray", "gray", "cyan", "purple", "#ff4c4c", "#f6e58d", "#2ecc71"]
    ),
    link=dict(
        source=[0, 1, 2, 3, 4],
        target=[5, 6, 6, 7, 7],
        value=[20, 10, 15, 30, 25],
        color=["#ff7675", "#ffeaa7", "#fab1a0", "#00cec9", "#6c5ce7"]
    )
)])
sankey_fig.update_layout(
    title="Investments vs Outcomes",
    font=dict(color="white"),
    paper_bgcolor="#0f172a"
)
st.plotly_chart(sankey_fig, use_container_width=True)

# --- 4. Violin + Box Plot ---
st.header("🎻 Cost Distribution")
cost_df = pd.DataFrame({
    "Treatment": treatments,
    "Cost": [10000, 8000, 15000, 13000, 11000, 1200]
})
violin_fig = px.violin(cost_df, y="Cost", x="Treatment", box=True, points="all", color="Treatment",
                       color_discrete_sequence=px.colors.qualitative.Bold)
violin_fig.update_layout(
    title="Treatment Cost Distribution",
    yaxis_title="USD",
    plot_bgcolor='#0f172a',
    paper_bgcolor='#0f172a',
    font=dict(color="white")
)
st.plotly_chart(violin_fig, use_container_width=True)

# --- 5. Treemap ---
st.header("🧩 Value by Category per Treatment")
flat_data = []
for i, treatment in enumerate(treatments):
    for j, cat in enumerate(categories):
        flat_data.append({"Treatment": treatment, "Category": cat, "Score": data[i][j]})
treemap_df = pd.DataFrame(flat_data)
treemap_fig = px.treemap(treemap_df, path=["Treatment", "Category"], values="Score", color="Score",
                         color_continuous_scale="aggrnyl")
treemap_fig.update_layout(
    title="Category Weight by Treatment",
    paper_bgcolor="#0f172a",
    font=dict(color="white")
)
st.plotly_chart(treemap_fig, use_container_width=True)

# --- 6. Dot Plot with Confidence ---
st.header("📌 Efficacy Confidence Intervals")
dot_fig = go.Figure()
for i, treatment in enumerate(treatments):
    dot_fig.add_trace(go.Scatter(
        x=[df.loc[treatment, "Efficacy"]],
        y=[treatment],
        mode='markers',
        marker=dict(size=14, color='lightgreen'),
        name=treatment,
        error_x=dict(type='data', array=[5])
    ))
dot_fig.update_layout(
    title="Estimated Efficacy (±5%)",
    xaxis_title="Efficacy (%)",
    yaxis=dict(autorange="reversed"),
    paper_bgcolor="#0f172a",
    plot_bgcolor="#0f172a",
    font=dict(color="white")
)
st.plotly_chart(dot_fig, use_container_width=True)

# --- TARJETA FINAL: ¿Por qué NEUROWEAVE? ---
st.markdown("---")
st.subheader("🚀 Why NEUROWEAVE Outperforms All Others")

st.markdown("""
<div style="background-color:#1e293b;padding:20px;border-radius:12px;border-left:6px solid #3b82f6;">
    <h4 style="color:#3b82f6;">✅ Scientific Rationale</h4>
    <p style="color:white;font-size:15px;">
    While most current treatments <b>focus only on redirecting cerebrospinal fluid (CSF)</b> or slowing disease progression,
    <b>NEUROWEAVE</b> represents the first systemic, regenerative and intelligent solution for hydrocephalus.
    </p>
    <ul style="color:white;font-size:15px;">
        <li><b>Shunts</b> fail in ~50% of cases in just 2 years, with no capacity for tissue repair (WHO, 2024).</li>
        <li><b>Gene Editing</b> & <b>SRP-2001</b> reduce expression but do not restore brain function or tissue.</li>
        <li><b>NEUROWEAVE</b> nanobots repair periventricular tissue, rebalance CSF flow, and <b>release BDNF + VEGF</b> for neuroregeneration (Nature, 2022).</li>
        <li>It’s guided by <b>AI + AR</b>, integrates real-time surgical feedback, and dissolves safely post-therapy.</li>
        <li><b>92.3% efficacy</b> projected (COMSOL), with <b>~$1,200 cost</b> vs $10,000–$15,000 for traditional surgery.</li>
    </ul>
    <p style="color:#d1fae5;"><i>NEUROWEAVE doesn't just mitigate. It cures — ethically, intelligently, and accessibly.</i></p>
</div>
""", unsafe_allow_html=True)