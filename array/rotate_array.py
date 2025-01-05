
from collections import deque

class Solution(object):

    def rotate1(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        stack = deque()
        # Slit
        # k = 3, len = 7, diff = 4
        # 1 2 3 4 5 6 7
        split = len(nums) - k
        base = nums[:split]
        rotation = nums[split:]
        for num in rotation:
            stack.append(num)
        while stack:
            val = stack.pop()
            base.insert(0, val)
        return base

    def rotate2(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        k = 3
        1, 2, 3, 4, 5, 6, 7
                   |
        5, 6, 7, 1, 2, 3, 4

        1, 2, 3, 4, 5, 6, 7, ?

        5: i = 4 -> i_new = 0
        6: i = 5 -> i_new = 1
        5: i_new = (i + K) % 7 = 7 % 7 = 0
        6: i_new = (i + k) % 7 = (5 + 3) % 7 = 1
        """
        spare = [0] * len(nums)
        for i in range(0, len(nums) - k):
            spare[i + k] = nums[i]
        for i in range(len(nums) - k, len(nums)):
            i_new = (i + k) % len(nums)
            spare[i_new] = nums[i]

        nums = spare
        return nums

    def rotate(self, nums, k):
        # if so some k is larger than the nums length
        k = k % len(nums)

        l, r = 0, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = k, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

        return nums


if __name__ == '__main__':
    s = Solution()
    print(s.rotate([1,2,3,4,5,6,7], k = 3))
    print(s.rotate1([1,2,3,4,5,6,7], k = 3))
    print(s.rotate2([1,2,3,4,5,6,7], k = 3))