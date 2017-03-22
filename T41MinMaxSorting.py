stocks = {
    'GOOG':520.54,
    'FB':76.45,
    'YHOO':39.28,
    'AMZN':306.21,
    'AAPL':99.76
}

stock_price = zip(stocks.values(),stocks.keys())
for k,v in stock_price:
    print(k,v)
print(30*'=')

print(min(zip(stocks.values(),stocks.keys())))
print(30*'=')
print(max(zip(stocks.values(),stocks.keys())))
print(30*'=')
print(sorted(zip(stocks.values(),stocks.keys())))