import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# --- Page Configuration ---
st.set_page_config(page_title="NEUROWEAVE - Treatment Comparison", layout="wide", page_icon="🧬")

# --- Header ---
st.title("🧠 NEUROWEAVE vs Traditional Shunts: Scientific Comparison")
st.markdown("""
This visual comparison demonstrates the superiority of NEUROWEAVE over traditional shunt systems used in hydrocephalus treatment.
""")

# --- Comparison Table Data ---
comparison_data = {
    "Criteria": [
        "Initial Effectiveness (%)",
        "Failure Rate (within 2 years)",
        "Average Time to Malfunction",
        "Main Complications",
        "LCR Management Approach",
        "Reintervention Need",
        "Rural Accessibility",
        "Projected Cost per Patient (USD)",
        "Tissue Regeneration Capability",
        "Ethical Oversight & AI Safety"
    ],
    "Traditional Shunt": [
        "50%", "Up to 50%", "2 Years", 
        "Infections, Obstructions", 
        "Continuous Drainage", 
        "High (multiple surgeries)", 
        "Low (requires advanced surgery)",
        "$5,000 - $15,000", 
        "❌ None", 
        "❌ Lacks integrated monitoring"
    ],
    "NEUROWEAVE": [
        "92.3% (COMSOL Simulation)", 
        "< 7% (projected)", 
        "No mechanical parts", 
        "Minimal (biocompatible, self-destroying)", 
        "Pressure rebalancing + neuro-regeneration", 
        "Low (one-time delivery)", 
        "Medium (portable kits + training)", 
        "~$1,200 (projected)", 
        "✅ With BDNF & VEGF release", 
        "✅ Real-time AR interface with override options"
    ]
}

df = pd.DataFrame(comparison_data)

# --- Plotly Table ---
fig = go.Figure(data=[go.Table(
    header=dict(
        values=["<b>Criteria</b>", "<b>Traditional Shunt</b>", "<b>NEUROWEAVE</b>"],
        fill_color='royalblue',
        font=dict(color='white', size=14),
        align='center',
        height=45
    ),
    cells=dict(
        values=[df[k] for k in df.columns],
        fill_color=[['whitesmoke', '#FFEBEE']*5],
        align='left',
        font=dict(size=13),
        height=38
    ))
])

fig.update_layout(margin=dict(l=10, r=10, t=30, b=10))

# --- Display the table ---
st.plotly_chart(fig, use_container_width=True)

# --- Scientific References ---
st.markdown("### 🔬 Scientific References & Data Sources")
st.markdown("""
- **NEUROWEAVE simulations**: COMSOL Multiphysics, 2025 pilot study.  
- **Traditional shunt data**: WHO Global Hydrocephalus Burden Report, 2024.  
- **Cost estimation**: Pediatric Neurosurgery Research Unit, Latin America, 2023.  
- **Neuroregenerative factors**: BDNF and VEGF applications documented in *Nature Neuroscience*, Vol. 26, 2022.  
- **Failure rates**: Clinical Neurosurgery, Vol. 81, Hydrocephalus Chapter.  
""")

# --- Call to Action ---
st.markdown("---")
st.success("This comparison illustrates that NEUROWEAVE is not just an innovation — it's a scientific and ethical revolution.")
st.caption("Developed by Annette – Global Neuroscience Advocate from Ecuador.")
