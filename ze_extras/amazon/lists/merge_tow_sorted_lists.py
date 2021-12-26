# Definition for singly-linked list.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionAlt:
    def mergeTwoLists(self, l1, l2):
        if l1 is None:
            return l2
        elif l2 is None:
            return l1
        elif l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2

"""
                        l1   
                        1    -    4    -    5 
 -1 prev_head,prev      ?
                        l2
                        1    -    2    -    3    -    6
                          
                                  l1   
                        1    -    4    -    5 
 -1 prev_head,prev
                        l2
                        1    -    2    -    3    -    6

                          
                        prev      l1   
                        1    -    4    -    5 
 -1 prev_head                 ?
                        l2
                        1    -    2    -    3    -    6
                        
                        prev      l1   
                        1         4    -    5 
 -1 prev_head           |      
                        l2
                        1    -    2    -    3    -    6

                        prev      l1   
                        1         4    -    5 
 -1 prev_head           |      
                                  l2
                        1    -    2    -    3    -    6

                                  l1   
                        1         4    -    5 
 -1 prev_head           |      
                                  l2
                        1    -    2    -    3    -    6
                        prev
"""
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1:
            return l2
        if not l2:
            return l1
        prev_head = ListNode(-1)
        prev = prev_head
        while l1 or l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        return prev_head


if __name__ == '__main__':
    s = Solution()

    # [1, 2, 4]
    l1_3 = ListNode(4)
    l1_2 = ListNode(2, l1_3)
    l1_1 = ListNode(1, l1_2)
    #
    l1 = [l1_1, l1_2, l1_3]

    # [1, 3, 4]
    l2_3 = ListNode(4)
    l2_2 = ListNode(3, l2_3)
    l2_1 = ListNode(1, l2_2)
    #
    l2 = [l2_1, l2_2, l2_3]

    output = [1, 1, 2, 3, 4, 4]
    assert s.mergeTwoLists(l1_1, l2_1) == output
