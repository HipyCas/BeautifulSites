import abc
from requests import get 
from requests.models import Response
from bs4 import BeautifulSoup
from typing import Union, Tuple, List


class PageInterface(metaclass=abc.ABCMeta):

    @classmethod
    def __subclasshook_(cls, subclass):
        return (hasattr(subclass, 'result_list') and
                callable(subclass.result_list))

    @abc.abstractmethod
    def result_list(self) -> tuple:
        """ Return the result of the parsing as a list (tuple) """
        raise NotImplementedError


class Page:

    def __init__(self, url: str, **kwargs):
        if kwargs:
            params = '?'
            for key, value in kwargs.items():
                if list(kwargs.items())[-1][0] == key:
                    params += f'{key}={value}'
                else:
                    params += f'{key}={value}&'
            url += params
        if not ('https://' in url or 'http://' in url):
            url = f'https://{url}'
        self.url: str = url
        self.request: Response = get(url)
        self.soup: BeautifulSoup = BeautifulSoup(self.request.content, 'html.parser')

    def refresh(self):
        self.request = get(self.url)
        self.soup = BeautifulSoup(self.request.content, 'html.parser')

    def set_meta(self, **kwargs):
        #? Why does this even exist? Or at least, why do I use it for setting the title?
        for key, value in kwargs.items():
            exec(f'self.{key} = "{value}"')

# TODO: Result class?
