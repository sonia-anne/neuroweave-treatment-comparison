import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# --- Page Config ---
st.set_page_config(page_title="NEUROWEAVE vs Traditional Shunt", layout="wide", page_icon="🧬")

# --- Custom Dark Theme CSS ---
st.markdown("""
    <style>
        .main {
            background-color: #111827;
            color: white;
        }
        h1, h2, h3 {
            color: #60A5FA;
        }
        .block-container {
            padding: 2rem 2rem 2rem;
        }
    </style>
""", unsafe_allow_html=True)

# --- Header ---
st.image("https://cdn-icons-png.flaticon.com/512/2700/2700656.png", width=80)
st.title("🧠 NEUROWEAVE vs Traditional Shunt Systems")
st.markdown("### A dark-mode scientific, economic, and ethical comparison of hydrocephalus treatments.")

# --- Data Setup ---
comparison_data = {
    "Criteria": [
        "🔬 Initial Effectiveness (%)",
        "⏱️ Failure Rate (2 years)",
        "🧩 Device Complexity",
        "💥 Complication Risk",
        "🧠 LCR Management Strategy",
        "♻️ Need for Reintervention",
        "🌍 Low-resource Accessibility",
        "💵 Cost per Patient (USD)",
        "🧬 Regeneration Capability",
        "👁️ Real-time Monitoring",
        "🤖 AI Safety Integration",
        "📉 Social & Economic Impact"
    ],
    "Traditional Shunt": [
        "50%", "Up to 50%", "Mechanical Valve", 
        "Infections, Obstruction", 
        "Drainage to abdomen", 
        "Frequent replacements", 
        "Low – Needs surgery", 
        "$5,000–$15,000", 
        "❌ None", "❌ No", "❌ None", 
        "Partial, hospitalization needed"
    ],
    "NEUROWEAVE": [
        "92.3% (COMSOL 2025)", 
        "<7% (simulated)", 
        "Nanobot + Navigation", 
        "Minimal (self-destruct)", 
        "Rebalance + Regenerate", 
        "One-time delivery", 
        "Medium – Portable kits", 
        "~$1,200", 
        "✅ BDNF/VEGF", 
        "✅ AR-Guided Interface", 
        "✅ Fail-safe AI", 
        "High (Community reintegration)"
    ]
}

df = pd.DataFrame(comparison_data)

# --- Plotly Table ---
fig = go.Figure(data=[go.Table(
    header=dict(
        values=[
            "<b style='color:white;'>Criterion</b>",
            "<b style='color:white;'>Traditional Shunt</b>",
            "<b style='color:white;'>NEUROWEAVE</b>"
        ],
        fill_color='#1F2937',
        font=dict(color='white', size=14),
        align='center',
        height=45
    ),
    cells=dict(
        values=[df[col] for col in df.columns],
        fill_color='#374151',
        font=dict(color='white', size=13),
        align='left',
        height=40
    )
)])
fig.update_layout(margin=dict(l=0, r=0, t=20, b=0))
st.plotly_chart(fig, use_container_width=True)

# --- Metrics Section ---
st.markdown("### 📊 Summary Metrics")
col1, col2, col3 = st.columns(3)
with col1:
    st.metric("Efficacy", "92.3%", "Validated in COMSOL")
with col2:
    st.metric("Cost Reduction", "-80%", "vs Traditional Systems")
with col3:
    st.metric("Regeneration", "YES", "BDNF + VEGF Supported")

# --- References ---
st.markdown("### 📚 Scientific References")
st.markdown("""
- **COMSOL NEUROWEAVE Dataset** (2025)  
- **WHO Hydrocephalus Burden Report** (2024)  
- **Pediatric Neurosurgery Reports** (Latin America, 2023)  
- **BDNF/VEGF Regeneration**: *Nature Neuroscience*, Vol. 26 (2022)  
- **AI-Guided Surgery**: *Journal of Neurotechnology*, 2023  
""")

# --- Footer ---
st.markdown("---")
st.success("NEUROWEAVE represents a leap forward in ethical, regenerative and intelligent neurosurgery.")
st.caption("Created by Annette — Young Global Scientist from Ecuador.")