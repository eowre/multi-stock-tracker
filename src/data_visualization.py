import matplotlib.pyplot as plt
import matplotlib.dates as mdates
import pandas as pd
from utils.helpers import save_plot

class StockDataVisualizer:
    def plot_price(self, data):
        """Plot stock price and moving averages"""
        print("Plotting stock price and moving averages...")
        fig, ax = plt.subplots(figsize=(12, 6))
        data["Close"].plot(ax=ax, label="Close Price")
        data["7-day MA"].plot(ax=ax, label="7-day MA")
        data["30-day MA"].plot(ax=ax, label="30-day MA")
        
        ax.set_title("Stock Price and Moving Averages")
        ax.set_xlabel("Date")
        ax.set_ylabel("Price")
        ax.legend()
        plt.show()
        save_plot(fig, "plots/price_plot.png")

    def plot_returns(self, data):
        """Plot daily returns with improved date formatting and alignment."""
        # Ensure the index is a DatetimeIndex and sorted
        data.index = pd.to_datetime(data.index)
        data.sort_index(inplace=True)

        # Plotting
        fig, ax = plt.subplots(figsize=(12, 6))
        ax.bar(data.index, data["Daily Return"], width=0.8, color="blue", alpha=0.7)  # Bar chart

        # Customize the plot
        ax.set_title("Daily Returns")
        ax.set_xlabel("Date")
        ax.set_ylabel("Return (%)")

        # Improve date formatting
        ax.xaxis.set_major_locator(mdates.MonthLocator())
        ax.xaxis.set_major_formatter(mdates.DateFormatter("%b %d"))  # Format dates as "Month Day"
        fig.autofmt_xdate()  # Rotate and align the date labels for better readability

        # Display the plot
        plt.show()
        save_plot(fig, "plots/returns_plot.png")