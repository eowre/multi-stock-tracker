class StockDataAnalyzer:
    def calculate_daily_returns(self, data):
        """Calculate daily returns from stock data and modify DataFrame in-place."""
        import pandas as pd
        
        if "Close" not in data.columns:
            raise ValueError("Data must contain 'Close' column to calculate daily returns.")
        
        # Convert Close to numeric in-place
        data.loc[:, "Close"] = pd.to_numeric(data["Close"], errors='coerce')
        
        # Calculate daily returns in-place
        data.loc[:, "Daily Return"] = data["Close"].pct_change() * 100
        data.fillna({"Daily Return": 0}, inplace=True)

    def calculate_moving_averages(self, data, window):
        """Calculate moving averages and modify DataFrame in-place."""
        if "Close" not in data.columns:
            raise ValueError("Data must contain 'Close' column to calculate moving averages.")
        
        # Calculate moving averages in-place
        column_name = f"{window}-day MA"
        data.loc[:, column_name] = data["Close"].rolling(window=window).mean()