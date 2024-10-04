

import requests
import json

class GetRequester:
    def __init__(self, url):
        self.url = url

    
    def get_response_body(self):
        try:
            response = requests.get(self.url)
            if response.status_code == 200:
                return response.content  
            else:
                return None
        except requests.exceptions.RequestException as e:
            print(f"An error occurred: {e}")
            return None
        pass
    
    def load_json(self):
        response_body = self.get_response_body()
        if response_body:
            return json.loads(response_body)  
        return None
        pass