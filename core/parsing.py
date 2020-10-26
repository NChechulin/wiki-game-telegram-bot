"""
Functions for getting data from by a wikipedia URL
"""


from typing import List
from urllib import request
from lxml import html


def get_html(url: str) -> str:
    """Returns HTML code of the page by url"""
    return request.urlopen(url).read()


def get_html_tree(html_code: str) -> html.HtmlElement:
    """Creates HTML Tree object by HTML code"""
    return html.fromstring(html_code)


def get_title(url: str) -> str:
    """Returns title of the page by it's URL"""
    dirty = url.split('/')[-1]
    return dirty.replace('_', ' ')


def get_all_links(url: str) -> List[str]:
    """Returns list of (title, URL)"""
    ans = set()
    tree = get_html_tree(get_html(url))

    for tag in tree.xpath('//a'):
        href = str(tag.get('href'))

        # get rid of non-relevant links
        if ':' not in href and href.startswith('/wiki/') and not url.endswith(href):
            ans.add(href)

    return ['https://en.wikipedia.org' + partial for partial in ans]
