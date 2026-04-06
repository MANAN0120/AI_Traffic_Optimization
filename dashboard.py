import streamlit as st
import random
import time
import pandas as pd

st.set_page_config(page_title="AI Traffic System", layout="wide")

st.title("🚦 AI Traffic Optimization Dashboard")

# Store history
if "data" not in st.session_state:
    st.session_state.data = []

placeholder = st.empty()

while True:
    # Simulated data (you can later connect real data)
    lane1 = random.randint(0, 10)
    lane2 = random.randint(0, 10)
    lane3 = random.randint(0, 10)

    total = lane1 + lane2 + lane3

    # Density
    if total < 5:
        density = "LOW"
        color = "🟢"
        signal_time = 10
    elif total < 10:
        density = "MEDIUM"
        color = "🟡"
        signal_time = 20
    else:
        density = "HIGH"
        color = "🔴"
        signal_time = 30

    # Save history
    st.session_state.data.append(total)

    with placeholder.container():
        # --- METRICS ---
        st.subheader("📊 Live Traffic Status")

        col1, col2, col3 = st.columns(3)
        col1.metric("Lane 1", lane1)
        col2.metric("Lane 2", lane2)
        col3.metric("Lane 3", lane3)

        st.markdown("---")

        col4, col5 = st.columns(2)

        col4.metric("Total Vehicles", total)
        col5.metric("Signal Time (sec)", signal_time)

        # --- TRAFFIC LIGHT ---
        st.markdown("### 🚦 Traffic Signal Status")
        st.markdown(f"## {color} {density} Traffic")

        st.markdown("---")

        # --- LINE GRAPH ---
        st.subheader("📈 Traffic Trend")
        df = pd.DataFrame(st.session_state.data, columns=["Vehicles"])
        st.line_chart(df)

        # --- BAR GRAPH (LANE COMPARISON) ---
        st.subheader("📊 Lane Comparison")
        lane_df = pd.DataFrame({
            "Lane": ["Lane 1", "Lane 2", "Lane 3"],
            "Vehicles": [lane1, lane2, lane3]
        })
        st.bar_chart(lane_df.set_index("Lane"))

    time.sleep(1)