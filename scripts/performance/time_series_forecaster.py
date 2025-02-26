import numpy as np
from statsmodels.tsa.holtwinters import ExponentialSmoothing
from sklearn.metrics import mean_squared_error

class ResourceForecaster:
    def __init__(self):
        self.models = {
            'cpu': None,
            'memory': None,
            'bandwidth': None
        }
        self.forecast_horizon = 24  # hours
        
    def train_models(self, historical_data):
        for resource_type, data in historical_data.items():
            model = ExponentialSmoothing(
                data,
                seasonal_periods=24,
                trend='add',
                seasonal='add'
            )
            self.models[resource_type] = model.fit()
    
    def forecast_resource_usage(self):
        forecasts = {}
        for resource_type, model in self.models.items():
            if model:
                forecast = model.forecast(self.forecast_horizon)
                confidence_intervals = model.get_prediction(
                    start=len(model.data),
                    end=len(model.data) + self.forecast_horizon
                ).conf_int()
                forecasts[resource_type] = {
                    'predictions': forecast,
                    'confidence_intervals': confidence_intervals
                }
        return forecasts 