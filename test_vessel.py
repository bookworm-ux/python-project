import pytest
from vessel_calc import VesselAnalyzer

def test_tce_calculation():
    # Setup a manual scenario
    analyzer = VesselAnalyzer(fuel_price_per_mt=600)
    mock_row = {
        'charter_rate_day': 20000,
        'voyage_days': 10,
        'fuel_cons_day': 10,
        'port_fees': 10000
    }
    # Expected: ((20000*10) - (10*10*600) - 10000) / 10 = 13000
    assert analyzer.calculate_tce(mock_row) == 13000.0