

class SolutionNaive(object):
    """
    Iterate over every number and then again in the inner loop, searching for a matching one.

    O(N^2) time complexity
    O(1) space complexity
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for idx, num in enumerate(nums):
            for idx_inner, num_inner in enumerate(nums):
                if idx_inner != idx and num_inner + num == target:
                    return [idx, idx_inner]


class SolutionBetter(object):
    """
    Two pass solutions where first pass caches numbers and their corresponding index
    and the second one looks up an complementing value from dict rather then doing a full scan

    O(N) time complexity
    O(N) space complexity
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_nums = {}
        for idx in range(len(nums)):
            seen_nums[nums[idx]] = idx

        for idx in range(len(nums)):
            complement = target - nums[idx]
            if complement in seen_nums and seen_nums[complement] != idx:
                return [idx, seen_nums[complement]]


class SolutionBest(object):
    """
    Single pass solution were a value is cached in dict as we pass through and also we check if a complementary
    value is already present in dict.

    O(N) time complexity
    O(N) space complexity
    """
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        seen_nums = {}

        for idx, num in enumerate(nums):
            complement = target - num
            if complement in seen_nums and seen_nums[complement] != idx:
                return [seen_nums[complement], idx]
            seen_nums[num] = idx


if __name__ == "__main__":
    s = SolutionNaive()
    assert ([0, 1] == s.twoSum([2, 7, 11, 15], 9))
    s = SolutionBetter()
    assert ([0, 1] == s.twoSum([2, 7, 11, 15], 9))
    s = SolutionBest()
    assert ([0, 1] == s.twoSum([2, 7, 11, 15], 9))
