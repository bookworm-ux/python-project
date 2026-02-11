import pandas as pd

class VesselAnalyzer:
    def __init__(self, fuel_price_per_mt: float):
        self.fuel_price = fuel_price_per_mt

    def calculate_tce(self, row) -> float:
        """
        Calculates the Time Charter Equivalent (Daily Profit).
        """
        total_revenue = row['charter_rate_day'] * row['voyage_days']
        total_fuel_cost = (row['fuel_cons_day'] * row['voyage_days']) * self.fuel_price
        net_profit = total_revenue - total_fuel_cost - row['port_fees']
        
        return round(net_profit / row['voyage_days'], 2)

# Mock Data: Imagine this coming from their Azure SQL Database
data = {
    'vessel_name': ['MPC Itajai', 'MPC Hamburg', 'MPC Elbe'],
    'teu_capacity': [2800, 3500, 1700],
    'charter_rate_day': [25000, 31000, 18000],
    'voyage_days': [15, 12, 20],
    'fuel_cons_day': [35.5, 42.0, 22.8], # Metric Tons per day
    'port_fees': [50000, 65000, 30000]
}

df = pd.DataFrame(data)
analyzer = VesselAnalyzer(fuel_price_per_mt=650.0) # Current bunker price

# Apply the automation
df['daily_tce_usd'] = df.apply(analyzer.calculate_tce, axis=1)

# Flagging underperforming assets (Profitability Automation)
benchmark = 15000
df['status'] = df['daily_tce_usd'].apply(lambda x: 'PROFITABLE' if x > benchmark else 'REVIEW REQUIRED')

print(df[['vessel_name', 'daily_tce_usd', 'status']])