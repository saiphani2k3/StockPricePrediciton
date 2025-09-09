"""
Data Sources Module
Handles all data fetching from different APIs and CSV files
"""

import streamlit as st
import pandas as pd
import numpy as np
import requests
import json
from datetime import datetime, date

START = "2010-01-01"
TODAY = date.today().strftime("%Y-%m-%d")

class DataSources:
    """Centralized data fetching for all supported APIs"""
    
    @staticmethod
    @st.cache_data
    def fetch_alpha_vantage_data(symbol, api_key):
        """Fetch stock data from Alpha Vantage API"""
        try:
            url = f"https://www.alphavantage.co/query"
            params = {
                'function': 'TIME_SERIES_DAILY',
                'symbol': symbol,
                'outputsize': 'full',
                'apikey': api_key,
                'datatype': 'json'
            }
            
            with st.spinner(f"🔄 Fetching data for {symbol} from Alpha Vantage..."):
                response = requests.get(url, params=params, timeout=30)
                data = response.json()
            
            # Check for API errors
            if "Error Message" in data:
                st.error(f"❌ API Error: {data['Error Message']}")
                if "Invalid API call" in data['Error Message']:
                    st.warning("💡 **Tip:** Alpha Vantage only supports US stocks and ADRs. Try selecting a different data source for international stocks.")
                return None
            
            if "Note" in data:
                st.error(f"❌ API Limit: {data['Note']}")
                st.info("⏰ Alpha Vantage free tier allows 25 requests/day. Please wait or upgrade your plan.")
                return None
            
            if "Time Series (Daily)" not in data:
                st.error(f"❌ No data found for symbol {symbol}")
                if any(symbol.endswith(ext) for ext in ['.NS', '.T', '.KS', '.SW', '.PA', '.SR']):
                    st.warning("🌍 **International Stock Detected:** Alpha Vantage doesn't support this exchange. Try Financial Modeling Prep or CSV upload instead.")
                return None
            
            # Parse the data
            time_series = data["Time Series (Daily)"]
            
            # Convert to DataFrame
            df_data = []
            for date_str, values in time_series.items():
                df_data.append({
                    'Date': datetime.strptime(date_str, '%Y-%m-%d'),
                    'Open': float(values['1. open']),
                    'High': float(values['2. high']),
                    'Low': float(values['3. low']),
                    'Close': float(values['4. close']),
                    'Volume': int(values['5. volume'])
                })
            
            df = pd.DataFrame(df_data)
            df = df.sort_values('Date').reset_index(drop=True)
            
            st.success(f"✅ Alpha Vantage: Loaded {len(df)} days of data for {symbol}")
            return df
            
        except Exception as e:
            st.error(f"❌ Alpha Vantage Error: {str(e)}")
            return None

    @staticmethod
    @st.cache_data
    def fetch_fmp_data(symbol, api_key):
        """Fetch stock data from Financial Modeling Prep API"""
        try:
            url = f"https://financialmodelingprep.com/api/v3/historical-price-full/{symbol}"
            params = {
                'apikey': api_key,
                'from': '2020-01-01',
                'to': TODAY
            }
            
            with st.spinner(f"🔄 Fetching data for {symbol} from Financial Modeling Prep..."):
                response = requests.get(url, params=params, timeout=30)
                data = response.json()
            
            # Check for API errors
            if "Error Message" in data:
                st.error(f"❌ API Error: {data['Error Message']}")
                return None
                
            if 'historical' not in data:
                st.error(f"❌ No historical data found for {symbol}")
                return None
            
            # Parse the data
            historical_data = data['historical']
            
            # Convert to DataFrame
            df_data = []
            for item in historical_data:
                df_data.append({
                    'Date': datetime.strptime(item['date'], '%Y-%m-%d'),
                    'Open': float(item['open']),
                    'High': float(item['high']),
                    'Low': float(item['low']),
                    'Close': float(item['close']),
                    'Volume': int(item['volume'])
                })
            
            df = pd.DataFrame(df_data)
            df = df.sort_values('Date').reset_index(drop=True)
            
            st.success(f"✅ Financial Modeling Prep: Loaded {len(df)} days of data for {symbol}")
            return df
            
        except Exception as e:
            st.error(f"❌ FMP Error: {str(e)}")
            return None

    @staticmethod
    @st.cache_data
    def fetch_fallback_data(symbol):
        """Try multiple fallback APIs"""
        # Try IEX Cloud
        try:
            url = f"https://cloud.iexapis.com/stable/stock/{symbol}/chart/2y"
            params = {'token': 'pk_test', 'format': 'json'}
            
            with st.spinner(f"🔄 Trying IEX Cloud for {symbol}..."):
                response = requests.get(url, params=params, timeout=20)
                data = response.json()
            
            if isinstance(data, list) and len(data) > 0:
                df_data = []
                for item in data:
                    if all(key in item for key in ['date', 'open', 'high', 'low', 'close', 'volume']):
                        if item['close']:  # Skip null values
                            df_data.append({
                                'Date': datetime.strptime(item['date'], '%Y-%m-%d'),
                                'Open': float(item['open']),
                                'High': float(item['high']),
                                'Low': float(item['low']),
                                'Close': float(item['close']),
                                'Volume': int(item['volume']) if item['volume'] else 0
                            })
                
                if df_data:
                    df = pd.DataFrame(df_data)
                    df = df.sort_values('Date').reset_index(drop=True)
                    st.success(f"✅ IEX Cloud Fallback: Loaded {len(df)} days of data for {symbol}")
                    return df
        except:
            pass
        
        return None

    @staticmethod
    def validate_csv_data(data):
        """Validate uploaded CSV data format"""
        required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
        missing_columns = [col for col in required_columns if col not in data.columns]
        
        if missing_columns:
            return False, f"Missing required columns: {missing_columns}"
        
        try:
            # Convert Date column to datetime
            data['Date'] = pd.to_datetime(data['Date'])
            return True, "CSV data is valid"
        except Exception as e:
            return False, f"Error processing CSV: {str(e)}"

    @staticmethod
    def get_compatible_stocks(data_source, all_stocks):
        """Filter stocks based on data source compatibility"""
        if "Alpha Vantage" in data_source:
            # Only show US stocks and ADRs (no .NS, .T, .KS, .SW, .PA, .SR extensions)
            compatible_stocks = {k: v for k, v in all_stocks.items() 
                               if not any(k.endswith(ext) for ext in ['.NS', '.T', '.KS', '.SW', '.PA', '.SR'])}
            return compatible_stocks, f"📊 Showing {len(compatible_stocks)} Alpha Vantage-compatible stocks (US + ADRs)"
        else:
            return all_stocks, "" 