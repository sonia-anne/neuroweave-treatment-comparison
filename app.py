import streamlit as st
import plotly.graph_objects as go

# --- PAGE CONFIG ---
st.set_page_config(page_title="NEUROWEAVE Comparative Pyramid", layout="wide", page_icon="🧠")

# --- DARK MODE CSS ---
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

# --- HEADER ---
st.title("🔺 NEUROWEAVE vs Traditional Shunt")
st.markdown("### Tri-Level Comparative Pyramid with Clinical, Economic and Technological Impact")

# --- DATA ---
labels = [
    "🧠 Efficacy",
    "💥 Complication Risk",
    "♻️ Reintervention Need",
    "💵 Patient Cost (USD)",
    "🌍 Global Accessibility",
    "🧬 Tissue Regeneration",
    "🤖 AI + Monitoring",
    "📈 Socioeconomic Impact"
]

traditional = [50, 90, 85, 10000, 20, 0, 0, 30]
neuro = [92.3, 10, 5, 1200, 70, 100, 100, 95]

colors_neuro = ['#00FFAB']*3 + ['#00C2FF']*2 + ['#FF61D2']*3
colors_trad = ['#FF6B6B']*3 + ['#FFC93C']*2 + ['#A29BFE']*3

# --- FIGURE ---
fig = go.Figure()

fig.add_trace(go.Bar(
    y=labels,
    x=traditional,
    name="Traditional Shunt",
    orientation='h',
    marker=dict(color=colors_trad),
    hovertemplate="<b>Traditional:</b> %{x}<extra></extra>",
    text=traditional,
    textposition='auto'
))

fig.add_trace(go.Bar(
    y=labels,
    x=neuro,
    name="NEUROWEAVE",
    orientation='h',
    marker=dict(color=colors_neuro),
    hovertemplate="<b>NEUROWEAVE:</b> %{x}<extra></extra>",
    text=neuro,
    textposition='auto'
))

fig.update_layout(
    title="NEUROWEAVE vs Traditional Shunt – Impact Pyramid",
    title_font_size=22,
    barmode='group',
    plot_bgcolor='#0f172a',
    paper_bgcolor='#0f172a',
    font=dict(color='white', size=14),
    xaxis=dict(title="Score / Cost", gridcolor='gray', linecolor='white'),
    yaxis=dict(
        title="Evaluation Criteria",
        categoryorder='array',
        categoryarray=list(reversed(labels)),
        tickfont=dict(color='white')
    ),
    legend=dict(orientation='h', yanchor='bottom', y=1.05, xanchor='center', x=0.5)
)

# --- DISPLAY ---
st.plotly_chart(fig, use_container_width=True)

# --- FOOTER ---
st.markdown("---")
st.success("NEUROWEAVE is not science fiction – it's tangible, regenerative neurotech.")
st.caption("Created by Annette — Ecuadorian Global Researcher. 🧠")