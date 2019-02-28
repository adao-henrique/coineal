from coineal_api import coinealApiConnection
import json

coin = coinealApiConnection(Key = "", secret= "", mobile="", password="", country = "55")
symbol = "vssusdt"

print("Buscando o ticker das ultimas 24h do '{}'...".format(symbol))
print("{}\n".format(json.dumps(coin.get_ticker("{}".format(symbol)).json(), indent = 2)))

print("Buscando o livro de ordens de '{}'...".format(symbol))
print("{}\n".format(coin.get_market("{}".format(symbol), "step0").json()))

print("Obtendo o preço de transação mais recente de cada moeda...")
print("{}\n".format(json.dumps(coin.get_latest_transaction().json(), indent = 2)))

print("Criando ordem...")
print("{}\n".format(json.dumps(coin.create_order(side="SELL", type=1, price=1, volume=1, symbol="{}".format(symbol)).json(), indent = 2)))

print("Cancelando Ordem")
print("{}\n".format(json.dumps(coin.cancel_order(order_id="34343", symbol="{}".format(symbol)).json(), indent = 2)))
