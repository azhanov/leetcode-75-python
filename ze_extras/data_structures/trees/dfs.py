
import collections
from utils.node import Node, create_tree


def visit(v):
    if v:
        print(v.value)
    else:
        print(None)


root = create_tree()
visited = set()
# Use stack , pop from the right, append to the right
stack = collections.deque([root])


def dfs_iter():
    """
    Depth first search but iterating over a stack. Immediate children of a node are placed on the stack.
    Then, popped from the stack
    :return:
    """
    while stack:
        node = stack.pop()
        if node not in visited:
            if not node:
                print(node)
            visited.add(node)
            visit(node)
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)


dfs_iter()



print('-'*70)



root = create_tree()
visited = set()
stack = collections.deque([root])


def dfs_recursive(node):
    """
    Depth first search using recursive call.
    :param node:
    :return:
    """
    if not node:
        return
    if node not in visited:
        visited.add(node)
        print(node.value)
        dfs_recursive(node.left)
        dfs_recursive(node.right)


dfs_recursive(root)
