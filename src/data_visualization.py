import matplotlib.pyplot as plt
from utils.helpers import save_plot

class StockDataVisualizer:
    def plot_price(self, data):
        """Plot stock price and moving averages."""
        fig, ax = plt.subplots(figsize=(12, 6))
        data["Close"].plot(ax=ax, label="Close Price")
        
        if "7-day MA" in data.columns:
            data["7-day MA"].plot(ax=ax, label="7-day MA")
        if "30-day MA" in data.columns:
            data["30-day MA"].plot(ax=ax, label="30-day MA")
            
        ax.set_title("Stock Price and Moving Averages")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend()
        
        save_plot(fig, "plots/price_plot.png")

    def plot_returns(self, data):
        """Plot daily returns."""
        fig, ax = plt.subplots(figsize=(12, 6))
        data["Daily Return"].plot(ax=ax, kind="bar")
        
        ax.set_title("Daily Returns")
        ax.set_xlabel("Date")
        ax.set_ylabel("Return (%)")
        
        save_plot(fig, "plots/returns_plot.png")