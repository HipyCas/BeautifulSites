from core import *


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


class BingSearch(Page, PageInterface):
    baseURL = 'https://www.bing.com/search'

    def __init__(self, query: str, **params: str):
        params.update(q=query)
        super().__init__(self.baseURL, **params)
        self.set_meta(title=self.soup.find('title').get_text())
    
    def result_list(self):
        titles = []
        for serp in range(5090, 5220):
            t = self.soup.find('a', h=f'ID=SERP,{serp}.1')
            if t:
                titles.append(t)
        while 'Traducir esta página' in titles or 'Translate this page' in titles:
            for i in range(len(titles)):
                if titles[i] == 'Traducir esta página' or titles[i] == 'Translate this page':
                    del titles[i]
                    break

        results = []
        i = 0
        for description, link in self.soup.find_all('div', class_='b_caption'), self.soup.find_all('div', class_='b_attribution'):
            results.append(SearchResult(title=titles[0], description=list(description.children)[1].get_text(), page=None, link=link.get_text()))

        return tuple(results)
