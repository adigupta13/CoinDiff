import json
from fake_useragent import UserAgent
import requests
import timeit

start_time = timeit.default_timer()
ua = UserAgent(verify_ssl=False)
api_url = "http://data.gate.io/api2/1"

def getGateCoins():
    api_gate_url = api_url + "/tickers"
    headers = {'User-Agent': ua.Safari}
    response = requests.get(api_gate_url,headers=headers)
    if (response.status_code == 200):
        return json.loads(response.content.decode('utf-8'))
    else:
        return {}
    

def getGateDict():
    coin_list = getGateCoins()

    price_dict = dict()

    for i in coin_list:
        base, token = i.split('_')
        base = base.upper()
        token = token.upper()
        if token == 'USDT':
            price = float(coin_list[i]['last'])
            price = float("{0:.3f}".format(price))
            price_dict[base] = price

    for i in coin_list:
        base,token = i.split('_')
        base = base.upper()
        token = token.upper()
        if token != 'USDT':
            if base not in price_dict:
                price = float(price_dict[token]) * float(coin_list[i]['last'])
                #Do price round off
                price = float("{0:.3f}".format(price))
                price_dict[base] = price

    return (price_dict)




