import requests
from track_station.settings import WHERETHEISS_API, TLE_API

# endpoint = f"/api/tle/{ISS_ID}"

class WhereTheISSAPI:

    @staticmethod
    def get_satellite_id(endpoint, name=""):
        data = requests.get(WHERETHEISS_API+endpoint).json()
        satellite_id = next((item.get('id') for item in data if item.get('name') == name), None)
        
        return satellite_id

    @staticmethod
    def get_iss_data_treated(endpoint):
        return requests.get(WHERETHEISS_API+endpoint).json()

class TLIAPI:

    @staticmethod
    def get_satellite_id(endpoint, name=""):
        data = requests.get(TLE_API+endpoint).json()
        satellite_id = next((item.get('id') for item in data if item.get('name') == name), None)
        
        return satellite_id
        