import yfinance as yf
from data_fetcher import StockDataFetcher
from data_analysis import StockDataAnalyzer
from data_visualization import StockDataVisualizer

def main():
    tickers = ["MSFT", "NVDA", "GOOG", "AMZN", "META"]
    
    fetcher = StockDataFetcher()
    analyzer = StockDataAnalyzer()
    visualizer = StockDataVisualizer()
    
    for ticker in tickers:
        print(f"Fetching data for {ticker}...")
        data = fetcher.fetch_data(ticker)
        
        print(f"Analyzing data for {ticker}...")
        # All operations modify data in-place
        analyzer.calculate_daily_returns(data)
        analyzer.calculate_moving_averages(data, 7)
        analyzer.calculate_moving_averages(data, 30)
        
        print(f"Visualizing data for {ticker}...")
        visualizer.plot_price(data)
        visualizer.plot_returns(data)

if __name__ == "__main__":
    main()