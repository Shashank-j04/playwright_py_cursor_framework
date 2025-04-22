import requests
from config.config import Config

class APIClient:
    def __init__(self):
        self.config = Config()
        self.session = requests.Session()
        self.session.headers.update({
            "Content-Type": "application/json",
            "Authorization": f"Bearer {self.config.API_KEY}"
        })
    
    def _make_request(self, method: str, endpoint: str, **kwargs):
        """Make an HTTP request"""
        url = f"{self.config.API_BASE_URL}{endpoint}"
        response = self.session.request(method, url, **kwargs)
        response.raise_for_status()
        return response.json()
    
    def get(self, endpoint: str, **kwargs):
        """Make a GET request"""
        return self._make_request("GET", endpoint, **kwargs)
    
    def post(self, endpoint: str, **kwargs):
        """Make a POST request"""
        return self._make_request("POST", endpoint, **kwargs)
    
    def put(self, endpoint: str, **kwargs):
        """Make a PUT request"""
        return self._make_request("PUT", endpoint, **kwargs)
    
    def delete(self, endpoint: str, **kwargs):
        """Make a DELETE request"""
        return self._make_request("DELETE", endpoint, **kwargs) 