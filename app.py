import plotly.graph_objects as go

# --- CRITERIOS ORGANIZADOS POR NIVELES (ESTILO PIRÁMIDE) ---
labels = [
    # Nivel Clínico
    "🧠 Clinical Efficacy",
    "💥 Complication Risk",
    "♻️ Reintervention Rate",
    # Nivel Económico
    "💵 Patient Cost (USD)",
    "🌍 Global Accessibility",
    # Nivel Tecnológico / Ético
    "🧬 Regenerative Capacity",
    "🤖 AI + Real-time Control",
    "📈 Social Reintegration"
]

# --- VALORES COMPARATIVOS ---
traditional_values = [50, 90, 85, 10000, 20, 0, 0, 30]
neuro_values = [92.3, 10, 5, 1200, 70, 100, 100, 95]

# --- COLORES POR NIVEL (NEUROWEAVE Y SHUNT) ---
colors_neuro = ['#00FFAB'] * 3 + ['#38BDF8'] * 2 + ['#F472B6'] * 3
colors_traditional = ['#EF4444'] * 3 + ['#FACC15'] * 2 + ['#A78BFA'] * 3

# --- CREACIÓN DEL GRÁFICO ---
fig = go.Figure()

# Barras Tradicionales
fig.add_trace(go.Bar(
    y=labels,
    x=traditional_values,
    name='Traditional Shunt',
    orientation='h',
    marker=dict(color=colors_traditional),
    text=traditional_values,
    textposition='outside',
    hovertemplate="<b>Traditional Shunt:</b> %{x}<extra></extra>"
))

# Barras NEUROWEAVE
fig.add_trace(go.Bar(
    y=labels,
    x=neuro_values,
    name='NEUROWEAVE',
    orientation='h',
    marker=dict(color=colors_neuro),
    text=neuro_values,
    textposition='outside',
    hovertemplate="<b>NEUROWEAVE:</b> %{x}<extra></extra>"
))

# --- ESTÉTICA Y DISEÑO AVANZADO ---
fig.update_layout(
    title="🔺 Tri-Level Pyramid Comparison: NEUROWEAVE vs Traditional Shunt",
    title_font_size=26,
    title_x=0.5,
    barmode='group',
    plot_bgcolor='#0f172a',
    paper_bgcolor='#0f172a',
    font=dict(color='white', size=15),
    xaxis=dict(
        title="Quantitative Score / Cost (USD)",
        title_font=dict(size=18),
        showgrid=True,
        gridcolor='gray',
        tickfont=dict(color='white'),
        linecolor='white',
        zerolinecolor='white'
    ),
    yaxis=dict(
        title="Evaluation Criteria",
        title_font=dict(size=18),
        tickfont=dict(size=15, color='white'),
        categoryorder='array',
        categoryarray=list(reversed(labels))
    ),
    legend=dict(
        orientation='h',
        yanchor='top',
        y=1.1,
        xanchor='center',
        x=0.5,
        bgcolor='rgba(0,0,0,0)',
        bordercolor='white',
        font=dict(size=14)
    ),
    margin=dict(t=100, l=80, r=80, b=80)
)

# --- MOSTRAR EL GRÁFICO ---
fig.show()