import streamlit as st
import plotly.graph_objects as go
import numpy as np

st.set_page_config(layout="wide")

st.title("Bar Plot with Error Bars")

# ---- Data ----
categories = ["1", "2", "3", "4", "5", "6"]

data = {}
data["Ideal"] = {"mean": [3.414213562,	2.896243218,	2.932409609,	2.950974898,	2.96,	2.96], "error": [0.0,0.0,0.0,0.0,0.0,0.0]}
data["FakeBackend"] = {"mean": [3.377929688,	2.712239583,	2.51515997,	2.285563151,	1.959834929,	1.656975963], "error": [0.0,0.0,0.0,0.0,0.0,0.0]}
data["FakeBackend + EM"] = {"mean": [3.394705594,	2.786815685,	2.623056273,	2.418573401,	2.108651982,	1.825453196], "error": [0.0,0.0,0.0,0.0,0.0,0.0]}
data["ibm_torino (QFT)"] = {"mean": [3.337402344,	2.573079427,	2.265206473,	1.511653646,	1.241223538,	0.978019593], "error": [0.0,0.0,0.0,0.0,0.0,0.0]}
data["ibm_torino + EM (QFT)"] = {"mean": [3.387702823,	2.836673297,	2.604488405,	1.741819115,	1.512698746,	1.371515795], "error": [0.0,0.0,0.0,0.0,0.0,0.0]}
data["ibm_torino (DQFT)"] = {"mean": [None, 2.61702474,	2.500093006,	2.16023763,	1.961693548,	1.567243304], "error": [0.0,0.0,0.0,0.0,0.0,0.0]}
data["ibm_torino + EM (DQFT)"] = {"mean": [None, 2.755993798,	2.654109524,	2.387892074,	2.327147454,	1.971485801], "error": [0.0,0.0,0.0,0.0,0.0,0.0]}
# ---- Layout ----

col1, col2 = st.columns([1, 3])

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
            error_y=dict(type='data', array=data[name]["error"])
        ))

    # ---- Fixed size ----
    fig.update_layout(
        width=800,
        height=600,
        barmode='group',
    
        plot_bgcolor='white',
        paper_bgcolor='white',
    
        # Axis titles
        xaxis_title="n",
        yaxis_title="Id",
    
        # 🔥 Explicit axis title font control
        xaxis_title_font=dict(size=18, family="Arial", color="black"),
        yaxis_title_font=dict(size=18, family="Arial", color="black"),
    
        # Tick label size (numbers on axis)
        xaxis=dict(
            showline=True,
            linewidth=2,
            linecolor='black',
            mirror=True,
            ticks='outside',
            tickfont=dict(size=18)
        ),
        yaxis=dict(
            showline=True,
            linewidth=2,
            linecolor='black',
            mirror=True,
            ticks='outside',
            tickfont=dict(size=18)
        ),
    
        legend=dict(font=dict(size=14))
    )
    
    st.plotly_chart(fig, use_container_width=False)










