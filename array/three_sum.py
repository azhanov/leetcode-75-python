class Solution:
    def threeSum(self, nums):
        """
        O(nlogn + n^2) ~ O(n^2) - time complexity
        O(n) - space complexity
        :param nums:
        :return:
        """
        result = []
        nums.sort()
        for idx in range(len(nums)):
            if nums[idx] > 0:
                break
            if idx == 0 or nums[idx] != nums[idx - 1]:
                self.twoSum(nums, idx, result)
        return result

    def twoSum(self, nums, idx, result):
        left = idx + 1
        right = len(nums) - 1
        while left < right:
            sum = nums[idx] + nums[left] + nums[right]
            if sum < 0:
                left += 1
            elif sum > 0:
                right -= 1
            else:
                result.append([nums[idx], nums[left], nums[right]])
                left += 1  # left used up - move right to the next value
                right -= 1  # right are used up - move left to the next values
                while left < right and nums[left] == nums[left-1]:
                    left += 1


class SolutionAlt:
    def threeSum(self, nums):
        """
        O(nlogn + n^2) ~ O(n^2) - time complexity
        O(n) - space complexity
        :param nums:
        :return:
        """
        result = []
        nums.sort()
        for idx in range(len(nums)):
            if nums[idx] > 0:
                break
            if idx == 0 or nums[idx] != nums[idx - 1]:
                self.twoSum(nums, idx, result)
        return result

    def twoSum(self, nums, idx, result):
        seen_nums = {}
        j = idx + 1
        while j < len(nums):
            compliment = -nums[idx] - nums[j]
            if compliment in seen_nums:
                result.append()


if __name__ == '__main__':
    s = Solution()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2],[-1, 0, 1]]
    assert s.threeSum([]) == []
    assert s.threeSum([0]) == []

    s = SolutionAlt()
    assert s.threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2],[-1, 0, 1]]
    assert s.threeSum([]) == []
    assert s.threeSum([0]) == []
