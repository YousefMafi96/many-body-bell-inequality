import streamlit as st
import plotly.graph_objects as go
import numpy as np

# Force white background
st.set_page_config(layout="wide")

st.title("Bell Inequality value")

categories = ["A", "B", "C", "D"]

np.random.seed(1)

data = {}
for i in range(1, 9):
    means = np.random.uniform(5, 15, 4)
    errors = np.random.uniform(0.5, 2, 4)
    data[f"Dataset {i}"] = {"mean": means, "error": errors}

selected = st.multiselect(
    "Select datasets",
    list(data.keys()),
    default=list(data.keys())
)

fig = go.Figure()

for name in selected:
    fig.add_trace(go.Bar(
        name=name,
        x=categories,
        y=data[name]["mean"],
        error_y=dict(type='data', array=data[name]["error"])
    ))

fig.update_layout(
    barmode='group',

    # White background
    plot_bgcolor='white',
    paper_bgcolor='white',

    # Axis labels with LaTeX
    xaxis_title=r"$\mathrm{Category}$",
    yaxis_title=r"$\mathrm{Value\ (units)}$",

    # Font customization
    font=dict(
        family="Arial",
        size=18,
        color="black"
    ),

    # Axis styling
    xaxis=dict(
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True,
        ticks='outside',
        tickfont=dict(size=16)
    ),
    yaxis=dict(
        showline=True,
        linewidth=2,
        linecolor='black',
        mirror=True,
        ticks='outside',
        tickfont=dict(size=16)
    ),

    legend=dict(
        font=dict(size=16)
    )
)

st.plotly_chart(fig, use_container_width=True)
