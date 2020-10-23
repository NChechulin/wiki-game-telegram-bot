from node import Node


def pretty_print_answer(end: Node):
    titles = []

    node = end

    while not (node is None):
        titles.append(node.title)
        node = node.parent

    titles.reverse()

    return ' -> '.join(titles)


def search(start_url: str) -> Node:
    TARGET_TITLE = 'Adolf Hitler'

    start_node = Node(start_url, None)

    edge = set()
    edge.add(start_node)

    total = 0

    for _ in range(10):
        new_edge = set()

        while len(edge) > 0:
            total += 1
            node: Node = edge.pop()
            print(node.title)
            node.set_children()

            possible_answer = node.try_find_answer(TARGET_TITLE)

            if not (possible_answer is None):
                print(total)
                return pretty_print_answer(possible_answer)

            for child in node.children:
                new_edge.add(child)

        edge = new_edge

    print(total)
    return 'Nothing found'
