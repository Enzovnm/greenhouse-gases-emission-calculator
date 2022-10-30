class Construction:

    def __init__(self, suply_chain_spends):
        self.suply_chain_spends = suply_chain_spends
        self.data = {
            'emission_factor': {
                # EXIOBASE 2021
                "activity_id": "construction-type_construction_work"
            },
            "parameters": {
                "money": suply_chain_spends,
                "money_unit": "usd"
            }
        }
