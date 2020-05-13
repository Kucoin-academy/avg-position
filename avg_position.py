#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import time
from decimal import Decimal

from kucoin.client import Market, User, Trade


class Avg(object):

    def __init__(self):
        # read configuration from json file
        with open('config.json', 'r') as file:
            config = json.load(file)

        self.api_key = config['api_key']
        self.api_secret = config['api_secret']
        self.api_passphrase = config['api_passphrase']
        self.sandbox = config['is_sandbox']
        self.symbol = config['symbol']
        self.min_param = float(config['min_param'])
        self.price_param = float(config['price_param'])
        self.market = Market(self.api_key, self.api_secret, self.api_passphrase, is_sandbox=self.sandbox)
        self.user = User(self.api_key, self.api_secret, self.api_passphrase, is_sandbox=self.sandbox)
        self.trade = Trade(self.api_key, self.api_secret, self.api_passphrase, is_sandbox=self.sandbox)
        self.symbol_trade = self.symbol+'-USDT'

    def get_symbol_precision(self):
        s = self.market.get_symbol_list()
        sd = {}
        for item in s:
            if item.get('symbol') and item.get('symbol') == self.symbol_trade:
                sd = item
        return int(1 / Decimal(sd['baseMinSize']))


if __name__ == '__main__':
    avg = Avg()
    init_ticker = avg.market.get_ticker(avg.symbol_trade)
    init_price = float(init_ticker['price'])
    print('init_price =', init_price)
    precision = avg.get_symbol_precision()
    print('precision =', precision)

    while 1:
        time.sleep(1)
        # account balance
        symbol_balance = avg.user.get_account_list(avg.symbol, 'trade')
        available_symbol = float(symbol_balance[0]['available'])
        print('symbol_balance =', available_symbol)

        usdt_balance = avg.user.get_account_list('USDT', 'trade')
        available_usdt = float(usdt_balance[0]['available'])
        print('usdt_balance =', available_usdt)

        now_symbol = avg.market.get_ticker(avg.symbol_trade)
        now_price = float(now_symbol['price'])
        print('now_price =', now_price)

        # calculate the number that how much needs to buy
        to_buy = (available_usdt - available_symbol * now_price) / 2 / now_price
        to_buy = int(to_buy * precision) / precision
        print('to_buy =', to_buy)
        # calculate the number that how much needs to sell
        to_sell = (available_symbol * now_price - available_usdt) / 2 / now_price
        to_sell = int(to_sell * precision) / precision
        print('to_sell =', to_sell)
        if abs((now_price - init_price) / init_price) > avg.price_param:
            init_price = float(now_price)
            print('refresh init_price =', init_price)
            if to_buy > avg.min_param:
                buy_order = avg.trade.create_limit_order(avg.symbol_trade, 'buy', to_buy, now_price)
                print('buy number > min_param,buy order id =', buy_order['orderId'])
            elif to_sell > avg.min_param:
                sell_order = avg.trade.create_limit_order(avg.symbol_trade, 'sell', to_sell, now_price)
                print('sell number > min_param,sell order id =', sell_order['orderId'])

