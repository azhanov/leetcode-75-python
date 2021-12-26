from utils.node import Node, create_tree


'''
Postorder traversal:    Left, Right, Root
'''
def print_postorder(node):
    if node:
        print_postorder(node.left)
        print_postorder(node.right)
        print(node.value)


root = create_tree()
print_postorder(root)
