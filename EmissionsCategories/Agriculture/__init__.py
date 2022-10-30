class Agriculture:

    def __init__(self, suply_chain_spends):
        self.suply_chain_spends = suply_chain_spends
        self.data = {
            "emission_factor": {
                # GHG PROTOCOL 2017
                "activity_id": "agriculture_fishing_forestry-type_agriculture_hunting_forestry_fishing"
            },
            "parameters": {
                "money": suply_chain_spends,
                "money_unit": "usd"
            }
        }
