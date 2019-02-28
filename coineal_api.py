import json
import time
import requests
import hashlib
try:
    #python3 compatibility
    import urllib.parse as urlparse
except ImportError:
    import urllib as urlparse



api_address = 'https://exchange-open-api.coineal.com/open/api'

class coinealApiConnection(object):

    #clientKey, secret, and userId are provided by itBit and are specific to your user account
    def __init__(self, Key, secret, mobile, password):
        self.Key = Key
        self.secret = secret.encode('utf-8')
        self.mobile = mobile
        self.nonce = 0
        self.country = "55";
        self.password = password;
        self.time = self._get_timestamp()
        self.api_address = "https://exchange-open-api.coineal.com/open/api"

    def make_request(self, verb, url, body_dict):
        url = api_address + url
        self.time = self._get_timestamp()

        if len(body_dict):
            body_dict['time'] = self.time
            body_dict['sign'] = self.get_sign()

        if verb in ("PUT", "POST"):
            json_body = json.dumps(body_dict)
        else:
            json_body = ""

        return requests.request(verb, url, data = json_body)


    def _get_timestamp(self):
        return int(time.time() * 1000)

    def get_sign(self):
        stri = "country"+self.country+"mobile"+self.mobile+"password"+self.password+"time"+str(self.time)
        string = stri.encode('utf-8')
        return hashlib.md5(string+self.secret).hexdigest()

    #Busca Ticker de um dado Symbol
    def get_ticker(self, tickerSymbol):
        path = "/get_ticker?symbol="+str(tickerSymbol)
        response = self.make_request("GET", path, {})
        return response
    #Busca as ordens em aberto de um dado Symbol
    def get_market(self, tickerSymbol, step):
        path = "/market_dept?symbol="+str(tickerSymbol)+"&type="+str(step)
        response = self.make_request("GET", path, {})
        return response

    def get_latest_transaction(self):
        path = "/market?api_key="+str(self.Key)+"&time="+str(self.time)+"&sign="+self.get_sign()
        response = self.make_request("GET", path, {})
        return response

    def create_order(self, side, type, price, volume, symbol):
        path = "/create_order"
        data ={ "time": "",
                "side": side,
                "type": type,
                "price": price,
                "volume": volume,
                "symbol": symbol,
                "api_key": self.Key,
                "sign": ""}
        response = self.make_request("POST", path, data)
        return response

    def cancel_order(self, order_id, symbol):
        path = "/cancel_order"
        data ={ "order_id": order_id,
                "time": "",
                "symbol": symbol,
                "api_key": self.Key,
                "sign": ""}
        response = self.make_request("POST", path, data)
        return response
