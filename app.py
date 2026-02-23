import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout="wide")

st.title("Bar Plot with Error Bars")

# ---- Data ----
categories = ["A", "B", "C", "D"]
np.random.seed(1)

data = {}
for i in range(1, 9):
    means = np.random.uniform(5, 15, 4)
    errors = np.random.uniform(0.5, 2, 4)
    data[f"Dataset {i}"] = {"mean": means, "error": errors}

# ---- Layout: Two Columns ----
col1, col2 = st.columns([1, 3])  # left small, right big

# ---- LEFT: Dataset Selection ----
with col1:
    st.subheader("Select Datasets")
    selected_data = []

    for name in data.keys():
        if st.checkbox(name, value=True):
            selected_data.append(name)

# ---- RIGHT: Plot ----
with col2:
    fig = go.Figure()

    for name in selected_data:
        fig.add_trace(go.Bar(
            name=name,
            x=categories,
            y=data[name]["mean"],
            error_y=dict(
                type='data',
                array=data[name]["error"]
            )
        ))

    fig.update_layout(
        barmode='group',

        # White background
        plot_bgcolor='white',
        paper_bgcolor='white',

        # LaTeX labels
        xaxis_title=r"$\mathrm{Category}$",
        yaxis_title=r"$\mathrm{Value\ (units)}$",

        # Global font
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
            ticks='outside'
        ),
        yaxis=dict(
            showline=True,
            linewidth=2,
            linecolor='black',
            mirror=True,
            ticks='outside'
        ),

        legend=dict(
            font=dict(size=14)
        )
    )

    st.plotly_chart(fig, use_container_width=True)
