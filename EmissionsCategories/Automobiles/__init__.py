class Automobiles:

    def __init__(self, suply_chain_spends):
        self.suply_chain_spends = suply_chain_spends
        self.data = {
            "emission_factor": {
                # GHG PROTOCOL 2017
                "activity_id": "passenger_vehicle-vehicle_type_automobile-fuel_source_na-distance_na-engine_size_na"
            },
            "parameters": {
                "distance": suply_chain_spends,
                "distance_unit": "km"
            }
        }
