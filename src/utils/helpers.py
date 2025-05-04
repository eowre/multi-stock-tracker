import datetime
import os
import matplotlib.pyplot as plt

def format_date(date):
    """Formats a datetime object to a string in the format YYYY-MM-DD."""
    return date.strftime("%Y-%m-%d")

def save_plot(figure, filename):
    """Saves a matplotlib figure to a specified filename."""
    directory = os.path.dirname(filename)
    if not os.path.exists(directory):
        os.makedirs(directory)
    figure.savefig(filename)
    plt.close(figure)