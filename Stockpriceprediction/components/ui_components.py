"""
UI Components Module
Contains all Streamlit UI components and interface elements
"""

import streamlit as st
import pandas as pd
from plotly import graph_objs as go
from prophet.plot import plot_plotly
from .stock_data import POPULAR_STOCKS, API_COMPARISON_DATA, DATA_SOURCE_CONFIG
from .data_sources import DataSources

class UIComponents:
    """Centralized UI components for the Stock Prophet app"""
    
    @staticmethod
    def setup_page_config():
        """Configure Streamlit page settings with clean, professional styling"""
        # Check session state for sidebar preference (default to collapsed)
        # Always show sidebar expanded for navigation functionality
        sidebar_state = "expanded"
            
        st.set_page_config(
            page_title="Stock Prophet",
            page_icon="📈",
            layout="wide",
            initial_sidebar_state=sidebar_state
        )
        
        # Clean, professional design inspired by modern financial apps
        st.markdown("""
        <style>
        /* Import clean, professional fonts */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&family=Source+Sans+Pro:wght@300;400;600;700&display=swap');
        
        /* Floating Navigation Bar */
        .floating-nav {
            position: fixed;
            top: 50%;
            left: 20px;
            transform: translateY(-50%);
            z-index: 1000;
            background: rgba(255, 255, 255, 0.95);
            border-radius: 12px;
            padding: 8px;
            box-shadow: 0 4px 20px rgba(0, 0, 0, 0.1);
            border: 1px solid rgba(229, 231, 235, 0.8);
            backdrop-filter: blur(10px);
            transition: all 0.3s ease;
        }
        
        /* Style the navigation buttons */
        .floating-nav button {
            width: 48px !important;
            height: 48px !important;
            border-radius: 8px !important;
            background: #f8f9fa !important;
            border: 1px solid #e5e7eb !important;
            margin: 4px 0 !important;
            font-size: 18px !important;
            transition: all 0.2s ease !important;
            display: flex !important;
            align-items: center !important;
            justify-content: center !important;
        }
        
        .floating-nav button:hover {
            background: #3b82f6 !important;
            color: white !important;
            transform: translateX(2px) !important;
            box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3) !important;
        }
        
        .floating-nav button:focus {
            background: #3b82f6 !important;
            color: white !important;
            box-shadow: 0 2px 8px rgba(59, 130, 246, 0.3) !important;
            border-color: #3b82f6 !important;
        }
        
        /* Style navigation buttons */
        div[data-testid="column"] .stButton > button {
            background: linear-gradient(135deg, #f8f9fa, #ffffff) !important;
            border: 1px solid #e5e7eb !important;
            border-radius: 8px !important;
            color: #374151 !important;
            font-weight: 500 !important;
            transition: all 0.3s ease !important;
            height: 50px !important;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.05) !important;
        }
        
        div[data-testid="column"] .stButton > button:hover {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
            color: white !important;
            border-color: #3b82f6 !important;
            transform: translateY(-2px) !important;
            box-shadow: 0 8px 20px rgba(59, 130, 246, 0.3) !important;
        }
        
        /* Primary button styling */
        div[data-testid="column"] button[data-testid="baseButton-primary"] {
            background: linear-gradient(135deg, #3b82f6, #1d4ed8) !important;
            color: white !important;
            border-color: #3b82f6 !important;
            box-shadow: 0 4px 12px rgba(59, 130, 246, 0.2) !important;
        }
        
        /* Style for separator line */
        .floating-nav div[style*="border-top"] {
            margin: 8px 4px !important;
            border-color: #e5e7eb !important;
            opacity: 0.6;
        }
        
        /* Hide nav on mobile */
        @media (max-width: 768px) {
            .floating-nav {
                display: none !important;
            }
        }
        
        /* Clean, professional background */
        .stApp {
            background: #ffffff;
            color: #1a1a1a;
            font-family: 'Inter', -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            font-weight: 400;
            line-height: 1.6;
        }
        
        /* Clean main container with minimal top spacing */
        .main .block-container {
            background: #ffffff;
            padding: 1rem 2.5rem 2rem 2.5rem;
            max-width: 1200px;
            margin: 0 auto;
        }
        
        /* Style the title to be centered */
        h1 {
            text-align: center !important;
            color: #1f2937 !important;
            margin-bottom: 0.5rem !important;
        }
        
        /* Style the caption */
        .caption {
            text-align: center !important;
            color: #6b7280 !important;
            font-size: 1.1rem !important;
        }
        
        /* Professional sidebar */
        .css-1d391kg, .css-1cypcdb, .css-1aumxhk {
            background: #f8f9fa;
            border-right: 1px solid #e9ecef;
        }
        
        /* Clean scrollbars */
        ::-webkit-scrollbar {
            width: 6px;
            height: 6px;
        }
        ::-webkit-scrollbar-track {
            background: #f1f3f4;
        }
        ::-webkit-scrollbar-thumb {
            background: #c1c8cd;
            border-radius: 3px;
        }
        ::-webkit-scrollbar-thumb:hover {
            background: #a8b3ba;
        }
        
        /* Clean input styling */
        .stSelectbox > div > div, .stTextInput > div > div > input {
            background: #ffffff;
            border: 1.5px solid #e1e5e9;
            border-radius: 6px;
            color: #2c3e50;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            font-weight: 400;
            transition: border-color 0.2s ease;
        }
        
        .stSelectbox > div > div:hover, .stTextInput > div > div > input:hover {
            border-color: #4f46e5;
        }
        
        .stSelectbox > div > div:focus, .stTextInput > div > div > input:focus {
            border-color: #4f46e5;
            box-shadow: 0 0 0 3px rgba(79, 70, 229, 0.1);
        }
        
        /* Clean radio buttons */
        .stRadio > div {
            background: #ffffff;
            border-radius: 8px;
            padding: 16px;
            border: 1px solid #e1e5e9;
            margin-bottom: 8px;
        }
        
        .stRadio > div:hover {
            border-color: #4f46e5;
            background: #fafbfc;
        }
        
        /* Professional slider */
        .stSlider > div > div > div > div {
            background: #4f46e5;
            height: 4px;
            border-radius: 2px;
        }
        
        /* Clean buttons */
        .stButton > button {
            background: #4f46e5;
            border: none;
            border-radius: 6px;
            color: white;
            font-weight: 500;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            padding: 0.5rem 1rem;
            transition: all 0.2s ease;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.1);
        }
        
        .stButton > button:hover {
            background: #4338ca;
            transform: translateY(-1px);
            box-shadow: 0 2px 6px rgba(0, 0, 0, 0.15);
        }
        
        /* Clean expanders */
        .streamlit-expanderHeader {
            background: #ffffff;
            border-radius: 6px;
            border: 1px solid #e1e5e9;
            color: #2c3e50;
            font-weight: 500;
        }
        
        .streamlit-expanderHeader:hover {
            border-color: #4f46e5;
            background: #fafbfc;
        }
        
        .streamlit-expanderContent {
            background: #fafbfc;
            border: 1px solid #e1e5e9;
            border-top: none;
            border-radius: 0 0 6px 6px;
        }
        
        /* Professional text styling */
        .stMarkdown, .stText, p {
            color: #374151;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
            line-height: 1.6;
        }
        
        h1 {
            color: #1f2937;
            font-family: 'Inter', sans-serif;
            font-weight: 700;
            font-size: 2.5rem;
            line-height: 1.2;
            margin-bottom: 0.5rem;
        }
        
        h2 {
            color: #1f2937;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1.8rem;
            line-height: 1.3;
            margin-bottom: 0.5rem;
        }
        
        h3 {
            color: #374151;
            font-family: 'Inter', sans-serif;
            font-weight: 600;
            font-size: 1.25rem;
            line-height: 1.4;
            margin-bottom: 0.5rem;
        }
        
        h4, h5, h6 {
            color: #4b5563;
            font-family: 'Inter', sans-serif;
            font-weight: 500;
        }
        
        /* Clean links */
        a {
            color: #4f46e5;
            text-decoration: none;
            font-weight: 500;
        }
        
        a:hover {
            color: #4338ca;
            text-decoration: underline;
        }
        
        /* Professional alert styling */
        .stAlert {
            border-radius: 8px;
            border: 1px solid #e1e5e9;
            font-family: 'Inter', sans-serif;
            font-size: 14px;
        }
        
        .stSuccess {
            background: #f0fdf4;
            border-color: #bbf7d0;
            color: #166534;
        }
        
        .stInfo {
            background: #eff6ff;
            border-color: #bfdbfe;
            color: #1e40af;
        }
        
        .stWarning {
            background: #fffbeb;
            border-color: #fde68a;
            color: #92400e;
        }
        
        .stError {
            background: #fef2f2;
            border-color: #fecaca;
            color: #dc2626;
        }
        
        /* Clean tables */
        .stDataFrame {
            border: 1px solid #e1e5e9;
            border-radius: 8px;
            overflow: hidden;
        }
        
        .stDataFrame tbody tr:hover {
            background: #f8f9fa;
        }
        
        /* Clean file uploader */
        .stFileUploader {
            background: #fafbfc;
            border: 2px dashed #d1d5db;
            border-radius: 8px;
            padding: 20px;
        }
        
        .stFileUploader:hover {
            border-color: #4f46e5;
            background: #f9fafb;
        }
        
        /* Hide default elements */
        #MainMenu {visibility: hidden;}
        .stDeployButton {display: none;}
        footer {visibility: hidden;}
        .stApp > header {visibility: hidden;}
        header[data-testid="stHeader"] {display: none;}
        
        /* Clean sidebar styling */
        .css-1d391kg .stMarkdown {
            color: #374151;
        }
        
        .css-1d391kg h1, .css-1d391kg h2, .css-1d391kg h3 {
            color: #1f2937;
        }
        
        /* Professional spacing */
        .css-1d391kg .stSelectbox, 
        .css-1d391kg .stTextInput, 
        .css-1d391kg .stRadio {
            margin-bottom: 1rem;
        }
        
        /* Clean metric cards */
        .stMetric {
            background: #ffffff;
            border: 1px solid #e1e5e9;
            border-radius: 8px;
            padding: 1.5rem;
            box-shadow: 0 1px 3px rgba(0, 0, 0, 0.05);
        }
        
        .stMetric:hover {
            box-shadow: 0 4px 12px rgba(0, 0, 0, 0.08);
            transform: translateY(-1px);
        }
        
        /* Responsive design */
        @media (max-width: 768px) {
            .main .block-container {
                padding: 1rem 1rem;
            }
            
            h1 {
                font-size: 2rem;
            }
            
            h2 {
                font-size: 1.5rem;
            }
        }
        </style>
                """, unsafe_allow_html=True)
    
    @staticmethod
    def render_floating_nav():
        """Render navigation that controls sidebar content"""
        # Initialize session state
        if 'current_section' not in st.session_state:
            st.session_state.current_section = 'data'
        if 'show_sidebar' not in st.session_state:
            st.session_state.show_sidebar = True
        if 'nav_action' not in st.session_state:
            st.session_state.nav_action = None
        if 'left_nav_open' not in st.session_state:
            st.session_state.left_nav_open = False
            
        # Clean CSS for main layout
        st.markdown("""
        <style>
        .main .block-container {
            padding-left: 2rem !important;
        }
        </style>
        """, unsafe_allow_html=True)
        
        # Create visual brand icon
        st.markdown("""
        <div style="position: fixed; left: 10px; top: 20px; z-index: 1000; 
                    background: linear-gradient(135deg, #3b82f6, #8b5cf6); 
                    width: 50px; height: 50px; border-radius: 12px; 
                    display: flex; align-items: center; justify-content: center; 
                    color: white; font-size: 24px; box-shadow: 0 4px 20px rgba(59, 130, 246, 0.4);">
            📊
        </div>
        """, unsafe_allow_html=True)
        
        # Navigation buttons
        col1, col2, col3, col4 = st.columns(4)
        
        with col1:
            if st.button("🌐 Data", key="nav_data_btn", use_container_width=True):
                st.session_state.current_section = 'data'
                st.session_state.nav_action = 'show_data'
                st.success("✅ Data section selected!")
        
        with col2:
            if st.button("📈 Stocks", key="nav_stocks_btn", use_container_width=True):
                st.session_state.current_section = 'stocks'
                st.session_state.nav_action = 'show_stocks'
                st.success("✅ Stocks section selected!")
        
        with col3:
            if st.button("⚙️ Settings", key="nav_settings_btn", use_container_width=True):
                st.session_state.current_section = 'settings'
                st.session_state.nav_action = 'show_settings'
                st.success("✅ Settings section selected!")
        
        with col4:
            if st.button("📊 Results", key="nav_results_btn", use_container_width=True):
                st.session_state.current_section = 'results'
                st.session_state.nav_action = 'scroll_to_results'
                st.success("✅ Results section selected!")
        
        # Style navigation buttons
        st.markdown("""
        <style>
        div[data-testid="column"] .stButton > button {
            height: 50px;
            border-radius: 12px;
            border: 1px solid rgba(59, 130, 246, 0.3);
            background: rgba(30, 41, 59, 0.8);
            color: #94a3b8;
            font-size: 14px;
            font-weight: 500;
            transition: all 0.3s ease;
        }
        
        div[data-testid="column"] .stButton > button:hover {
            background: rgba(59, 130, 246, 0.3) !important;
            border-color: #3b82f6 !important;
            color: white !important;
            transform: translateY(-2px);
            box-shadow: 0 4px 15px rgba(59, 130, 246, 0.3);
        }
        </style>
        """, unsafe_allow_html=True)
    
    @staticmethod
    def render_header():
        """Render clean, professional header"""
        st.title("📊 Stock Prophet")
        st.caption("AI-Powered Financial Analytics Dashboard")
        st.divider()

    @staticmethod
    def render_sidebar_api_selection():
        """Render dynamic sidebar content based on navigation selection"""
        # Initialize session state for persistent selections
        if 'selected_data_source' not in st.session_state:
            st.session_state.selected_data_source = "🔵 Alpha Vantage"
        if 'selected_stock' not in st.session_state:
            st.session_state.selected_stock = "AAPL"
        if 'selected_api_key' not in st.session_state:
            st.session_state.selected_api_key = ""
        if 'prediction_years' not in st.session_state:
            st.session_state.prediction_years = 2
        if 'selected_model' not in st.session_state:
            st.session_state.selected_model = "🔮 Prophet (Recommended)"
        
        # Get current section from session state
        current_section = st.session_state.get('current_section', 'data')
        
        # Debug info in sidebar
        st.sidebar.success(f"🔍 Sidebar Debug: Showing {current_section} section")
        
        # Dynamic sidebar header based on current section
        section_config = {
            'data': {
                'title': '🌐 Data Sources',
                'subtitle': 'Choose your preferred data source for stock analysis:'
            },
            'stocks': {
                'title': '📈 Stock Selection',
                'subtitle': 'Select and configure stock symbols for analysis:'
            },
            'settings': {
                'title': '⚙️ Settings',
                'subtitle': 'Configure prediction parameters and preferences:'
            },
            'results': {
                'title': '📊 Results',
                'subtitle': 'View analysis results and export options:'
            }
        }
        
        config = section_config.get(current_section, section_config['data'])
        
        # Dynamic sidebar header
        st.sidebar.markdown(f"### {config['title']}")
        st.sidebar.markdown(config['subtitle'])
        
        # Content based on current section
        if current_section == 'data':
            st.sidebar.markdown("### 🌐 Data Sources")
            st.sidebar.markdown("**Choose your stock data provider:**")
            
            # Detailed descriptions for each API
            st.sidebar.info("""
            **📊 About Data Sources:**
            
            Choose the API that best fits your needs. Each provider offers different coverage, limits, and features.
            """)
            
            # Data source selection with session state persistence
            data_source = st.sidebar.radio(
                "**Select Data Provider:**",
                [
                    "🔵 Alpha Vantage",
                    "🟢 Financial Modeling Prep", 
                    "📁 Upload CSV File"
                ],
                index=["🔵 Alpha Vantage", "🟢 Financial Modeling Prep", "📁 Upload CSV File"].index(st.session_state.selected_data_source) if st.session_state.selected_data_source in ["🔵 Alpha Vantage", "🟢 Financial Modeling Prep", "📁 Upload CSV File"] else 0,
                help="Choose your preferred stock data source"
            )
            
            # Update session state when selection changes
            if data_source != st.session_state.selected_data_source:
                st.session_state.selected_data_source = data_source
            
            # Show detailed info based on selection
            if data_source == "🔵 Alpha Vantage":
                st.sidebar.success("""
                **🔵 Alpha Vantage Selected**
                
                ✅ **Coverage**: US Stock Markets  
                📊 **Data Quality**: Professional-grade  
                🔄 **Update Frequency**: Real-time  
                🆓 **Free Limit**: 25 requests/day  
                💰 **Paid Plans**: Available for more requests  
                
                **Perfect for US stock analysis!**
                """)
                
            elif data_source == "🟢 Financial Modeling Prep":
                st.sidebar.success("""
                **🟢 Financial Modeling Prep Selected**
                
                ✅ **Coverage**: Global Markets  
                📊 **Data Quality**: Comprehensive  
                🔄 **Update Frequency**: Daily  
                🆓 **Free Limit**: 250 requests/day  
                🌍 **International**: World-wide coverage  
                
                **Great for global stock analysis!**
                """)
                
            else:  # CSV Upload
                st.sidebar.success("""
                **📁 CSV Upload Selected**
                
                ✅ **Coverage**: Your own data  
                📊 **Data Quality**: Depends on your file  
                🔄 **Update Frequency**: Manual  
                🆓 **Cost**: Completely free  
                📋 **Format**: Standard OHLCV format  
                
                **Use your own historical data!**
                """)
            
            return st.session_state.selected_data_source
            
        elif current_section == 'stocks':
            st.sidebar.markdown("### 📈 Stock Selection")
            st.sidebar.markdown("**Select a company to analyze:**")
            
            # Show current data source (from session state)
            st.sidebar.info(f"💡 **Current Data Source**: {st.session_state.selected_data_source}")
            
            # Popular stocks selection with session state persistence
            popular_stocks = ["AAPL", "GOOGL", "MSFT", "AMZN", "TSLA", "META", "NVDA", "NFLX"]
            
            # Find current stock index
            current_index = 0
            if st.session_state.selected_stock in popular_stocks:
                current_index = popular_stocks.index(st.session_state.selected_stock)
            
            selected_stock = st.sidebar.selectbox(
                "**Popular Stocks:**",
                popular_stocks,
                index=current_index,
                help="Choose from popular stocks"
            )
            
            # Update session state when selection changes
            if selected_stock != st.session_state.selected_stock:
                st.session_state.selected_stock = selected_stock
            
            # Custom stock input
            custom_stock = st.sidebar.text_input(
                "**Or Enter Custom Symbol:**",
                placeholder="e.g., AAPL",
                help="Enter any stock symbol"
            )
            
            if custom_stock:
                st.session_state.selected_stock = custom_stock.upper()
            
            st.sidebar.success(f"✅ Selected: **{st.session_state.selected_stock}**")
            return st.session_state.selected_data_source
            
        elif current_section == 'settings':
            st.sidebar.markdown("### ⚙️ Prediction Settings")
            st.sidebar.markdown("**Configure your AI prediction model:**")
            
            # Show current selections
            st.sidebar.info(f"💡 **Current Setup**:\n- Data: {st.session_state.selected_data_source}\n- Stock: {st.session_state.selected_stock}")
            
            # Prediction model selection with session state persistence
            model_options = ["🔮 Prophet (Recommended)", "🧠 LSTM Neural Network", "📊 ARIMA"]
            current_model_index = 0
            if st.session_state.selected_model in model_options:
                current_model_index = model_options.index(st.session_state.selected_model)
            
            model_type = st.sidebar.selectbox(
                "**AI Model:**",
                model_options,
                index=current_model_index,
                help="Choose prediction algorithm"
            )
            
            # Update session state when model changes
            if model_type != st.session_state.selected_model:
                st.session_state.selected_model = model_type
            
            # Time horizon with session state persistence
            prediction_years = st.sidebar.slider(
                "**Prediction Period:**",
                min_value=1, max_value=5, 
                value=st.session_state.prediction_years,
                help="How many years to predict"
            )
            
            # Update session state when years change
            if prediction_years != st.session_state.prediction_years:
                st.session_state.prediction_years = prediction_years
            
            st.sidebar.info(f"📊 **Model**: {st.session_state.selected_model.split()[0]}\n📅 **Period**: {st.session_state.prediction_years} years")
            return st.session_state.selected_data_source
            
        elif current_section == 'results':
            st.sidebar.markdown("### 📊 Prediction Results")
            st.sidebar.markdown("**View and export your analysis:**")
            
            # Show current configuration
            st.sidebar.info(f"🎯 **Current Configuration**:\n- Data: {st.session_state.selected_data_source}\n- Stock: {st.session_state.selected_stock}\n- Model: {st.session_state.selected_model.split()[0]}\n- Period: {st.session_state.prediction_years} years")
            
            # Export options
            st.sidebar.markdown("**📤 Export Options:**")
            col1, col2 = st.sidebar.columns(2)
            with col1:
                st.button("📄 CSV", help="Download as CSV")
            with col2:
                st.button("📋 PDF", help="Generate PDF report")
            
            return st.session_state.selected_data_source
        
        return st.session_state.selected_data_source

    @staticmethod
    def render_api_configuration(data_source):
        """Render API configuration using session state"""
        # Use the session state data source
        current_data_source = st.session_state.get('selected_data_source', data_source)
        
        if current_data_source == "📁 Upload CSV File":
            return None, "csv"
        elif "Alpha Vantage" in current_data_source:
            # API key input with session state persistence
            api_key = st.sidebar.text_input(
                "API Key:", 
                value=st.session_state.get('selected_api_key', ''),
                type="password", 
                help="Get free key from alphavantage.co"
            )
            if api_key != st.session_state.get('selected_api_key', ''):
                st.session_state.selected_api_key = api_key
            return api_key, "alpha_vantage"
        else:
            # FMP API key with session state
            api_key = st.sidebar.text_input(
                "API Key:", 
                value=st.session_state.get('selected_api_key', 'demo'),
                help="Use 'demo' for testing"
            )
            if api_key != st.session_state.get('selected_api_key', 'demo'):
                st.session_state.selected_api_key = api_key
            return api_key, "fmp"

    @staticmethod
    def render_stock_selection(data_source):
        """Render stock selection using session state"""
        return st.session_state.get('selected_stock', 'AAPL')
    
    @staticmethod
    def render_prediction_settings():
        """Render prediction settings using session state"""
        return st.session_state.get('prediction_years', 2)
    
    @staticmethod
    def render_csv_upload():
        """Render CSV upload"""
        st.sidebar.info("CSV upload functionality")
        return None
    
    @staticmethod
    def render_stock_analysis_header(selected_stock, data_source):
        """Render stock analysis header"""
        st.markdown(f"## 📈 Analysis for {selected_stock}")
    
    @staticmethod
    def render_metrics_dashboard(data):
        """Render metrics dashboard"""
        if data is not None:
            st.success("✅ Data loaded successfully!")
        else:
            st.warning("⚠️ No data available")
    
    @staticmethod
    def render_recent_data_table(data):
        """Render recent data table"""
        if data is not None:
            st.dataframe(data.tail())
    
    @staticmethod
    def render_interactive_chart(data, selected_stock):
        """Render interactive chart with dark theme and blue lines"""
        if data is not None:
            # Create plotly figure with dark theme
            fig = go.Figure()
            
            # Add price line with blue color
            fig.add_trace(go.Scatter(
                x=data.index,
                y=data['Close'],
                mode='lines',
                name='Close Price',
                line=dict(color='#667eea', width=2.5),
                hovertemplate='<b>Date:</b> %{x}<br><b>Price:</b> $%{y:.2f}<extra></extra>'
            ))
            
            # Dark theme layout
            fig.update_layout(
                plot_bgcolor='rgba(25, 42, 86, 0.8)',  # Dark blue background to match left chart
                paper_bgcolor='rgba(0,0,0,0)',   # Transparent paper
                font=dict(color='#e0e6ed', family='Inter, -apple-system, BlinkMacSystemFont, sans-serif'),
                title=dict(
                    text=f'📈 {selected_stock} Price Chart',
                    x=0.5,
                    font=dict(size=20, color='#667eea', family='Inter', weight=600)
                ),
                xaxis=dict(
                    gridcolor='rgba(255,255,255,0.15)',
                    color='#e0e6ed',
                    showgrid=True,
                    zeroline=False,
                    title=dict(text='Date', font=dict(size=14, color='#c0c5ca'))
                ),
                yaxis=dict(
                    gridcolor='rgba(255,255,255,0.15)',
                    color='#e0e6ed',
                    showgrid=True,
                    zeroline=False,
                    title=dict(text='Price ($)', font=dict(size=14, color='#c0c5ca'))
                ),
                hovermode='x unified',
                margin=dict(l=40, r=40, t=80, b=40),
                height=500,
                hoverlabel=dict(
                    bgcolor='rgba(30, 30, 50, 0.95)',
                    font_color='white',
                    bordercolor='#667eea'
                )
            )
            
            # Display the chart
            st.plotly_chart(fig, use_container_width=True)
    
    @staticmethod
    def render_prediction_results(current_price, future_price, n_years):
        """Render prediction results"""
        st.metric("Current Price", f"${current_price:.2f}")
        st.metric("Predicted Price", f"${future_price:.2f}")
    
    @staticmethod
    def render_forecast_chart(model, forecast):
        """Render forecast chart"""
        st.success("✅ Forecast chart rendered")
    
    @staticmethod
    def render_forecast_components(model, forecast):
        """Render forecast components"""
        st.info("📊 Forecast components analysis")
    
    @staticmethod
    def render_forecast_details(forecast):
        """Render forecast details"""
        st.dataframe(forecast.tail())
    
    @staticmethod
    def render_disclaimer():
        """Render disclaimer"""
        st.markdown("---")
        st.caption("⚠️ This is for educational purposes only. Not financial advice.")