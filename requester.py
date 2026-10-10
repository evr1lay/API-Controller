import requests


class Requester:
    def __init__(self, url: str) -> None:
        self.url = url

    def is_api_running(self) -> bool:
        try:
            response = requests.get(self.url, timeout=1)
            return response.status_code == 200
        except requests.exceptions.RequestException:
            return False

    def get(self):
        """returns .json() of GET method"""
        return requests.get(self.url)

    def post(self, message_content: str):
        """returns .json() of POST method"""
        json = {"content": message_content}
        return requests.post(self.url, json=json)
