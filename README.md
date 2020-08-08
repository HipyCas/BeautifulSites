# BeautifulSites4
An implementation of BeautifulSoup for some of the most popular and useful websites

What exactly?
---
BeautifulSites4 is an implementation of BeautifulSoup4 for some of the most popular and useful sites possible. Instead of having to parse all the data yourself, you can for example, get the results of a Bing search just by doing `BingSearch('foo').result_list()`

How does it work?
---
The way this BeautifulSites4 works is pretty straight forward. 

It is completely based in class, so any page that you want to query is available as a class to call. For example, for getting the results of a Bing search of the topic 'foo', you would need to create a `BingSearch` class from the *search* module, by typing `BingSearch('foo')`

Pretty simple, right? Getting the results isn't any harder. With the Bing example, you can get the results of the search (shown in the current page, of course). Let's say you saved the BingSearch instance in the variable `bing`. If you now want to get the results of the query you have stored in `bing`, you would simply type `bing.result_list()` and done.

But keep an eye open! The results of each type of query have their own class to be represented, so a wiki page would have a `WikiResult` and a search query have a `SearchResult`, with different attributes and even methods. Continuing with the Bing example, `bing.result_list()` returns a tuple of this `SearchResult` class. To actually access the data, you have to individually access the title, description and link attributes (they will become iterable later on).

The Bing example
---
```python
from BeautifulSites4.search import BingSearch

bing = BingSearch('foo')
results = bing.result_list()
type(results[0])  # Outputs <class 'BeautifulSites4.search.SearchResult'>

for result in results:
    print('== Result ==')
    print(f' {result.title}')
    print(f' {result.description}')
    print(f' {result.link}\n')
``` 

Contributing
---
What an awesome idea! If you have an idea of a website, that you have studied the architecture, and know how to scrap the data with BeautifulSoup4, I'm happy to hear that and look forward to see your page implemented in this package.

To contribute, clone the repository and create a fork of it first, then implement the code in the section you believe it should go, and make a pull request.

Contributors
---
TODO