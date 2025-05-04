class StockDataAnalyzer:
    def calculate_daily_returns(self, data):
        """Calculate daily returns from stock data."""
        data["Daily Return"] = data["Close"].pct_change() * 100
        return data

    def calculate_moving_averages(self, data, window):
        """Calculate moving averages for the stock data."""
        data[f"{window}-day MA"] = data["Close"].rolling(window=window).mean()
        return data