from Graphs.node import Node, create_tree

queue = []


def print_tree():
    queue.append(root)
    level = 0
    while len(queue):
        current_node = queue.pop(0)
        print("\t"*level + "Popped and processed node = {}".format(current_node.value))

        if current_node.left:
            #print("\t"*level + "Queueing left child node = {}".format(current_node.left.value))
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)
            #print("\t"*level + "Queueing right child node = {}".format(current_node.right.value))
        #print("\t"*level + "Queue : {}".format([node.value for node in queue]))

        level += 1


root = create_tree()
print_tree()
