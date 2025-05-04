class StockDataVisualizer:
    def plot_price(self, data, ticker):
        import matplotlib.pyplot as plt
        
        plt.figure(figsize=(14, 7))
        plt.plot(data['Close'], label=f"{ticker} Close Price", color="blue")
        plt.title(f"{ticker} Stock Price")
        plt.xlabel("Date")
        plt.ylabel("Price")
        plt.legend()
        plt.grid()
        plt.show()

    def plot_returns(self, data, ticker):
        import seaborn as sns
        
        sns.histplot(data['Daily Return'], bins=50, kde=True, color="purple")
        plt.title(f"{ticker} Daily Returns Distribution")
        plt.xlabel("Daily Return (%)")
        plt.ylabel("Frequency")
        plt.show()