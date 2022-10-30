class Eletricity:

    def __init__(self, suply_chain_spends):
        self.suply_chain_spends = suply_chain_spends
        self.data = {
            'emission_factor': {
                # GHG PROTOCOL 2017
                "activity_id": "electricity-energy_source_grid_mix"
            },
            'parameters': {
                "energy": suply_chain_spends,
                "energy_unit": "kWh"
            }
        }
