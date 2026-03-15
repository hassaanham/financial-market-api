from fastapi import FastAPI, HTTPException
import requests
import pandas as pd

app = FastAPI(title="Financial Market Data API")

# Sample stock data (simulated market data)
STOCKS = {
    "AAPL": {"price": 212.45, "previous_close": 210.10, "currency": "USD"},
    "MSFT": {"price": 418.72, "previous_close": 415.40, "currency": "USD"},
    "GOOG": {"price": 173.28, "previous_close": 171.95, "currency": "USD"},
    "AMZN": {"price": 186.14, "previous_close": 184.20, "currency": "USD"},
    "TSLA": {"price": 178.53, "previous_close": 175.80, "currency": "USD"}
}


@app.get("/")
def home():
    return {"message": "Financial Market Data API is running"}


@app.get("/stock/{symbol}")
def get_stock(symbol: str):
    symbol = symbol.upper()

    if symbol not in STOCKS:
        raise HTTPException(status_code=404, detail="Stock symbol not found")

    stock = STOCKS[symbol]

    return {
        "symbol": symbol,
        "price": stock["price"],
        "previous_close": stock["previous_close"],
        "currency": stock["currency"]
    }


@app.get("/compare")
def compare_stocks(symbols: str):
    symbol_list = [symbol.strip().upper() for symbol in symbols.split(",")]

    stocks = []

    for symbol in symbol_list:
        if symbol in STOCKS:
            stock = STOCKS[symbol]
            stocks.append({
                "symbol": symbol,
                "price": stock["price"],
                "previous_close": stock["previous_close"],
                "currency": stock["currency"]
            })

    if not stocks:
        raise HTTPException(status_code=404, detail="No valid stock symbols found")

    df = pd.DataFrame(stocks)

    # calculate price change
    df["change"] = (df["price"] - df["previous_close"]).round(2)

    return df.to_dict(orient="records")


@app.get("/market-news")
def market_news():
    url = "https://jsonplaceholder.typicode.com/posts?_limit=3"

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        return {
            "source": "Demo external API",
            "articles": data
        }

    except requests.exceptions.RequestException:
        raise HTTPException(status_code=500, detail="Failed to fetch market news")