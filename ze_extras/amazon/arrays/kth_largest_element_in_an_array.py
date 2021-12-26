class SolutionNaive(object):
    def findKthLargest(self, nums, k):
        """
        O(N long(N)) - space complexity (sorting)
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not nums or not k:
            return None
        nums = sorted(nums)
        return nums[-k]


import heapq
class SolutionBetter(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        heapq.heapify(nums)
        res = []
        #for i in range(len(nums)-1, -1, -1):
        hv = heapq.heappop(res)
        return hv


class Solution(object):
    def findKthLargest(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """


if __name__ == '__main__':
    s = SolutionNaive()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4

    s = SolutionBetter()
    assert s.findKthLargest([3, 2, 1, 5, 6, 4], 2) == 5
    assert s.findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4) == 4
