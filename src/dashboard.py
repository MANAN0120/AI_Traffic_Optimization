import streamlit as st
import random
import time
import pandas as pd

st.title("🚦 AI Traffic Optimization Dashboard")

# Placeholder for live data
placeholder = st.empty()

data = []

while True:
    # Simulated real values (later you can connect actual)
    lane1 = random.randint(0, 10)
    lane2 = random.randint(0, 10)
    lane3 = random.randint(0, 10)

    total = lane1 + lane2 + lane3

    if total < 5:
        density = "LOW"
    elif total < 10:
        density = "MEDIUM"
    else:
        density = "HIGH"

    if total < 5:
        signal_time = 10
    elif total < 10:
        signal_time = 20
    else:
        signal_time = 30

    # Store for graph
    data.append(total)

    with placeholder.container():
        st.subheader("📊 Live Traffic Data")

        col1, col2, col3 = st.columns(3)

        col1.metric("Lane 1", lane1)
        col2.metric("Lane 2", lane2)
        col3.metric("Lane 3", lane3)

        st.metric("Total Vehicles", total)
        st.write(f"Density: {density}")
        st.write(f"Signal Time: {signal_time} sec")

        # Graph
        df = pd.DataFrame(data, columns=["Traffic"])
        st.line_chart(df)

    time.sleep(1)