"""
Prediction Engine Module
Handles Prophet model training and forecasting logic
"""

import streamlit as st
import pandas as pd
from prophet import Prophet

class PredictionEngine:
    """Centralized prediction engine using Facebook Prophet"""
    
    @staticmethod
    def prepare_data_for_prophet(data):
        """Prepare data for Prophet model training"""
        df_train = data[['Date', 'Close']].copy()
        df_train = df_train.rename(columns={"Date": "ds", "Close": "y"})
        df_train = df_train.dropna()
        
        if len(df_train) < 30:
            st.error("❌ Insufficient data for prediction. Need at least 30 data points.")
            st.stop()
        
        return df_train

    @staticmethod
    def train_prophet_model(df_train):
        """Train Prophet model with progress indicator"""
        with st.spinner("🧠 Training Prophet model... This may take a moment."):
            try:
                m = Prophet(
                    daily_seasonality=False,
                    weekly_seasonality=True,
                    yearly_seasonality=True,
                    seasonality_mode='additive'
                )
                m.fit(df_train)
                
                st.success("✅ Model training completed!")
                return m
                
            except Exception as e:
                st.error(f"❌ Model training failed: {str(e)}")
                st.stop()

    @staticmethod
    def generate_forecast(model, period_days):
        """Generate forecast for specified period"""
        try:
            future = model.make_future_dataframe(periods=period_days)
            forecast = model.predict(future)
            return forecast
            
        except Exception as e:
            st.error(f"❌ Forecast generation failed: {str(e)}")
            st.stop()

    @staticmethod
    def extract_prediction_metrics(data, forecast):
        """Extract key prediction metrics"""
        current_price = data['Close'].iloc[-1]
        future_price = forecast['yhat'].iloc[-1]
        
        return {
            'current_price': current_price,
            'future_price': future_price,
            'price_change': future_price - current_price,
            'price_change_pct': ((future_price - current_price) / current_price) * 100
        } 