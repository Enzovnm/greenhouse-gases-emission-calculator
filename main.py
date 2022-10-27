from turtle import distance
import requests

BASE_URL = 'https://beta3.api.climatiq.io'
API_KEY = '11GM28ZZW94KVCP05ERBS4Y3SXFM'

agriculture = {
    'emission_factor_id': '3675b9a0-28bc-4dec-b34b-6198e921d781_22cdac63-419a-4980-ad99-5c0caff0a614',
    # 'parameters': weight, weight unit
}
construction = {
    'construction_factor_id': '3675b9a0-28bc-4dec-b34b-6198e921d781_22cdac63-419a-4980-ad99-5c0caff0a614'
    # 'parameters': weight, weight unit
}

financial_service = {
    'financial_service_id': '7241aaa8-6cc4-4a2b-8490-14487018bd2c'
    # parameters
}

real_state = {
    'real_state_id': '3c194ea6-e7b3-42c7-b87d-f92ca549ccc3'
    # parameters
}

office_spends = {
    'office_spends_id': '642c1bd6-b850-4799-aa45-31ffe2326df1'
}

passeger_car = {
    'passeger_car_id' = '56d4bd00-3875-4186-8e8f-284dc2ab7da9'
}


# INPUTS
name = str(input('Digite seu nome: ')).capitalize()

print('#' * 50)
category = int(
    input(' [1] - Agricultura \n [2] - Construção \n [3] - Serviços Financeiro \n [4] - Mercado Imobiliário \n '
          + f'{name}, digite a categoria do seu empreendimento: '))


kwh_per_month = float(
    input(f'{nome}, digite o consumo de KWh do seu empreendimento:'))

office_spends = str(
    f'{nome}, Digite os custos em computadores e eletrônicos: ')


distance_estimated = int(f'{nome}, digite a quantidade de Km no ano: ')






def construction():
    requests.get(url= BASE_URL + '/batch')


def financial_service():
    pass


def real_state():
    pass
