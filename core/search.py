"""
Contains logic for operating with Nodes
"""


from core.node import Node
from core.cache import Cache
from typing import List

cache = Cache()


def pretty_print_answer(end: Node, is_final=True) -> str:
    """
    Returns a pretty string, which represents a path from start node to end node
    """
    chain = get_node_chain(end)

    if not is_final:
        chain += cache.get(end.title)

    return ' -> '.join(chain)


def get_node_chain(end: Node) -> List[str]:
    """
    Returns a list of titles, which represents the path
    """
    node = end
    titles = []

    while not (node is None):
        titles.append(node.title)
        node = node.parent

    titles.reverse()
    return titles


def search(start_url: str) -> str:
    """
    Searches for a path to end article. Returns pretty printed path, if a solution is found. Else returns Nothing found
    """
    TARGET_TITLE = 'Adolf Hitler'

    start_node = Node(start_url, None)

    edge = set()
    edge.add(start_node)
    seen = set()

    total = 0

    for _ in range(10):
        new_edge = set()

        while len(edge) > 0:
            total += 1
            node: Node = edge.pop()
            node.set_children()

            if cache.in_cache(node.title):
                return pretty_print_answer(node, is_final=False)

            possible_answer = node.try_find_answer(TARGET_TITLE)

            if not (possible_answer is None):
                cache.add(get_node_chain(possible_answer))
                return pretty_print_answer(possible_answer)

            for child in node.children:
                new_edge.add(child)

            seen.add(node)

        edge = new_edge - seen

    return 'Nothing found'
