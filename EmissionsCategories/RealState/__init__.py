class RealState:

    def __init__(self, suply_chain_spends):
        self.suply_chain_spends = suply_chain_spends
        self.data = {
            "emission_factor": {
                # GHG PROTOCOL 2017
                "activity_id": "other_real_estate-type_real_estate_activities"
            },
            "parameters": {
                "money": suply_chain_spends,
                "money_unit": "usd"
            }
        }
