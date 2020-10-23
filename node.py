from typing import List
import parsing


class Node:
    title: str
    url: str
    parent: 'Node' = None
    children: List['Node'] = None

    def __init__(self, url: str, parent: Node):
        self.url = url
        self.parent = parsing
        self.title = parsing.get_title(self.url)

    def __set_children(self):
        urls = parsing.get_all_links(self.url)

        for url in urls:
            self.children.append(Node(url, self))
