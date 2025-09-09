"""
Stock Data Module
Contains all stock listings and related data constants
"""

# All stocks organized alphabetically for better UX
POPULAR_STOCKS = {
    # 🇺🇸 US Stocks - Available on both Alpha Vantage and FMP
    'AAPL': '🇺🇸 Apple Inc.',
    'ADBE': '🇺🇸 Adobe Inc.',
    'AMC': '🇺🇸 AMC Entertainment',
    'AMZN': '🇺🇸 Amazon.com Inc.',
    'AMT': '🇺🇸 American Tower Corp.',
    'ATVI': '🇺🇸 Activision Blizzard',
    'BA': '🇺🇸 Boeing Company',
    'BABA': '🇨🇳 Alibaba Group (ADR)',
    'BAC': '🇺🇸 Bank of America',
    'BB': '🇺🇸 BlackBerry Limited',
    'BIDU': '🇨🇳 Baidu Inc. (ADR)',
    'C': '🇺🇸 Citigroup Inc.',
    'CAT': '🇺🇸 Caterpillar Inc.',
    'CCI': '🇺🇸 Crown Castle Inc.',
    'COIN': '🇺🇸 Coinbase Global Inc.',
    'COST': '🇺🇸 Costco Wholesale',
    'CRM': '🇺🇸 Salesforce Inc.',
    'CVX': '🇺🇸 Chevron Corporation',
    'DIS': '🇺🇸 Walt Disney Company',
    'EA': '🇺🇸 Electronic Arts Inc.',
    'EBAY': '🇺🇸 eBay Inc.',
    'ETSY': '🇺🇸 Etsy Inc.',
    'F': '🇺🇸 Ford Motor Company',
    'GE': '🇺🇸 General Electric',
    'GME': '🇺🇸 GameStop Corp.',
    'GOOGL': '🇺🇸 Alphabet Inc. (Google)',
    'GS': '🇺🇸 Goldman Sachs Group',
    'HD': '🇺🇸 Home Depot Inc.',
    'HDB': '🇮🇳 HDFC Bank (ADR)',
    'IBN': '🇮🇳 ICICI Bank (ADR)',
    'INFY': '🇮🇳 Infosys Limited (ADR)',
    'ITUB': '🇧🇷 Itaú Unibanco (ADR)',
    'JD': '🇨🇳 JD.com Inc. (ADR)',
    'JNJ': '🇺🇸 Johnson & Johnson',
    'JPM': '🇺🇸 JPMorgan Chase & Co.',
    'KO': '🇺🇸 Coca-Cola Company',
    'LCID': '🇺🇸 Lucid Group Inc.',
    'LI': '🇨🇳 Li Auto Inc. (ADR)',
    'LMT': '🇺🇸 Lockheed Martin',
    'LYFT': '🇺🇸 Lyft Inc.',
    'MA': '🇺🇸 Mastercard Inc.',
    'MCD': '🇺🇸 McDonald\'s Corporation',
    'META': '🇺🇸 Meta Platforms (Facebook)',
    'MMYT': '🇮🇳 MakeMyTrip Limited (ADR)',
    'MS': '🇺🇸 Morgan Stanley',
    'MSFT': '🇺🇸 Microsoft Corporation',
    'MSTR': '🇺🇸 MicroStrategy Inc.',
    'NFLX': '🇺🇸 Netflix Inc.',
    'NIO': '🇨🇳 NIO Inc. (ADR)',
    'NKE': '🇺🇸 Nike Inc.',
    'NOC': '🇺🇸 Northrop Grumman',
    'NOW': '🇺🇸 ServiceNow Inc.',
    'NVO': '🇩🇰 Novo Nordisk (ADR)',
    'NVDA': '🇺🇸 NVIDIA Corporation',
    'ORCL': '🇺🇸 Oracle Corporation',
    'PDD': '🇨🇳 PDD Holdings/Temu (ADR)',
    'PEP': '🇺🇸 PepsiCo Inc.',
    'PG': '🇺🇸 Procter & Gamble',
    'PINS': '🇺🇸 Pinterest Inc.',
    'PLD': '🇺🇸 Prologis Inc.',
    'PLTR': '🇺🇸 Palantir Technologies',
    'PYPL': '🇺🇸 PayPal Holdings',
    'RACE': '🇮🇹 Ferrari N.V. (ADR)',
    'RBLX': '🇺🇸 Roblox Corporation',
    'RDY': '🇮🇳 Dr. Reddys Labs (ADR)',
    'RIVN': '🇺🇸 Rivian Automotive',
    'RTX': '🇺🇸 Raytheon Technologies',
    'RY': '🇨🇦 Royal Bank of Canada (ADR)',
    'SAP': '🇩🇪 SAP SE (ADR)',
    'SBUX': '🇺🇸 Starbucks Corporation',
    'SHEL': '🇬🇧 Shell plc (ADR)',
    'SHOP': '🇨🇦 Shopify Inc.',
    'SIFY': '🇮🇳 Sify Technologies (ADR)',
    'SNAP': '🇺🇸 Snap Inc.',
    'SNOW': '🇺🇸 Snowflake Inc.',
    'SPOT': '🇺🇸 Spotify Technology',
    'SQ': '🇺🇸 Block Inc. (Square)',
    'TGT': '🇺🇸 Target Corporation',
    'TSM': '🇹🇼 Taiwan Semi (ADR)',
    'TSLA': '🇺🇸 Tesla Inc.',
    'TTWO': '🇺🇸 Take-Two Interactive',
    'TWTR': '🇺🇸 Twitter Inc.',
    'UBER': '🇺🇸 Uber Technologies',
    'UL': '🇬🇧 Unilever PLC (ADR)',
    'UNH': '🇺🇸 UnitedHealth Group',
    'V': '🇺🇸 Visa Inc.',
    'VALE': '🇧🇷 Vale S.A. (ADR)',
    'WFC': '🇺🇸 Wells Fargo & Company',
    'WIT': '🇮🇳 Wipro Limited (ADR)',
    'WMT': '🇺🇸 Walmart Inc.',
    'WNS': '🇮🇳 WNS Holdings (ADR)',
    'XOM': '🇺🇸 Exxon Mobil Corporation',
    'XPEV': '🇨🇳 XPeng Inc. (ADR)',
    'ZM': '🇺🇸 Zoom Video Communications',
    
    # 🌍 International Stocks - Available ONLY on FMP (will show warning for Alpha Vantage users)
    'ASML.AS': '🇳🇱 ASML Holding',
    'BMW.DE': '🇩🇪 BMW AG',
    'BP.L': '🇬🇧 BP p.l.c.',
    'DAI.DE': '🇩🇪 Mercedes-Benz Group',
    'MC.PA': '🇫🇷 LVMH (Louis Vuitton)',
    'NESN.SW': '🇨🇭 Nestlé S.A.',
    
    # 🇮🇳 Indian Stocks (.NS) - Available ONLY on FMP
    'RELIANCE.NS': '🇮🇳 Reliance Industries',
    'TCS.NS': '🇮🇳 Tata Consultancy Services',
    'HDFCBANK.NS': '🇮🇳 HDFC Bank',
    'INFY.NS': '🇮🇳 Infosys Limited',
    'HINDUNILVR.NS': '🇮🇳 Hindustan Unilever',
    'ITC.NS': '🇮🇳 ITC Limited',
    'KOTAKBANK.NS': '🇮🇳 Kotak Mahindra Bank',
    'BHARTIARTL.NS': '🇮🇳 Bharti Airtel',
    'SBIN.NS': '🇮🇳 State Bank of India',
    'MARUTI.NS': '🇮🇳 Maruti Suzuki',
    
    # 🇯🇵 Japanese Stocks (.T) - Available ONLY on FMP  
    '7203.T': '🇯🇵 Toyota Motor Corp.',
    '6758.T': '🇯🇵 Sony Group Corp.',
    '9984.T': '🇯🇵 SoftBank Group',
    
    # 🇰🇷 Korean Stocks (.KS) - Available ONLY on FMP
    '005930.KS': '🇰🇷 Samsung Electronics',
}

