import json
import streamlit as st
import pandas as pd
from Utils.Conversions import real_to_dolar
from EmissionsCategories.Agriculture import Agriculture
from EmissionsCategories.Automobiles import Automobiles
from EmissionsCategories.Construction import Construction
from EmissionsCategories.Eletricity import Eletricity
from EmissionsCategories.FinancialService import FinancialService
from EmissionsCategories.RealState import RealState
from BatchEstimate.emissions_estimate import EmissionsEstimate

# HEADER
st.header('Calculadora de Emissões de Gases do Efeito Estufa')

# INPUTS
category = st.selectbox('Selecione a categoria do seu empreendimento:', (
    'Agricultura', 'Construção', 'Serviço Financeiro', 'Mercado Imobiliário')
)
suply_chain = st.number_input(
    "Digite o Financiamento da Cadeia de Suprimentos em R$ do seu empreendimento: ", min_value=0.00)
kwh_consumption = st.number_input(
    'Digite o consumo de KWh desde o ínicio do seu empreendimento: ', min_value=0)
colaborators = st.number_input(
    'Digite a quantidade de colaboradores no seu empreendimento', min_value=0)
office_distance = st.number_input(
    "Digite a distancia média de Km que os colaboradores percorrem para chegar no escritório", min_value=0)
# BUTTON TO CALCULATE
calculate_button = st.button('Calcular')

# WHEN THE BUTTON IS CLICKED
if calculate_button:
    # CONVERTING SUPLY CHAINFROM R$ TO USD
    suply_chain = real_to_dolar(suply_chain)

    ghg_emission_by_category = {
        'Agricultura': Agriculture(suply_chain).data,
        'Construção': Construction(suply_chain).data,
        'Serviço Financeiro': FinancialService(suply_chain).data,
        'Mercado Imobiliário': RealState(suply_chain).data
    }

    # Energy datas of Enterprise
    energy_consumption_ghg_emission = Eletricity(
        kwh_consumption).data

    # Job Round Trip by colaborator(Automobiles Gasoline)
    gasoline_ghg_emission_by_colaborator = Automobiles(
        office_distance*colaborators*2).data

    # Adding all parameters in a list
    ghg_emissions_list = [ghg_emission_by_category[category],
                          energy_consumption_ghg_emission,
                          gasoline_ghg_emission_by_colaborator
                          ]

    # Retrieving Emissions calculated by API
    emissions = EmissionsEstimate(
        ghg_emissions_list).emissions_estimate()

    # Converting to a dict
    emissions_list = json.loads(emissions)

    # Creating a list to DataFrame
    emissions = {
        "Categoria": [],
        "Fonte de Dados": [],
        "Unidade do CO2": [],
        "Método do Cálculo": [],
        "Quantidade de Emissão de CO2": []

    }

    # Adding dict datas to Dataframe List
    for i in emissions_list['results']:
        emissions["Categoria"].append([i['emission_factor']['category']])
        emissions["Fonte de Dados"].append(i['emission_factor']['source'])
        emissions['Unidade do CO2'].append(i['co2e_unit'])
        emissions["Método do Cálculo"].append(i['co2e_calculation_method'])
        emissions["Quantidade de Emissão de CO2"].append(i['co2e'])

    # Creating DataFrame
    emissions_df = pd.DataFrame(emissions)

    # GHG Emissions Total
    co2_emissions_total_tonne = (
        emissions_df['Quantidade de Emissão de CO2'].sum()) / 1000

    # Displaying DataFrame
    st.write(emissions_df)

    # Displaying GHG Emissions Total
    st.markdown('#### Emissão de CO2 Total:')
    st.write(f'### {co2_emissions_total_tonne:.2f} t CO₂ₑ')
