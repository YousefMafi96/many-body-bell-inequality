import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.title("Bar Plot with Error Bars (Selectable)")

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

fig.update_layout(barmode='group')
st.plotly_chart(fig)