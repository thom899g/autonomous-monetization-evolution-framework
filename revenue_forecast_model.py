from typing import Dict, Optional
import logging
from dataclasses import dataclass
import numpy as np

logger = logging.getLogger(__name__)

@dataclass
class ForecastResult:
    predicted_revenue: float
    confidence_interval: Dict[str, float]

class RevenueForecastModel:
    def __init__(self):
        self.models = {}  # Key: model_id, Value: trained model
        
    def train_forecast_model(self, historical_data: pd.DataFrame) -> str:
        """Trains a revenue forecast model and returns its ID."""
        if not historical_data:
            raise ValueError("No historical data provided for training")
            
        # Simulated training
        X = historical_data[['price', 'demand', 'competition']]
        y = historical_data['revenue']
        
        # Split data
        from sklearn.model_selection import train_test_split
        X_train, X_test, y_train, y_test = train_test_split(X, y)
        
        # Train model
        from sklearn.ensemble import RandomForestRegressor
        model = RandomForestRegressor()
        model.fit(X_train, y_train)
        
        model_id = f"RF_{len(self.models) + 1}"
        self.models[model_id] = model
        
        logger.info(f"Trained forecast model with ID: {model_id}")
        return model_id

    def make_forecast(self, model_id: str, input_data: Dict[str, float]) -> ForecastResult:
        """Makes a revenue forecast using the specified model."""
        if model_id not in self.models:
            raise KeyError(f"Model {model_id} does not exist")
            
        try:
            # Prepare input
            data = np.array([[
                input_data.get('price', 100),
                input_data.get('demand', 500),
                input_data.get('competition', 30)
            ]])
            
            # Make prediction
            prediction =