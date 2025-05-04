class StockDataFetcher:
    def __init__(self):
        import yfinance as yf
        self.yf = yf

    def fetch_data(self, ticker):
        """
        Fetch historical stock data for the given ticker symbol.
        :param ticker: Stock ticker symbol (e.g., 'MSFT', 'NVDA', 'GOOG', 'AMZN', 'META')
        :return: DataFrame containing stock data
        """
        stock_data = self.yf.Ticker(ticker).history(period="1y", interval="1d")
        return stock_data.dropna()  # Drop any rows with null values