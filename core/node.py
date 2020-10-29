"""
This module contains Node class, which represents one article.
"""


from typing import List
from core import parsing


class Node:
    """
    Represents article. Has a title, URL, parent and child nodes
    """

    title: str
    url: str
    parent: 'Node' = None
    children: List['Node'] = None

    def __init__(self, url: str, parent: 'Node'):
        self.url = url
        self.parent = parent
        self.children = []
        self.title = parsing.get_title(self.url)

    def set_children(self):
        """
        Finds all links on page and creates child Nodes
        """
        urls = parsing.get_all_links(self.url)

        for url in urls:
            self.children.append(Node(url, self))

    def try_find_answer(self, target_answer: str) -> 'Node':
        """
        Looks if one of the children is a final point. Returns it if yes, else None
        """
        for node in self.children:
            if node.title == target_answer:
                return node
        return None
