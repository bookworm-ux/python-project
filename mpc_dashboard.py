import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. SETUP DATA (This defines 'df')
data = {
    'vessel_name': ['MPC Itajai', 'MPC Hamburg', 'MPC Elbe', 'MPC Green', 'MPC Atlantic'],
    'teu_capacity': [2800, 3500, 1700, 2100, 4200],
    'charter_rate_day': [25000, 31000, 18000, 22000, 38000],
    'voyage_days': [15, 12, 20, 14, 10],
    'fuel_cons_day': [35.5, 42.0, 22.8, 28.5, 52.0], 
    'port_fees': [50000, 65000, 30000, 40000, 80000]
}
df = pd.DataFrame(data)

# 2. STREAMLIT UI
st.set_page_config(page_title="MPC Fleet Monitor", layout="wide")
st.title("🚢 MPC Fleet Profitability Monitor")
st.write("Real-time Time Charter Equivalent (TCE) Analysis")

# 3. SIDEBAR CONTROLS
st.sidebar.header("Market Variables")
fuel_price = st.sidebar.slider("Current Fuel Price (USD/MT)", 400, 1000, 650)
benchmark = st.sidebar.number_input("Profit Benchmark (USD/Day)", value=15000)

# 4. CALCULATION LOGIC
df['daily_tce_usd'] = df.apply(lambda row: ((row['charter_rate_day'] * row['voyage_days']) - 
                      (row['fuel_cons_day'] * row['voyage_days'] * fuel_price) - 
                      row['port_fees']) / row['voyage_days'], axis=1).round(0)

# 5. VISUALS
col1, col2 = st.columns(2)

with col1:
    st.subheader("Daily Profit by Vessel")
    colors = ['#2ecc71' if x > benchmark else '#e74c3c' for x in df['daily_tce_usd']]
    fig, ax = plt.subplots()
    ax.bar(df['vessel_name'], df['daily_tce_usd'], color=colors)
    ax.axhline(y=benchmark, color='black', linestyle='--', label='Target')
    plt.xticks(rotation=45)
    st.pyplot(fig)

with col2:
    st.subheader("Fleet Data Summary")
    st.dataframe(df[['vessel_name', 'teu_capacity', 'daily_tce_usd']])

st.info(f"Analysis based on fuel price of ${fuel_price}/MT. Red bars indicate ships below the ${benchmark} profit target.")