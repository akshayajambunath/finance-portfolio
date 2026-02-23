import yfinance as yf

def get_full_financials(ticker_symbol):
    try:
        stock = yf.Ticker(ticker_symbol)

        # Basic Market Data
        info = stock.info
        current_price = info.get("currentPrice")
        eps = info.get("trailingEps")
        pe_ratio = info.get("trailingPE")

        print(f"\nFinancial Data for {ticker_symbol.upper()}")
        print("-" * 50)
        print(f"Current Price: ${current_price}")
        print(f"EPS (TTM): {eps}")
        print(f"P/E Ratio (TTM): {pe_ratio}")

        # Financial Statements (Annual)
        financials = stock.financials  # Income statement
        financials = financials.T  # Transpose for easier reading

        print("\n--- Last 3 Years Financial Data ---")

        # Loop through last 3 years
        for i in range(min(3, len(financials))):
            year = financials.index[i].year
            revenue = financials.iloc[i].get("Total Revenue")
            net_income = financials.iloc[i].get("Net Income")

            print(f"\nYear: {year}")
            print(f"Revenue: {revenue}")
            print(f"Net Income: {net_income}")

            # Profit Margin
            if revenue and net_income:
                profit_margin = net_income / revenue
                print(f"Profit Margin: {profit_margin:.2%}")

        # Revenue Growth (last 2 years)
        if len(financials) >= 2:
            revenue_latest = financials.iloc[0].get("Total Revenue")
            revenue_previous = financials.iloc[1].get("Total Revenue")

            if revenue_latest and revenue_previous:
                revenue_growth = (revenue_latest - revenue_previous) / revenue_previous
                print(f"\nRevenue Growth (Latest Year): {revenue_growth:.2%}")

        market_cap = info.get("marketCap")
        print(f"Market Cap: {market_cap}")

    except Exception as e:
        print("Error retrieving data:", e)


if __name__ == "__main__":
    ticker_list = ["AAPL"]
    for ticker in ticker_list:
        get_full_financials(ticker)
