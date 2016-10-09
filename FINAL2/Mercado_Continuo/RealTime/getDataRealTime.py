from googlefinance import getQuotes
import json

lista = ['BME:TEF','BME:ITX','BME:CDR','BME:EDR','BME:DGI','BME:ENC','BME:PHM','BME:RLIA','BME:TUB','BME:NTH']

print(json.dumps(getQuotes(lista), indent=2))

a = getQuotes(lista)

listaValores = ['StockSymbol','LastTradePrice','LastTradeDateTime','LastTradeDateTimeLong']
for d in a:
    s = ""
    for v in listaValores:
        s = s + str(d[v]) + ";"
    print (s)

