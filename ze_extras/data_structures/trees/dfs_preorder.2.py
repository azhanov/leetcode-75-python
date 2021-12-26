
from Graphs.node import create_tree, Node

"""
Preorder traversal:     Root, Left, Right
"""
def dfs(visited, node):
    if not node:
        return
    if node not in visited:
        print(node.value)
        visited.add(node)
        dfs(visited, node.left)
        dfs(visited, node.right)


# Driver Code
visited = set()
dfs(visited, create_tree())
