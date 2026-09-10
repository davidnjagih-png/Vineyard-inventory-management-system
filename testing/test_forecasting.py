import pytest
import pandas as pd
from logic.forecasting import Forecasting

def test_forecast_predict_next_month():
    data = pd.DataFrame({
        "month": ["Jan", "Feb", "Mar"],
        "sales": [100, 150, 200]
    })
    forecast = Forecasting(data)
    prediction = forecast.predict_next_month()
    assert prediction > 0
    assert isinstance(prediction, (int, float))

def test_forecast_with_seasonal_variation():
    data = pd.DataFrame({
        "month": ["Oct", "Nov", "Dec"],
        "sales": [120, 130, 300]
    })
    forecast = Forecasting(data)
    prediction = forecast.predict_next_month()
    assert prediction >= 130

def test_inventory_recommendations():
    data = pd.DataFrame({
        "month": ["Jan", "Feb", "Mar"],
        "sales": [80, 90, 100]
    })
    forecast = Forecasting(data)
    recommendations = forecast.recommend_inventory()
    assert "reorder" in recommendations or "maintain" in recommendations
