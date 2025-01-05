
from utils.node import Node, create_tree


def dfs_preorder(node):
    if not node:
        return
    print(node.value)
    dfs_preorder(node.left)
    dfs_preorder(node.right)


root = create_tree()
dfs_preorder(root)

