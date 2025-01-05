class Solution(object):
    def containsDuplicateX(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))

    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        count_dict = {}
        for num in nums:
            if num in count_dict:
                return True
            else:
                count_dict[num] = num
        return False