# API comparison data
API_COMPARISON_DATA = """
| Feature | Alpha Vantage | FMP | CSV |
|---------|---------------|-----|-----|
| **🇺🇸 US Stocks** | ✅ | ✅ | ✅ |
| **🇮🇳 Indian (.NS)** | ❌ | ✅ | ✅ |
| **🇯🇵 Japanese (.T)** | ❌ | ✅ | ✅ |
| **🇰🇷 Korean (.KS)** | ❌ | ✅ | ✅ |
| **🇪🇺 European** | ❌ | ✅ | ✅ |
| **📈 ADRs** | ✅ | ✅ | ✅ |
| **🆓 Free Tier** | 25/day | 250/day | Unlimited |
| **🏢 Corporate Network** | ✅ | ✅ | ✅ |
"""

# Data source configurations
DATA_SOURCE_CONFIG = {
    "🔵 Alpha Vantage API": {
        "description": """
        **Alpha Vantage Features:**
        - ✅ 25 requests/day (free)
        - ✅ 20+ years of data
        - ✅ Reliable corporate network access
        - ⚠️ **LIMITED: US stocks + ADRs only**
        
        **✅ Supported:** US exchanges (NASDAQ, NYSE) + ADRs
        **❌ Not Supported:** Indian (.NS), Japanese (.T), Korean (.KS), European exchanges
        
        **Get FREE API key:**
        [alphavantage.co/support/#api-key](https://alphavantage.co/support/#api-key)
        """,
        "api_key_label": "Alpha Vantage API Key:",
        "api_key_help": "Get free API key from alphavantage.co"
    },
    "🟢 Financial Modeling Prep": {
        "description": """
        **Financial Modeling Prep Features:**
        - ✅ 250 requests/day (free)
        - ✅ Demo mode available
        - ✅ Multiple fallback sources
        
        **Get FREE API key:**
        [financialmodelingprep.com](https://financialmodelingprep.com/developer/docs)
        """,
        "api_key_label": "FMP API Key:",
        "api_key_help": "Use 'demo' for testing or get free key",
        "default_value": "demo"
    },
    "📁 Upload CSV File": {
        "description": """
        **CSV Upload Features:**
        - ✅ Use your own data files
        - ✅ No API limits
        - ✅ Works offline
        """,
        "csv_requirements": """
        **CSV Format Requirements:**
        - Required columns: `Date`, `Open`, `High`, `Low`, `Close`, `Volume`
        - Date format: YYYY-MM-DD
        """
    }
} 