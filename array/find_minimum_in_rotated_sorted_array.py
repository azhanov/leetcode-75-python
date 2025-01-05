class Solution:
    """
    Starting list
    0, 1, 2, 3, 4, 5, 6, 7

    Rotated array: binary search
    4, 5, 6, 7, 0, 1, 2, 3
    L        M           R

             T > mid : go right
    4, 5, 6, 7, 0, 1, 2, 3
    L     M              R
             L
    4, 5, 6, 7, 0, 1, 2, 3
             L     M     R

       T < mid:  go left
    4, 5, 6, 7, 0, 1, 2, 3
    L     M              R
       R



    """

    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums) - 1

        while l <= r:
            mid = (l + r) // 2

            if nums[mid] == targer:
                return nums[mid]

            # On the left side
            if nums[mid] >= num[l]:
                # Target to the right
                if target > nums[mid]:
                    # Simply go right
                    l = mid + 1
                elif target < nums[mid]:
                    r = mid - 1
                else:

            else:
        # On the right side
