import requests
import json


class EmissionsEstimate:

    BASE_URL = 'https://beta3.api.climatiq.io/'
    API_KEY = '11GM28ZZW94KVCP05ERBS4Y3SXFM'  # YOUR API KEY

    def __init__(self, emissions):
        self.emissions = emissions

    def emissions_estimate(self):

        # REQUEST ON CLIMATIQ API
        head = {'Authorization': 'Bearer ' + self.API_KEY}
        r = requests.post(self.BASE_URL + 'batch',
                          data=json.dumps(self.emissions), headers=head)
        return r.text
