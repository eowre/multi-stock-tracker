import matplotlib.pyplot as plt
from utils.helpers import save_plot

class StockDataVisualizer:
    def plot_price(self, data):
        """Plot stock price and moving averages, updating data in place."""
        # Plotting
        fig, ax = plt.subplots(figsize=(12, 6))
        data["Close"].plot(ax=ax, label="Close Price")
        data["7-day MA"].plot(ax=ax, label="7-day MA")
        data["30-day MA"].plot(ax=ax, label="30-day MA")
        
        ax.set_title("Stock Price and Moving Averages")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend()
        
        save_plot(fig, "plots/price_plot.png")

        plt.show()

    def plot_returns(self, data):
        """Plot daily returns, updating data in place."""
        # Calculate daily returns if not already present
        if "Daily Return" not in data.columns:
            data["Daily Return"] = data["Close"].pct_change() * 100

        # Plotting
        fig, ax = plt.subplots(figsize=(12, 6))
        data["Daily Return"].plot(ax=ax, kind="bar")
        
        ax.set_title("Daily Returns")
        ax.set_xlabel("Date")
        ax.set_ylabel("Return (%)")
        
        save_plot(fig, "plots/returns_plot.png")

        # Show the plot in the notebook
        plt.show()