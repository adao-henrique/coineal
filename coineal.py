from coineal_api import coinealApiConnection
import json

coin = coinealApiConnection(Key = "", secret= "", mobile="", password="")
symbol = "vssusdt"

print("Buscando o ticker das ultimas 24h do '{}'...".format(symbol))
print("{}\n".format(json.dumps(coin.get_ticker("{}".format(symbol)).json(), indent = 2)))

print("Buscando o livro de ordens de '{}'...".format(symbol))
print("{}\n".format(coin.get_market("{}".format(symbol), "step0").json()))

print("Obtendo o preço de transação mais recente de cada moeda...")
print("{}\n".format(coin.get_latest_transaction().json()))

print("Criando ordem...")
print("{}\n".format(coin.create_order("SELL", 1, 1, 1, "vssusdt").json(), indent = 2))

print("Cancelando Ordem")
print("{}\n".format(coin.cancel_order("34343", "vssusdt").json(), indent = 2))
