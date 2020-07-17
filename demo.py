# Demo program that:
# logs in
# checks if chosen stock has fractional shares trading
# buys specified amount in dollars 
# sells when purchased amount goes up by specified %

import robin_stocks as rh

user = "test@gmail.com"
pswd = "example"

rh.login(user, pswd)

stock_ticker = "TSLA"
dollar_amount = 1

stock_name = rh.stocks.get_instruments_by_symbols(stock, info="simple_name")
    
print(stock_name + " stock price: " + rh.stocks.get_quotes(stock, info="last_trade_price")[0]) # accessing the first element of the returned list

if (rh.stocks.get_instruments_by_symbols(stock, info="fractional_tradability")[0] == 'tradable'):
    print("Attempting to buy")
    print(rh.orders.order_buy_fractional_by_price(stock, dollar_amount))
else: 
    print(stock_ticker + " isn't fractionally tradeable. Try a different stock.")

#need to get selling and pricing info