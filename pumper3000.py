################################################### imports #####

import requests
import json
import time
import re
from binance.client import Client
import os
import math
from binance.client import Client
from binance.websockets import BinanceSocketManager
from twisted.internet import reactor

################################################### set var, read files, connect binance and telegram ####

with open('C:\\Users\\bollm\Documents\\Workspaces\\pumper3000\\token.txt') as file:
    token = file.read()
with open('C:\\Users\\bollm\Documents\\Workspaces\\pumper3000\\api_key.txt') as file:
    api_key = file.read()
with open('C:\\Users\\bollm\Documents\\Workspaces\\pumper3000\\api_secret.txt') as file:
    api_secret = file.read()
client = Client(api_key, api_secret)
URL = "https://api.telegram.org/bot{}/".format(token)
BTC = "BTC"
btc_price = {'error':False}

################################################## telegram section ####

def get_url(url):
    response = requests.get(url)
    content = response.content.decode("utf8")
    return content

def get_json_from_url(url):
    content = get_url(url)
    js = json.loads(content)
    return js

def get_updates():
    url = URL + "getUpdates"
    js = get_json_from_url(url)
    return js

def get_last_chat_id_and_text(updates):
    BTC = 'BTC'
    num_updates = len(updates["result"])
    last_update = num_updates - 1
    text = updates["result"][last_update]["message"]["text"]
    cryptolist = re.findall("[#]\w+", text)
    chat_id = updates["result"][last_update]["message"]["chat"]["id"]
    crypto = ''.join(cryptolist)
    crypto = crypto.replace("#", "")
    crypto = crypto.replace("[", "")
    crypto = crypto.replace("]", "")
    crypto = crypto.replace("'", "")
    crypto = crypto.upper()
    market = crypto + BTC
    return (crypto, market, chat_id)

def send_message(text, chat_id):
    url = URL + "sendMessage?text={}&chat_id={}".format(text, chat_id)
    get_url(url)
    
################################################### binance section ####

### kaufmenge ###

def getmenge(market):
    pricearr = client.get_symbol_ticker(symbol=market)
    pricevar = float(pricearr["price"])

    balanceBTC = client.get_asset_balance(asset='BTC')
    FreeBTC= float(balanceBTC['free'])

    FreeBTC= float(FreeBTC * 0.1)
    menge = round(((FreeBTC/pricevar)))
    print('kaufmenge',':',menge)
    input("Press Enter to continue...")
    return menge

### balance ###

def getbalance(crypto):
    print('verfuegbare bitcoin:',client.get_asset_balance(asset='BTC').get('free')) 
    print('verfuegbare pumpwaehrung:',client.get_asset_balance(asset=crypto).get('free'))

### kaufen ###

def buy(market, menge):
    order = client.order_market_buy(symbol=market,quantity=menge)
    print(order)

### verkaufen ###

def sell(crypto, market):
    input("Press Enter to continue...")
    balanceBNB = float(client.get_asset_balance(asset=crypto).get('free'))
    print(balanceBNB)
    balanceBNB = math.floor(balanceBNB)
    print(balanceBNB)
    sell = client.order_market_sell(symbol=market, quantity=balanceBNB)
    print(sell)

### markt mit schneiden ###

def btc_trade_history(msg):
    ''' define how to process incoming WebSocket messages '''
    if msg['e'] != 'error':
        print(msg['c'],msg['p'],msg['P'],msg['E'],msg['s'])
        btc_price['last'] = msg['c']
        btc_price['bid'] = msg['b']
        btc_price['last'] = msg['a']
    else:
        btc_price['error'] = True

def stop_btc_trade_history():
    input("Press Enter to Stop")
    # stop websocket
    bsm.stop_socket(conn_key)
    # properly terminate WebSocket
    reactor.stop()
    
# init and start the WebSocket

bsm = BinanceSocketManager(client)
conn_key = bsm.start_symbol_ticker_socket(market, btc_trade_history)
bsm.start()

################################################### main #####

def main():
    last_textchat = (None, None)
    while True:
        crypto, market, chat = get_last_chat_id_and_text(get_updates())
        if (market, chat) != last_textchat:
            if (market) == BTC:
                print('noch einmal')
                last_textchat = (market, chat)
            else:
                getbalance(crypto)
                menge = getmenge(market)
                #buy(market,menge)
                getbalance(crypto)
                #sell(crypto,market)
                getbalance(crypto)
                stop_btc_trade_history()
                last_textchat = (market, chat)
        time.sleep(0.2)
if __name__ == '__main__':
    main()