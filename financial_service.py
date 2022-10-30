from msilib.schema import Class


class FinancialService:

    def __init__(self, suply_chain_spends):
        self.suply_chain_spends = suply_chain_spends
        self.data = {
            "emission_factor": {
                # GHG PROTOCOL 2017
                "activity_id": "financial_services-type_financial_intermediation"
            },
            "parameters": {
                "money": suply_chain_spends,
                "money_unit": "usd"
            }
        }
