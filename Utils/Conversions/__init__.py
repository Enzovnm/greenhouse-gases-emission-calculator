import json
import requests


def real_to_dolar(value):
    datas = requests.get(
        'https://economia.awesomeapi.com.br/json/last/BRL-USD/').text
    datas = json.loads(datas)
    real_converted = float(datas['BRLUSD']['high'])
    value_converted = value * real_converted
    return value_converted
