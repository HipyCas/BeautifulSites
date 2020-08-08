from BeautifulSites4.core import *


class SearchResult:
    def __init__(self, title, description, page, link):
        self.title = title
        self.description = description
        self.page = page
        self.link = link

    # TODO: More attr? Methods?


# TODO: Solve Google data parsing, look at Bing's
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

    def __init__(self, query: str, **params):
        params.update(q=query)
        super().__init__(self.baseURL, **params)
        self.set_meta(title=self.soup.find('title').get_text())
    
    def result_list(self):
        # Extract titles
        titles = []
        for serp in range(5090, 5220):  # search for all titles
            t = self.soup.find('a', h=f'ID=SERP,{serp}.1')
            if t:
                titles.append(t.get_text())
        while 'Traducir esta página' in titles or 'Translate this page' in titles or 'https://' in titles or 'http://' in titles:  # clear unwanted titles
            for i in range(len(titles)):
                if titles[i] == 'Traducir esta página' or titles[i] == 'Translate this page' or 'https://' in titles[i] or 'http://' in titles[i]:
                    del titles[i]
                    break

        # Extract descriptions
        descriptions = [list(description.children)[1].get_text() for description in self.soup.find_all('div', class_='b_caption')]

        # Extract links
        links = [link.get_text() for link in self.soup.find_all('div', class_='b_attribution')]

        # Generate results (SearchResult list)
        results = []
        for i in range(len(titles)):
            results.append(SearchResult(title=titles[i], description=descriptions[i], page=None, link=links[i]))

        # Return results as tuple
        return tuple(results)


class YahooSearch(Page, PageInterface):

    baseURL = 'https://search.yahoo.com/search'

    def __init__(self, query: str, **params):
        params.update(q=query)
        super().__init__(self.baseURL, **params)
        self.set_meta(title=self.soup.find('title'))

    def result_list(self) -> tuple:
        # Extract titles
        titles = [title.get_text() for title in self.soup.find_all('a', class_='ac-algo fz-l ac-21th lh-24')]

        # Extract description
        descriptions = [description.get_text() for description in self.soup.find_all('p', class_='fz-ms lh-1_43x')]

        # Extract pages
        pages = [page.get_text() for page in self.soup.find_all('span', class_='fz-ms fw-m fc-12th wr-bw lh-17')]

        # Extract links
        links = [link['href'] for link in self.soup.find_all('a', class_='ac-algo fz-l ac-21th lh-24')]

        # Generate results (SearchResult list)
        results = []
        for i in range(len(titles)):
            results.append(SearchResult(title=titles[i], description=descriptions[i], page=pages[i], link=links[i]))

        # Return results as tuple
        return tuple(results)
