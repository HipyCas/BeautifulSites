from requests import get
from bs4 import BeautifulSoup


class Page:

    def __init__(self, url: str, **kwargs: (str, str)):
        if kwargs:
            params = '?'
            for key, value in kwargs:
                if list(kwargs.items())[-1][0] == key:
                    params += f'{key}={value}'
                else:
                    params += f'{key}={value}&'
            url += params
        if not ('https://' in url or 'http://' in url):
            url = f'https://{url}'
        self.url = url
        self.request = get(url)
        self.soup = BeautifulSoup(self.request.content, 'html.parser')

    def refresh(self):
        self.request = get(self.url)
        self.soup = BeautifulSoup(self.request.content, 'html.parser')