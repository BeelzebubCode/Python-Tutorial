import yfinance as yf

# ดึงข้อมูล EUR/USD ย้อนหลัง
symbol = "EURUSD=X"
data = yf.download(symbol, start="2020-01-01", end="2024-03-01")

print(data.head())