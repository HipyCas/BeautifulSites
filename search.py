from requests import get
from bs4 import BeautifulSoup


class SearchResult:
    def __init__(self, title, description, page, link):
        self.title = title
        self.description = description
        self.page = page
        self.link = link


"""
class GoogleSearch:
    web_search_URL = 'https://www.google.com/search'
    img_search_URL = ''

    def __init__(self, query: str, **params: (str, str)):
        extra_params = ''
        for key, value in params.items():
            extra_params += f'&{key}={value}'

        self.request = get(f'{self.web_search_URL}?q={query}{extra_params}')
        if self.request.status_code == 200:
            self.soup = BeautifulSoup(self.request.content, 'html.parser')
        else:
            raise RuntimeError('Unable to fetch Google search query')

    def getResults(self) -> tuple:
        results = []
        for title, description, page, link in self.soup.find_all('div', class_='BNeawe vvjwJb AP7Wnd'), self.soup.find_all('div', class_='BNeawe s3v9rd AP7Wnd'), self.soup.find_all('div', class_='BNeawe UPmit AP7Wnd'), self.soup.find_all('div', class_='kCrYT'):
            link = link
            results.append(SearchResult(title.get_text(), description, page.get_text(), list(link.children)[]))
"""
