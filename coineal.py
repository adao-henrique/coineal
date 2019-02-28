from coineal_api import coinealApiConnection
import json

coin = coinealApiConnection(Key = "c04ca9e9fd0c82f7c3fd5d2a6f9a0277", secret= "51f87bca9d85145eea3b4febe0b6d51e", mobile="", password="", country = "55")
symbol = "vssusdt"

print("Buscando o ticker das ultimas 24h do '{}'...".format(symbol))
print("{}\n".format(json.dumps(coin.get_ticker("{}".format(symbol)).json(), indent = 2)))

print("Buscando o livro de ordens de '{}'...".format(symbol))
print("{}\n".format(coin.get_market("{}".format(symbol), "step0").json()))

print("Obtendo o preço de transação mais recente de cada moeda...")
print("{}\n".format(json.dumps(coin.get_latest_transaction().json(), indent = 2)))

print("Criando ordem...")
print("{}\n".format(json.dumps(coin.create_order(side="SELL", type=1, price=1, volume=1, symbol="vssusdt").json(), indent = 2)))

print("Cancelando Ordem")
print("{}\n".format(json.dumps(coin.cancel_order(order_id="34343", symbol="vssusdt").json(), indent = 2)))
