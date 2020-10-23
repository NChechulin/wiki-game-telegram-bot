from node import Node
from queue import Queue


def search(start_url: str) -> Node:
    TARGET_TITLE = 'Adolf Hitler'

    start_node = Node(start_url, None)

    edge = Queue()
    edge.put(start_node)

    for _ in range(10):
        new_edge = Queue()

        while not edge.empty():
            node: Node = edge.get()
            print(node.title)
            node.set_children()

            possible_answer = node.try_find_answer(TARGET_TITLE)

            if not (possible_answer is None):
                return possible_answer

            for child in node.children:
                new_edge.put(child)

        edge = new_edge
    return None
