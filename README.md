# Stock Tracker

This project is a stock tracking application that allows users to fetch, analyze, and visualize stock data for major companies including Microsoft (MSFT), NVIDIA (NVDA), Google (GOOG), Amazon (AMZN), and Meta (META).

## Project Structure

```
stock-tracker
├── src
│   ├── main.py               # Entry point of the application
│   ├── data_fetcher.py       # Fetches stock data using yfinance
│   ├── data_analysis.py       # Analyzes stock data (daily returns, moving averages)
│   ├── data_visualization.py   # Visualizes stock prices and returns
│   └── utils
│       └── helpers.py        # Utility functions
├── requirements.txt          # Project dependencies
├── .gitignore                # Files to ignore in Git
└── README.md                 # Project documentation
```

## Setup Instructions

1. Clone the repository:
   ```
   git clone <repository-url>
   cd stock-tracker
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

To run the application, execute the following command:
```
python src/main.py
```

## Functionalities

- **Data Fetching**: Retrieve stock data for MSFT, NVDA, GOOG, AMZN, and META using the `StockDataFetcher` class.
- **Data Analysis**: Calculate daily returns and moving averages using the `StockDataAnalyzer` class.
- **Data Visualization**: Visualize stock prices and daily returns distributions using the `StockDataVisualizer` class.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features you would like to add.