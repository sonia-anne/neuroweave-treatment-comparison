import plotly.graph_objects as go

# --- DATOS ORGANIZADOS POR NIVELES DE LA PIRÁMIDE ---
labels = [
    # Nivel clínico
    "🧠 Efficacy",
    "💥 Complication Risk",
    "♻️ Reintervention Need",
    # Nivel económico
    "💵 Patient Cost (USD)",
    "🌍 Global Accessibility",
    # Nivel tecnológico / ético
    "🧬 Tissue Regeneration",
    "🤖 AI + Real-Time Monitoring",
    "📈 Socioeconomic Impact"
]

# Valores estimados (cuantitativos o escalas)
traditional = [50, 90, 85, 10000, 20, 0, 0, 30]
neuro = [92.3, 10, 5, 1200, 70, 100, 100, 95]

# Colores por categoría (niveles piramidales)
colors_neuro = ['#00FFAB']*3 + ['#00C2FF']*2 + ['#FF61D2']*3
colors_trad = ['#FF6B6B']*3 + ['#FFC93C']*2 + ['#A29BFE']*3

# --- CONSTRUCCIÓN DEL GRÁFICO TIPO PIRÁMIDE ESCALONADA ---
fig = go.Figure()

# Barras para el tratamiento tradicional
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

# Barras para NEUROWEAVE
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

# --- ESTILO Y CONFIGURACIÓN VISUAL ---
fig.update_layout(
    title="🔺 Tri-Level Pyramid Comparison: NEUROWEAVE vs Traditional Shunt",
    title_font_size=24,
    barmode='group',
    plot_bgcolor='#0f172a',
    paper_bgcolor='#0f172a',
    font=dict(color='white', size=14),
    xaxis=dict(
        title="Quantitative Score / Cost (USD)",
        title_font=dict(size=16),
        showgrid=True,
        gridcolor='gray',
        linecolor='white',
        tickfont=dict(color='white')
    ),
    yaxis=dict(
        title="Evaluation Criteria",
        tickfont=dict(size=15, color='white'),
        categoryorder='array',
        categoryarray=list(reversed(labels))  # Inversión visual para pirámide
    ),
    legend=dict(
        orientation='h',
        yanchor='bottom',
        y=1.02,
        xanchor='center',
        x=0.5,
        font=dict(size=14)
    ),
    margin=dict(l=80, r=80, t=80, b=80)
)

# --- MOSTRAR GRÁFICO ---
fig.show()