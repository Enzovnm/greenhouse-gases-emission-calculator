import json
from Utils.Conversions import real_to_dolar
import streamlit as st
import pandas as pd
from EmissionsCategories import Agriculture
from EmissionsCategories import Automobiles
from EmissionsCategories import Construction
from EmissionsCategories import Eletricity
from EmissionsCategories import FinancialService
from EmissionsCategories import RealState
from BatchEstimate.emissions_estimate import EmissionsEstimate

st.header('Calculadora de Emissões de Gases do Efeito Estufa')


category = st.selectbox('Selecione a categoria do seu empreendimento:', (
    'Agricultura', 'Construção', 'Serviço Financeiro', 'Mercado Imobiliário')
)


suply_chain = st.number_input(
    "Digite o Financiamento da Cadeia de Suprimentos em R$ do seu empreendimento: ", min_value=0.00)

suply_chain = real_to_dolar(suply_chain)


kwh_consumption = st.number_input(
    'Digite o consumo de KWh desde o ínicio do seu empreendimento: ', min_value=0)


colaborators = st.number_input(
    'Digite a quantidade de colaboradores no seu empreendimento', min_value=0)

office_distance = st.number_input(
    "Digite a distancia média de Km que os colaboradores percorrem para chegar no escritório", min_value=0)

calculate_button = st.button('Calcular')

if calculate_button:

    ghg_emission_by_category = {
        'Agricultura': Agriculture.Agriculture(suply_chain).data,
        'Construção': Construction.Construction(suply_chain).data,
        'Serviço Financeiro': FinancialService.FinancialService(suply_chain).data,
        'Mercado Imobiliário': RealState.RealState(suply_chain).data
    }

    # EMISSIONS CALCULATOR
    energy_consumption_ghg_emission = Eletricity.Eletricity(
        kwh_consumption).data

    # Job Round Trip by colaborator
    gasoline_ghg_emission_by_colaborator = Automobiles.Automobiles(
        office_distance*colaborators*2).data

    ghg_emissions_list = [ghg_emission_by_category[category],
                          energy_consumption_ghg_emission,
                          gasoline_ghg_emission_by_colaborator
                          ]

    emissions = EmissionsEstimate(
        ghg_emissions_list).emissions_estimate()

    emissions_list = json.loads(emissions)

    emissions = {
        "Categoria": [],
        "Fonte de Dados": [],
        "Unidade do CO2": [],
        "Método do Cálculo": [],
        "Quantidade de Emissão de CO2": []

    }

    for i in emissions_list['results']:
        emissions["Categoria"].append([i['emission_factor']['category']])
        emissions["Fonte de Dados"].append(i['emission_factor']['source'])
        emissions['Unidade do CO2'].append(i['co2e_unit'])
        emissions["Método do Cálculo"].append(i['co2e_calculation_method'])
        emissions["Quantidade de Emissão de CO2"].append(i['co2e'])

    emissions_df = pd.DataFrame(emissions)

    co2_emissions_total_tonne = (
        emissions_df['Quantidade de Emissão de CO2'].sum()) / 1000

    st.write(emissions_df)

    st.markdown('#### Emissão de CO2 Total:')
    st.write('#### ' + str(co2_emissions_total_tonne))
