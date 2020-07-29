# Demo program that:
# logs in
# checks if chosen stock has fractional shares trading
# buys specified amount in dollars 
# sells when purchased amount goes up by specified %

import robin_stocks as rh

user = "test@gmail.com"
pswd = "example"

rh.login(user, pswd)

stock_ticker = "FB"
dollar_amount = 1

stock_name = rh.stocks.get_instruments_by_symbols(stock, info="simple_name")
    
print(stock_name + " stock price: " + rh.stocks.get_quotes(stock, info="last_trade_price")[0])

if (rh.stocks.get_instruments_by_symbols(stock_ticker, info="fractional_tradability")[0] == 'tradable'):
    print("Fractional trading is enabled for " + stock_ticker)
    print("Attempting to buy $",dollar_amount," of "+stock_ticker)
    #print(rh.orders.order_buy_fractional_by_price(stock_ticker, dollar_amount, 'gfd')) # buy $1 of stock_ticker, order good for day
    order_ID = rh.orders.get_all_stock_orders(info='id')[0] # get ID of latest order
    purchased_price = float(rh.orders.get_stock_order_info(order_ID)['average_price'])
    purchased_quantity = float(rh.orders.get_stock_order_info(order_ID)['quantity'])
    while True: # this is bad practice because we will make tons of API calls, but this is just a simple demo so it's okay
        current_dollar_value = float(rh.stocks.get_quotes(stock_ticker, info="last_trade_price")[0])*purchased_quantity
        if ( current_dollar_value >= 1.01 ):
            print("Attempting to sell ",current_dollar_value," of "+stock_ticker)
            rh.orders.order_sell_fractional_by_quantity(stock_ticker, purchased_quantity, 'gfd')
else: 
    print(stock_ticker+" isn't fractionally tradeable")

