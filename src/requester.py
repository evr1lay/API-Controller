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

    def get(self) -> requests.Response:
        """API GET-method."""
        response = requests.get(self.url, timeout=1)
        response.raise_for_status()
        return response

    def post(self, payload: dict) -> requests.Response:
        """API POST-method."""
        response = requests.post(
            self.url,
            json=payload,
            timeout=1,
        )
        response.raise_for_status()
        return response

    def patch(self, id: int | str, payload: dict | None = None) -> requests.Response | None:
        """API PATCH-method."""
        if payload is None:
            return None

        response = requests.patch(
            f"{self.url}/{id}",
            json=payload,
            timeout=1,
        )
        response.raise_for_status()
        return response

    def delete(self, id: int | str):
        pass
