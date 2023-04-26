from dask.bytes.tests.test_http import requests


class WhatsApp:
    def __init__(self):
        self._api_key = "krFbpYI7QNKTmvKWpyL8QP1cAK"
        self.base_url = 'https://waba.360dialog.io/v1/messages'
        self.headers = {
            'D360-API-KEY': self._api_key,
            'Content-Type': 'application/json',
        }

    def send_message_to_whatsapp(self, data):
        response = requests.post(self.base_url, headers=self.headers, json=data)
        return response

