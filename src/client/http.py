import httpx


class HttpClient:
    def __init__(self, base_url: str):
        self.base_url = base_url
        self.protocol = "https://"
        self.headers = {"accept": "application/json"}

    def get(self, endpoint, params=None):
        url = self.protocol + self.base_url + endpoint
        response = httpx.get(url, params=params, headers=self.headers)
        return response

    def post(self, endpoint, data=None):
        url = self.base_url + endpoint
        response = httpx.post(url, json=data)
        return response

    def put(self, endpoint, data=None):
        url = self.base_url + endpoint
        response = httpx.put(url, json=data)
        return response

    def patch(self, endpoint, data=None):
        url = self.base_url + endpoint
        response = httpx.patch(url, json=data)
        return response

    def delete(self, endpoint):
        url = self.base_url + endpoint
        response = httpx.delete(url)
        return response
