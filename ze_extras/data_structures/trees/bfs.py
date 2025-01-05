
from collections import deque
from utils.node import Node, create_tree


def bfs(root):
    # Use queue, pop from the left , add to the right
    queue = deque([root])
    visited = set()
    levels = 0

    while queue:
        node = queue.popleft()
        print(f"Visiting: {node.value}")

        if node.left:
            if node.left not in visited:
                print(f"Adding L: {node.left.value}")
                visited.add(node.left)
                queue.append(node.left)
        if node.right:
            if node.right not in visited:
                print("Adding R: {}".format(node.right.value))
                visited.add(node.right)
                queue.append(node.right)
        levels += 1
    print(f'Levels: {levels}')

root = create_tree()
bfs(root)
