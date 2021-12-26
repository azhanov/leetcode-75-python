from Graphs.node import Node, create_tree

'''
Inorder traversal:    Left, Visit, Right
'''
def traverse_tree_inorder(node):
    order = []
    if node is None:
        return order
    if node:
        order = traverse_tree_inorder(node.left)
        order.append(node.value)
        order = order + traverse_tree_inorder(node.right)
        print(order)
    return order


def traverse_tree_inorder2(node, order=[]):
    if node is None:
        return order
    traverse_tree_inorder2(node.left, order)
    order.append(node.value)
    order + traverse_tree_inorder2(node.right, order)
    print(order)
    return order


root = create_tree()
traverse_tree_inorder(root)
print('-'*10)
traverse_tree_inorder2(root)
