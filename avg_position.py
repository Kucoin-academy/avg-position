#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time

from kucoin.client import Market, User, Trade

if __name__ == '__main__':
    # read configuration from json file
    with open('config.json', 'r') as file:
        config = json.load(file)

    api_key = config['api_key']
    api_secret = config['api_secret']
    api_passphrase = config['api_passphrase']
    symbol = config['symbol']
    min_param = config['min_param']
    price_param = config['price_param']
    sandbox = config['is_sandbox']
    market = Market(api_key, api_secret, api_passphrase, is_sandbox=sandbox)
    user = User(api_key, api_secret, api_passphrase, is_sandbox=sandbox)
    trade = Trade(api_key, api_secret, api_passphrase, is_sandbox=sandbox)
    init_ticker = market.get_ticker(symbol+'-USDT')
    init_price = float(init_ticker['price'])
    print('init_price =', init_price)

    while 1:
        time.sleep(1)
        # account balance
        symbol_balance = user.get_account_list(symbol, 'trade')
        available_symbol = float(symbol_balance[0]['available'])
        print('symbol_balance =', available_symbol)
        usdt_balance = user.get_account_list('USDT', 'trade')
        available_usdt = float(usdt_balance[0]['available'])
        print('usdt_balance =', available_usdt)
        now_symbol = market.get_ticker(symbol+'-USDT')
        now_price = float(now_symbol['price'])
        print('now_price =', now_price)
        # calculate the number that how much needs to buy
        to_buy = (available_usdt - available_symbol * now_price) / 2 / now_price
        print('to_buy =', to_buy)
        # calculate the number that how much needs to sell
        to_sell = (available_symbol * now_price - available_usdt) / 2 / now_price
        print('to_sell =', to_sell)
        if abs((now_price - init_price) / init_price) > price_param:
            init_price = float(now_price)
            print('refresh init_price =', init_price)
            if to_buy > min_param:
                buy_order = trade.create_limit_order(symbol, 'buy', to_buy, now_price)
                print('buy number > min_param,buy order id =', buy_order['orderId'])
            elif to_sell > min_param:
                sell_order = trade.create_limit_order(symbol, 'sell', to_sell, now_price)
                print('sell number > min_param,sell order id =', sell_order['orderId'])

