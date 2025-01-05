
class Node(object):
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

    def set_left(self, left):
        self.left = left

    def set_right(self, right):
        self.right = right


def create_tree():
    n8 = Node(8, left=None, right=None)
    n4 = Node(4, left=n8, right=None)
    n5 = Node(5, left=None, right=None)
    n6 = Node(6, left=None, right=None)
    root = Node(1, left=Node(2, n4, n5),    right=Node(3, n6, None))
    return root

#               1
#           2       3
#         4   5    6
#       8
