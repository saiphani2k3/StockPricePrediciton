"""
Stock Prophet - AI-Powered Financial Analytics Dashboard
Enhanced Visual Experience with Modern UI/UX
"""

import streamlit as st
import pandas as pd
import requests
from datetime import datetime, date, timedelta
import plotly.graph_objects as go
import plotly.express as px

# Import components
from components.data_sources import DataSources
from components.prediction_engine import PredictionEngine
from components.ui_components import UIComponents
from components.stock_data import POPULAR_STOCKS

def main():
    # Enhanced Custom CSS for modern, eye-catching layout with DARK THEME
    st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
    
    /* Global styling - DARK THEME */
    .main > div {
        font-family: 'Inter', sans-serif;
    }
    
    /* Hide Streamlit branding */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    
    /* Dark animated gradient background */
    .stApp {
        background: linear-gradient(-45deg, #1a1a2e, #16213e, #0f3460, #533483);
        background-size: 400% 400%;
        animation: gradientBG 15s ease infinite;
        min-height: 100vh;
    }
    
    @keyframes gradientBG {
        0% { background-position: 0% 50%; }
        50% { background-position: 100% 50%; }
        100% { background-position: 0% 50%; }
    }
    
    /* Main container overlay - DARK */
    .main .block-container {
        background: rgba(26, 26, 46, 0.95);
        backdrop-filter: blur(10px);
        border-radius: 20px;
        padding: 2rem;
        margin-top: 1rem;
        box-shadow: 0 20px 40px rgba(0,0,0,0.4);
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    
    /* Enhanced main header styling - DARK */
    .main-header {
        text-align: center;
        padding: 2rem 1rem;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 50%, #f093fb 100%);
        color: white;
        border-radius: 20px;
        margin-bottom: 2rem;
        box-shadow: 0 15px 35px rgba(102, 126, 234, 0.4);
        position: relative;
        overflow: hidden;
    }
    
    .main-header::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shine 3s infinite;
    }
    
    @keyframes shine {
        0% { left: -100%; }
        100% { left: 100%; }
    }
    
    .main-header h1 {
        font-size: 3rem !important;
        font-weight: 700 !important;
        margin: 0 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
        background: linear-gradient(45deg, #fff, #f0f8ff);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
    }
    
    .main-header p {
        font-size: 1.2rem !important;
        margin: 0.5rem 0 0 0 !important;
        opacity: 0.95;
        font-weight: 400;
    }
    
    /* Floating icons */
    .header-icon {
        position: absolute;
        font-size: 2rem;
        opacity: 0.3;
        animation: float 6s ease-in-out infinite;
    }
    
    .icon-1 { top: 20%; left: 10%; animation-delay: 0s; }
    .icon-2 { top: 30%; right: 15%; animation-delay: 2s; }
    .icon-3 { bottom: 20%; left: 20%; animation-delay: 4s; }
    .icon-4 { bottom: 30%; right: 10%; animation-delay: 1s; }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px) rotate(0deg); }
        33% { transform: translateY(-20px) rotate(5deg); }
        66% { transform: translateY(-10px) rotate(-5deg); }
    }
    
    /* Enhanced section styling - DARK */
    .section-header {
        background: linear-gradient(90deg, #667eea, #764ba2);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip: text;
        font-weight: 600 !important;
        font-size: 1.3rem !important;
        margin-bottom: 1rem !important;
        display: flex;
        align-items: center;
        gap: 0.5rem;
    }
    
    /* Card styling with dark glassmorphism */
    .section-card {
        background: rgba(40, 40, 60, 0.8);
        backdrop-filter: blur(10px);
        border: 1px solid rgba(255, 255, 255, 0.1);
        border-radius: 15px;
        padding: 1.5rem;
        margin-bottom: 1rem;
        box-shadow: 0 8px 32px rgba(0, 0, 0, 0.3);
        transition: all 0.3s ease;
    }
    
    .section-card:hover {
        transform: translateY(-5px);
        box-shadow: 0 12px 40px rgba(0, 0, 0, 0.4);
        border-color: rgba(102, 126, 234, 0.3);
    }
    
    /* Enhanced button styling - DARK */
    .stButton > button {
        background: linear-gradient(45deg, #667eea, #764ba2) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.5rem 1rem !important;
        font-weight: 500 !important;
        transition: all 0.3s ease !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6) !important;
        background: linear-gradient(45deg, #764ba2, #667eea) !important;
    }
    
    /* Dark theme for text and elements */
    .stMarkdown, .stText, p, span, div {
        color: #e0e6ed !important;
    }
    
    h1, h2, h3, h4, h5, h6 {
        color: #f0f5fa !important;
    }
    
    /* Success/Info/Warning styling - DARK */
    .stAlert {
        border-radius: 12px !important;
        border: none !important;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3) !important;
        background: rgba(40, 40, 60, 0.9) !important;
        color: #e0e6ed !important;
    }
    
    /* COMPREHENSIVE Selectbox styling - DARK BACKGROUNDS */
    .stSelectbox label {
        color: #f0f5fa !important;
        font-weight: 500 !important;
    }
    
    /* Force ALL dropdown elements to dark background */
    .stSelectbox > div > div,
    .stSelectbox > div > div > div,
    .stSelectbox div[data-baseweb="select"],
    .stSelectbox div[data-baseweb="select"] > div,
    .stSelectbox div[role="listbox"],
    .stSelectbox div[role="option"],
    [data-baseweb="select"] > div,
    [data-baseweb="popover"] > div,
    [data-baseweb="menu"] > ul,
    [data-baseweb="menu"] li {
        background: rgba(30, 30, 50, 0.95) !important;
        background-color: rgba(30, 30, 50, 0.95) !important;
        color: #f0f5fa !important;
        border-radius: 8px !important;
    }
    
    /* Selectbox main container */
    .stSelectbox > div > div {
        background: rgba(30, 30, 50, 0.95) !important;
        background-color: rgba(30, 30, 50, 0.95) !important;
        color: #f0f5fa !important;
        border: 2px solid rgba(102, 126, 234, 0.4) !important;
        border-radius: 10px !important;
        transition: all 0.3s ease !important;
    }
    
    /* Dropdown menu when opened */
    .stSelectbox div[data-baseweb="select"] > div {
        background: rgba(30, 30, 50, 0.98) !important;
        background-color: rgba(30, 30, 50, 0.98) !important;
        color: #f0f5fa !important;
        border: 2px solid rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Individual dropdown options */
    .stSelectbox div[role="option"] {
        background: rgba(30, 30, 50, 0.98) !important;
        background-color: rgba(30, 30, 50, 0.98) !important;
        color: #f0f5fa !important;
        padding: 8px 12px !important;
    }
    
    /* Hover effect for options */
    .stSelectbox div[role="option"]:hover {
        background: rgba(102, 126, 234, 0.4) !important;
        background-color: rgba(102, 126, 234, 0.4) !important;
        color: #ffffff !important;
    }
    
    /* Focus states */
    .stSelectbox > div > div:focus-within {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.3) !important;
    }
    
    /* Selectbox arrow and icons */
    .stSelectbox svg {
        fill: #f0f5fa !important;
    }
    
    /* Override any white backgrounds with !important */
    .stSelectbox * {
        background-color: rgba(30, 30, 50, 0.95) !important;
    }
    
    /* Specific overrides for stubborn white backgrounds */
    div[data-baseweb="select"] {
        background: rgba(30, 30, 50, 0.95) !important;
        background-color: rgba(30, 30, 50, 0.95) !important;
    }
    
    div[data-baseweb="popover"] {
        background: rgba(30, 30, 50, 0.95) !important;
        background-color: rgba(30, 30, 50, 0.95) !important;
    }
    
    /* Nuclear option - override ALL white backgrounds in selectboxes */
    .stSelectbox div,
    .stSelectbox span,
    .stSelectbox ul,
    .stSelectbox li {
        background: rgba(30, 30, 50, 0.95) !important;
        background-color: rgba(30, 30, 50, 0.95) !important;
        color: #f0f5fa !important;
    }
    
    /* Target Streamlit's internal dropdown classes */
    [class*="css-"][class*="select"],
    [class*="css-"][class*="dropdown"] {
        background: rgba(30, 30, 50, 0.95) !important;
        background-color: rgba(30, 30, 50, 0.95) !important;
        color: #f0f5fa !important;
    }
    
    /* Force any element with white background inside selectbox to dark */
    .stSelectbox [style*="background-color: white"],
    .stSelectbox [style*="background-color: #ffffff"],
    .stSelectbox [style*="background-color: rgb(255, 255, 255)"],
    .stSelectbox [style*="background: white"],
    .stSelectbox [style*="background: #ffffff"] {
        background: rgba(30, 30, 50, 0.95) !important;
        background-color: rgba(30, 30, 50, 0.95) !important;
        color: #f0f5fa !important;
    }
    
    /* FORCE BLACK BACKGROUND - Most aggressive approach */
    .stSelectbox div[role="listbox"],
    .stSelectbox div[data-baseweb="popover"],
    .stSelectbox div[data-baseweb="popover"] > div,
    .stSelectbox ul[role="listbox"],
    .stSelectbox li[role="option"] {
        background: #000000 !important;
        background-color: #000000 !important;
        color: #ffffff !important;
        border: 1px solid #667eea !important;
    }
    
    /* Target the dropdown container specifically */
    div[data-baseweb="popover"][data-popper-placement] {
        background: #000000 !important;
        background-color: #000000 !important;
    }
    
    div[data-baseweb="popover"][data-popper-placement] > div {
        background: #000000 !important;
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    /* Override any remaining white elements */
    [data-baseweb="popover"] * {
        background: #000000 !important;
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    /* Additional targeting for dropdown menu elements */
    div[aria-expanded="true"] + div,
    div[aria-expanded="true"] + div > div,
    div[aria-expanded="true"] + div ul,
    div[aria-expanded="true"] + div li {
        background: #000000 !important;
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    /* Target all possible dropdown variations */
    .css-* div[role="listbox"],
    .css-* ul[role="listbox"],
    .css-* li[role="option"],
    [class*="css-"] div[role="listbox"],
    [class*="css-"] ul[role="listbox"],
    [class*="css-"] li[role="option"] {
        background: #000000 !important;
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    /* Nuclear option - force ALL children of selectbox */
    .stSelectbox * {
        background: #000000 !important;
        background-color: #000000 !important;
        color: #ffffff !important;
    }
    
    /* Text inputs - DARK */
    .stTextInput > div > div > input {
        background: rgba(30, 30, 50, 0.95) !important;
        color: #f0f5fa !important;
        border: 2px solid rgba(102, 126, 234, 0.4) !important;
        border-radius: 10px !important;
    }
    
    .stTextInput > div > div > input:focus {
        border-color: #667eea !important;
        box-shadow: 0 0 0 3px rgba(102, 126, 234, 0.3) !important;
    }
    
    .stTextInput label {
        color: #f0f5fa !important;
        font-weight: 500 !important;
    }
    
    /* Number input styling */
    .stNumberInput > div > div > input {
        background: rgba(30, 30, 50, 0.95) !important;
        color: #f0f5fa !important;
        border: 2px solid rgba(102, 126, 234, 0.4) !important;
        border-radius: 10px !important;
    }
    
    .stNumberInput label {
        color: #f0f5fa !important;
        font-weight: 500 !important;
    }
    
    /* File uploader - DARK */
    .stFileUploader > div {
        background: rgba(30, 30, 50, 0.95) !important;
        border: 2px dashed rgba(102, 126, 234, 0.5) !important;
        border-radius: 10px !important;
        color: #f0f5fa !important;
    }
    
    .stFileUploader label {
        color: #f0f5fa !important;
        font-weight: 500 !important;
    }
    
    /* Metrics styling - DARK (NO WHITE BOXES) */
    .stMetric {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
        padding: 0 !important;
    }
    
    .stMetric > div {
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }
    
    /* File uploader - DARK */
    .stFileUploader > div {
        background: rgba(40, 40, 60, 0.9) !important;
        border: 2px dashed rgba(102, 126, 234, 0.5) !important;
        border-radius: 10px !important;
        color: #e0e6ed !important;
    }
    
    /* Results section enhancement - DARK */
    .results-section {
        background: linear-gradient(135deg, rgba(102, 126, 234, 0.15), rgba(40, 40, 60, 0.9));
        padding: 2rem;
        border-radius: 20px;
        border: 2px solid rgba(102, 126, 234, 0.3);
        margin-top: 2rem;
        backdrop-filter: blur(10px);
        box-shadow: 0 15px 35px rgba(0, 0, 0, 0.4);
    }
    
    /* Dataframe styling - DARK */
    .stDataFrame {
        background: rgba(40, 40, 60, 0.9) !important;
        border-radius: 10px !important;
    }
    
    /* Enhanced typography - DARK */
    h1, h2, h3 {
        font-family: 'Inter', sans-serif !important;
        font-weight: 600 !important;
        color: #f0f5fa !important;
    }
    
    /* Pulse animation for important elements */
    .pulse {
        animation: pulse 2s infinite;
    }
    
    @keyframes pulse {
        0% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0.7); }
        70% { box-shadow: 0 0 0 10px rgba(102, 126, 234, 0); }
        100% { box-shadow: 0 0 0 0 rgba(102, 126, 234, 0); }
    }
    
    /* Enhanced Professional Styling */
    .main > div {
        padding-top: 2rem !important;
        padding-bottom: 2rem !important;
    }
    
    /* Professional headers and typography */
    h1, h2, h3 {
        font-family: 'Inter', -apple-system, BlinkMacSystemFont, sans-serif !important;
        font-weight: 600 !important;
        line-height: 1.2 !important;
        letter-spacing: -0.025em !important;
    }
    
    /* Enhanced container styling */
    .block-container {
        padding: 2rem 3rem !important;
        max-width: 1400px !important;
        margin: 0 auto !important;
    }
    
    /* Professional button styling */
    .stButton > button {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
        color: white !important;
        border: none !important;
        border-radius: 12px !important;
        padding: 0.75rem 2rem !important;
        font-weight: 600 !important;
        font-family: 'Inter', sans-serif !important;
        font-size: 1rem !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
        transition: all 0.3s cubic-bezier(0.4, 0, 0.2, 1) !important;
        text-transform: none !important;
        letter-spacing: 0.025em !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(102, 126, 234, 0.6) !important;
        background: linear-gradient(135deg, #5a67d8 0%, #6b46c1 100%) !important;
    }
    
    .stButton > button:active {
        transform: translateY(0px) !important;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4) !important;
    }
    
    /* Professional metrics styling */
    [data-testid="metric-container"] {
        background: linear-gradient(135deg, rgba(30, 30, 50, 0.8) 0%, rgba(40, 45, 70, 0.6) 100%) !important;
        border: 1px solid rgba(102, 126, 234, 0.2) !important;
        border-radius: 16px !important;
        padding: 1.5rem !important;
        backdrop-filter: blur(10px) !important;
        transition: all 0.3s ease !important;
    }
    
    [data-testid="metric-container"]:hover {
        border-color: rgba(102, 126, 234, 0.4) !important;
        transform: translateY(-2px) !important;
        box-shadow: 0 8px 25px rgba(0, 0, 0, 0.3) !important;
    }
    
    /* Enhanced dividers */
    .element-container hr {
        margin: 3rem 0 !important;
        border: none !important;
        height: 1px !important;
        background: linear-gradient(90deg, transparent, rgba(102, 126, 234, 0.3), transparent) !important;
    }
    
    /* Professional spacing and layout */
    .element-container {
        margin-bottom: 1.5rem !important;
    }
    
    /* Enhanced sidebar styling */
    .css-1d391kg {
        background: linear-gradient(180deg, rgba(15, 23, 42, 0.95) 0%, rgba(30, 41, 59, 0.9) 100%) !important;
        backdrop-filter: blur(10px) !important;
    }
    
    /* Professional column styling */
    [data-testid="column"] {
        padding: 0 1rem !important;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Enhanced main header with floating icons
    st.markdown('''
    <div class="main-header">
        <div class="header-icon icon-1">📊</div>
        <div class="header-icon icon-2">🚀</div>
        <div class="header-icon icon-3">💎</div>
        <div class="header-icon icon-4">🔮</div>
        <h1>🌟 Stock Prophet AI 🌟</h1>
    </div>
    ''', unsafe_allow_html=True)
    
    # Initialize session state
    if 'data_source' not in st.session_state:
        st.session_state.data_source = "🔵 Alpha Vantage"
    if 'selected_stock' not in st.session_state:
        st.session_state.selected_stock = "AAPL"
    if 'prediction_years' not in st.session_state:
        st.session_state.prediction_years = 1
    if 'show_results' not in st.session_state:
        st.session_state.show_results = False
    
    # Three horizontal sections with enhanced styling
    col1, col2, col3 = st.columns(3)
    
    # Section 1: Data Source
    with col1:
        st.markdown('''
        <div class="section-card">
            <h3 class="section-header">🌐 Data Source</h3>
        </div>
        ''', unsafe_allow_html=True)
        
        data_source = st.selectbox(
            "🔗 Choose your data provider:",
            ["🌟 Alpha Vantage API", "💼 Financial Modeling Prep", "📊 Upload CSV File"],
            index=["🌟 Alpha Vantage API", "💼 Financial Modeling Prep", "📊 Upload CSV File"].index(st.session_state.data_source) if st.session_state.data_source in ["🌟 Alpha Vantage API", "💼 Financial Modeling Prep", "📊 Upload CSV File"] else 0,
            key="data_source_select"
        )
        st.session_state.data_source = data_source
        
        # API key input based on selection
        api_key = None
        uploaded_file = None
        
        if data_source == "🌟 Alpha Vantage API":
            st.info("🇺🇸 **US Markets Focus**\n⚡ 25 requests/day (free tier)")
            api_key = st.text_input("🔐 API Key:", type="password", help="Get your free key from alphavantage.co")
            
        elif data_source == "💼 Financial Modeling Prep":
            st.info("🌍 **Global Markets Coverage**\n⚡ 250 requests/day (free tier)")
            api_key = st.text_input("🔐 API Key:", value="demo", help="Use 'demo' for testing")
            
        else:  # CSV Upload
            st.info("📈 **Your Own Data**\n♾️ Unlimited usage")
            uploaded_file = st.file_uploader("📁 Upload CSV file", type=['csv'])
    
    # Section 2: Stock Selection
    with col2:
        st.markdown('''
        <div class="section-card">
            <h3 class="section-header">🎯 Stock Selection</h3>
        </div>
        ''', unsafe_allow_html=True)
        
        if data_source != "📊 Upload CSV File":
            # Stock selection dropdown
            from components.stock_data import POPULAR_STOCKS
            
            # Create searchable dropdown
            stock_options = []
            stock_mapping = {}
            for symbol, company in POPULAR_STOCKS.items():
                display_text = f"{symbol} - {company}"
                stock_options.append(display_text)
                stock_mapping[display_text] = symbol
            
            # Find current selection
            current_stock = st.session_state.selected_stock
            current_index = 0
            for i, option in enumerate(stock_options):
                if current_stock in option:
                    current_index = i
                    break
            
            selected_option = st.selectbox(
                "🔍 Search & select company:",
                stock_options,
                index=current_index,
                help="💡 Type to search companies globally"
            )
            
            if selected_option:
                selected_stock = stock_mapping[selected_option]
                st.session_state.selected_stock = selected_stock
                
                # Check compatibility with selected API
                if data_source == "🌟 Alpha Vantage API":
                    # Alpha Vantage only supports US stocks and ADRs
                    if any(selected_stock.endswith(ext) for ext in ['.NS', '.T', '.KS', '.AS', '.DE', '.L', '.PA', '.SW']):
                        st.warning(f"⚠️ **{selected_stock}** requires Financial Modeling Prep API")
                        st.info("💡 Switch to FMP or select a US stock for Alpha Vantage")
                    else:
                        st.success(f"✅ {selected_stock} Ready!")
                else:
                    st.success(f"✅ {selected_stock} Ready!")
            
            # Popular stocks (horizontal quick select) - US stocks that work with both APIs
            st.markdown("**⚡ Quick Select:**")
            popular_stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "NFLX", "UBER"]
            
            cols = st.columns(3)
            for i, stock in enumerate(popular_stocks):
                with cols[i % 3]:
                    if st.button(f"🏢 {stock}", key=f"pop_{stock}", use_container_width=True):
                        st.session_state.selected_stock = stock
                        st.rerun()
        else:
            st.info("📊 Using uploaded CSV data")
    
    # Section 3: Time Frame Settings
    with col3:
        st.markdown('''
        <div class="section-card">
            <h3 class="section-header">⏰ Time Frame & Settings</h3>
        </div>
        ''', unsafe_allow_html=True)
        
        # Time frame selection with both months and years
        time_frame_type = st.selectbox(
            "📅 Investment Horizon:",
            ["⚡ Short Term (Months)", "📈 Long Term (Years)"],
            help="🎯 Choose your investment timeframe"
        )
        
        if time_frame_type == "⚡ Short Term (Months)":
            prediction_months = st.selectbox(
                "🗓️ Prediction Period:",
                [1, 2, 3, 6, 9, 12, 18, 24],
                index=0,
                help="📊 Months to predict into the future"
            )
            prediction_years = prediction_months / 12.0
            st.markdown(f"**🔮 Forecasting {prediction_months} month{'s' if prediction_months > 1 else ''} ahead**")
        else:
            prediction_years = st.selectbox(
                "🗓️ Prediction Period:",
                [1, 2, 3, 4, 5],
                index=0,
                help="📊 Years to predict into the future"
            )
            prediction_months = prediction_years * 12
            st.markdown(f"**🔮 Forecasting {prediction_years} year{'s' if prediction_years > 1 else ''} ahead**")
        
        st.session_state.prediction_years = prediction_years
        
        # Model settings
        model_type = st.selectbox(
            "🤖 AI Model:",
            ["🧠 Prophet AI (Recommended)", "📊 Linear Trend", "📈 Exponential Growth"],
            help="🔬 Choose prediction algorithm"
        )
        
        confidence_level = st.slider(
            "🎯 Confidence Level:",
            min_value=0.80, max_value=0.99, value=0.95, step=0.01,
            help="📈 Statistical confidence level"
        )
    
    # Enhanced Predict Button Section
    st.markdown("---")
    st.markdown('''
    <div style="text-align: center; margin: 2rem 0;">
        <h2 style="color: #667eea; font-weight: 700;">Launch Prediction Engine</h2>
    </div>
    ''', unsafe_allow_html=True)
    
    # Check if ready to predict
    ready_to_predict = False
    if data_source == "📊 Upload CSV File":
        ready_to_predict = uploaded_file is not None
    else:
        ready_to_predict = (api_key and api_key.strip() and 
                          st.session_state.selected_stock and st.session_state.selected_stock.strip())
    
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if ready_to_predict:
            if st.button("🔮 ✨ PREDICT FUTURE PRICE ✨ 🔮", type="primary", use_container_width=True):
                st.session_state.show_results = True
                st.rerun()
            st.success("🎯 All systems ready for prediction!")
        else:
            st.button("🔮 ✨ PREDICT FUTURE PRICE ✨ 🔮", type="primary", use_container_width=True, disabled=True)
            if data_source == "📊 Upload CSV File":
                st.warning("📋 Please upload a CSV file to continue")
            else:
                st.warning("🔧 Please configure API key and select a stock")
    
    # Enhanced Results Section (only show when predict button is clicked)
    if st.session_state.get('show_results', False):
        st.markdown('''
        <div class="results-section">
            <div style="text-align: center; margin-bottom: 2rem;">
                <h1 style="color: #667eea; font-weight: 700; margin: 0;">
                    📊 ✨ AI Analysis Results ✨ 📊
                </h1>
                <p style="color: #666; font-size: 1.2rem; margin: 0.5rem 0;">
                    🤖 Powered by Advanced Machine Learning Algorithms
                </p>
            </div>
        </div>
        ''', unsafe_allow_html=True)
        
        # Get the selected stock from session state
        current_stock = st.session_state.selected_stock
        
        if data_source == "📊 Upload CSV File":
            if uploaded_file is not None:
                try:
                    data = pd.read_csv(uploaded_file)
                    # Validate CSV format
                    required_columns = ['Date', 'Open', 'High', 'Low', 'Close', 'Volume']
                    if all(col in data.columns for col in required_columns):
                        data['Date'] = pd.to_datetime(data['Date'])
                        data = data.sort_values('Date')
                        st.success(f"🎉 CSV data loaded successfully! ({len(data)} records)")
                    else:
                        st.error(f"❌ CSV must contain columns: {required_columns}")
                        st.session_state.show_results = False
                        st.rerun()
                except Exception as e:
                    st.error(f"❌ Error reading CSV: {str(e)}")
                    st.session_state.show_results = False
                    st.rerun()
            else:
                st.warning("📋 Please upload a CSV file first.")
                st.session_state.show_results = False
                st.rerun()
        else:
            # Check API key
            if not api_key:
                st.warning(f"⚠️ Please enter your {data_source.split()[0]} API key.")
                st.session_state.show_results = False
                st.rerun()
            
            # Fetch data from API
            with st.spinner(f'🌐 Fetching market data for {current_stock}...'):
                data = fetch_data_from_api(data_source, current_stock, api_key)
            
            if data is None or data.empty:
                st.error(f"❌ Could not fetch data for {current_stock}. Please check the symbol and try again.")
                st.session_state.show_results = False
                st.rerun()
            
            st.success(f"🎉 Market data fetched successfully! ({len(data)} records)")
        
        # Display basic metrics
        if data is not None and not data.empty:
            display_stock_metrics(data, current_stock)
            
            # Run Prophet prediction
            perform_stock_prediction(data, prediction_years, current_stock)
        
        st.markdown('</div>', unsafe_allow_html=True)


def fetch_data_from_api(api_type, stock, api_key):
    """Fetch data from API"""
    try:
        if api_type == "🌟 Alpha Vantage API":
            return DataSources.fetch_alpha_vantage_data(stock, api_key)
        elif api_type == "💼 Financial Modeling Prep":
            return DataSources.fetch_fmp_data(stock, api_key)
    except Exception as e:
        st.error(f"❌ API Error: {str(e)}")
    return None

def display_stock_metrics(data, stock_symbol):
    """Display enhanced stock metrics with beautiful styling"""
    current_price = data['Close'].iloc[-1]
    prev_price = data['Close'].iloc[-2] if len(data) > 1 else current_price
    price_change = current_price - prev_price
    pct_change = (price_change / prev_price) * 100 if prev_price != 0 else 0
    
    # Enhanced metrics display header
    st.markdown('''
    <div style="text-align: center; margin: 2rem 0 1rem 0;">
        <h3 style="color: #667eea; font-weight: 600;">📊 Real-Time Market Metrics</h3>
    </div>
    ''', unsafe_allow_html=True)
    
    # Metrics display without white boxes
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="💰 Current Price",
            value=f"${current_price:.2f}",
            delta=f"{price_change:.2f} ({pct_change:.1f}%)"
        )
    
    with col2:
        st.metric(
            label="📊 Volume",
            value=f"{data['Volume'].iloc[-1]:,.0f}" if 'Volume' in data.columns else "N/A"
        )
    
    with col3:
        st.metric(
            label="📈 52W High",
            value=f"${data['High'].max():.2f}"
        )
    
    with col4:
        st.metric(
            label="📉 52W Low",
            value=f"${data['Low'].min():.2f}"
        )
    
    # Add Price Chart
    st.markdown('''
    <div style="margin: 2rem 0 1rem 0;">
        <h3 style="color: #667eea; font-weight: 600; text-align: center;">
            📈 ✨ Price Chart ✨
        </h3>
    </div>
    ''', unsafe_allow_html=True)
    
    # Create and display the price chart
    fig = go.Figure()
    
    # Add price line
    fig.add_trace(go.Scatter(
        x=data['Date'],
        y=data['Close'],
        mode='lines',
        name='Close Price',
        line=dict(color='#667eea', width=2),
        hovertemplate='<b>%{x}</b><br>Price: $%{y:.2f}<extra></extra>'
    ))
    
    # Update layout
    fig.update_layout(
        title=dict(
            text=f"📈 {stock_symbol} Stock Price",
            x=0.5,
            font=dict(size=20, color='#667eea', family='Inter', weight=600)
        ),
        xaxis=dict(
            title=dict(text='Date', font=dict(size=14, color='#c0c5ca')),
            gridcolor='rgba(255,255,255,0.15)',
            color='#e0e6ed',
            showgrid=True
        ),
        yaxis=dict(
            title=dict(text='Price ($)', font=dict(size=14, color='#c0c5ca')),
            gridcolor='rgba(255,255,255,0.15)',
            color='#e0e6ed',
            showgrid=True
        ),
        height=400,
        showlegend=False,
        plot_bgcolor='rgba(25, 42, 86, 0.8)',  # Dark blue background
        paper_bgcolor='rgba(0,0,0,0)',
        font=dict(color='#e0e6ed', family='Inter, -apple-system, BlinkMacSystemFont, sans-serif'),
        margin=dict(l=40, r=40, t=80, b=40),
        hoverlabel=dict(
            bgcolor='rgba(30, 30, 50, 0.95)',
            font_color='white',
            bordercolor='#667eea'
        ),
        hovermode='x unified'
    )
    
    # Display the chart
    st.plotly_chart(fig, use_container_width=True)
    
    # Enhanced recent data section
    st.markdown('''
    <div style="margin: 2rem 0 1rem 0;">
        <h3 style="color: #667eea; font-weight: 600; text-align: center;">
            📋 ✨ Recent Price History ✨
        </h3>
    </div>
    ''', unsafe_allow_html=True)
    
    # Style the dataframe
    recent_data = data.tail(10).copy()
    recent_data.index = range(len(recent_data))
    st.dataframe(
        recent_data[['Date', 'Open', 'High', 'Low', 'Close', 'Volume']],
        use_container_width=True,
        hide_index=True
    )

def perform_stock_prediction(data, n_years, stock_symbol):
    """Perform enhanced stock prediction using Prophet with beautiful styling"""
    try:
        st.markdown('''
        <div style="text-align: center; margin: 2rem 0;">
            <h2 style="color: #667eea; font-weight: 700;">
                🔮 ✨ AI Prediction Engine ✨ 🔮
            </h2>
            <p style="color: #e0e6ed; font-size: 1.1rem;">
                🧠 Unleashing the power of Facebook Prophet Algorithm
            </p>
        </div>
        ''', unsafe_allow_html=True)
        
        with st.spinner('🤖 Training advanced AI model... Please wait'):
            # Prepare data for Prophet
            df_train = PredictionEngine.prepare_data_for_prophet(data)
            
            # Train model (fixed function call)
            model = PredictionEngine.train_prophet_model(df_train)
            
            if model:
                # Generate forecast - ensure period_days is always an integer
                period_days = int(n_years * 365)
                forecast = PredictionEngine.generate_forecast(model, period_days)
                
                if forecast is not None:
                    # Extract prediction metrics
                    metrics = PredictionEngine.extract_prediction_metrics(data, forecast)
                    
                    # Display prediction results with enhanced styling
                    st.markdown('''
                    <div style="text-align: center; margin: 2rem 0 1rem 0; padding: 1rem; background: linear-gradient(135deg, rgba(76, 175, 80, 0.2), rgba(139, 195, 74, 0.2)); border-radius: 15px; border: 2px solid rgba(76, 175, 80, 0.4);">
                        <h3 style="color: #4CAF50; font-weight: 600; margin: 0;">
                            🎉 ✅ Prediction Successfully Completed! ✅ 🎉
                        </h3>
                        <p style="color: #e0e6ed; margin: 0.5rem 0 0 0;">
                            🚀 AI has analyzed market patterns and generated future insights
                        </p>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    # Enhanced prediction metrics without white boxes
                    st.markdown('''
                    <div style="text-align: center; margin: 1.5rem 0 1rem 0;">
                        <h3 style="color: #667eea; font-weight: 600;">📊 Prediction Metrics Dashboard</h3>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    col1, col2, col3, col4 = st.columns(4)
                    
                    with col1:
                        st.metric(
                            "📈 Current Price", 
                            f"${data['Close'].iloc[-1]:.2f}",
                            f"{((data['Close'].iloc[-1] - data['Close'].iloc[-2]) / data['Close'].iloc[-2] * 100):+.2f}%"
                        )
                    
                    with col2:
                        predicted_price = forecast['yhat'].iloc[-1]
                        current_price = data['Close'].iloc[-1]
                        change_pct = (predicted_price - current_price) / current_price * 100
                        
                        # Calculate display timeframe
                        if n_years < 1:
                            months = int(n_years * 12)
                            timeframe_text = f"{months}M"
                        else:
                            years = int(n_years) if n_years == int(n_years) else f"{n_years:.1f}"
                            timeframe_text = f"{years}Y"
                        
                        st.metric(
                            f"🎯 {timeframe_text} Prediction", 
                            f"${predicted_price:.2f}",
                            f"{change_pct:+.2f}%"
                        )
                    
                    with col3:
                        if metrics and 'confidence_upper' in metrics:
                            st.metric(
                                "📊 Upper Bound",
                                f"${metrics['confidence_upper']:.2f}",
                                "95% Confidence"
                            )
                        else:
                            st.metric("🔍 Accuracy", "High", "AI Confidence")
                    
                    with col4:
                        if metrics and 'confidence_lower' in metrics:
                            st.metric(
                                "📉 Lower Bound",
                                f"${metrics['confidence_lower']:.2f}",
                                "95% Confidence"
                            )
                        else:
                            trend = "📈 Bullish" if change_pct > 0 else "📉 Bearish"
                            st.metric("📊 Trend", trend, f"{abs(change_pct):.1f}%")
                    
                    # Enhanced chart section
                    st.markdown('''
                    <div style="text-align: center; margin: 2rem 0 1rem 0;">
                        <h3 style="color: #667eea; font-weight: 600;">
                            📈 ✨ Interactive Prediction Chart ✨ 📈
                        </h3>
                        <p style="color: #e0e6ed; font-size: 1rem;">
                            📊 Visualizing historical data and AI-powered future predictions
                        </p>
                    </div>
                    ''', unsafe_allow_html=True)
                    
                    # Render interactive chart
                    UIComponents.render_interactive_chart(data, stock_symbol)
                    
                else:
                    st.error("❌ Failed to generate forecast. Please try again.")
            else:
                st.error("❌ Failed to train model. Please check your data.")
                
    except Exception as e:
        st.error(f"❌ Prediction failed: {str(e)}")
        st.info("💡 Please try selecting a different stock or timeframe.")

if __name__ == "__main__":
    # Page Configuration
    st.set_page_config(
        page_title="Stock Prophet",
        page_icon="📈",
        layout="wide",
        initial_sidebar_state="collapsed"
    )
    
    main() 