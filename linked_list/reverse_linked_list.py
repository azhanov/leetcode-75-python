# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        prev = None
        curr = head
        while curr is not None:
            next_temp = curr.next  # save next node
            curr.next = prev  # point curr node to prev
            prev = curr  # preserve curr for next step
            curr = next_temp  # move forward to next
        return prev


if __name__ == '__main__':
    # Build input linked list
    input_list = list(range(1, 6))
    print("input_list: ")
    print(input_list)
    prev_node = None
    for val in reversed(input_list):
        curr_node = ListNode(val, prev_node)
        prev_node = curr_node

    # Do the work
    s = Solution()
    reversed_linked_list = s.reverseList(curr_node)

    # Converted the resulting reversed linked list into simply reversed list
    reversed_list = []
    node = reversed_linked_list
    while node is not None:
        reversed_list.append(node.val)
        node = node.next
    print("reversed_list: ")
    print(reversed_list)

    # Verify
    assert(input_list == list(reversed(reversed_list)))
