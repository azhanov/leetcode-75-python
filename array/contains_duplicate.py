
''' ¯\_(ツ)_/¯ '''

class SolutionNaive(object):
    """
    Loop over every number and then then check all other numbers for a match.

    O(N^2) - time complexity
    O(1) - space complexity
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        for idx, num in enumerate(nums):
            for idx_inner, num_inner in enumerate(nums):
                if num == num_inner and idx != idx_inner:
                    return True

        return False


class SolutionBetter(object):
    """
    Sort and scan for duplicates between i and i+1 elements.

    O(N Log N) - time complexity
    O(1) - space complexity
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        for idx in range(len(nums)-1):
            if nums[idx] == nums[idx+1]:
                return True
        return False


class SolutionBetter(object):
    """
    Sort and scan for duplicates between i and i+1 elements.

    O(N Log N) - time complexity
    O(1) - space complexity
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums = sorted(nums)
        for idx in range(len(nums)-1):
            if nums[idx] == nums[idx+1]:
                return True
        return False


class SolutionBest(object):
    """
    Summary: Use Python Set data structure.

    O(N Log N) - time complexity
    O(1) - space complexity
    """
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        return len(nums) != len(set(nums))


if __name__ == "__main__":
    s = SolutionNaive()
    assert (s.containsDuplicate([]) is False)
    assert (s.containsDuplicate([1]) is False)
    assert (s.containsDuplicate([1, 2]) is False)
    assert (s.containsDuplicate([1, 2, 3, 1]) is True)
    assert (s.containsDuplicate([1, 2, 3, 4, 4]) is True)
    assert (s.containsDuplicate([1, 2, 3, 4]) is False)

    s = SolutionBetter()
    assert (s.containsDuplicate([]) is False)
    assert (s.containsDuplicate([1]) is False)
    assert (s.containsDuplicate([1, 2]) is False)
    assert (s.containsDuplicate([1, 2, 3, 1]) is True)
    assert (s.containsDuplicate([1, 2, 3, 4, 4]) is True)
    assert (s.containsDuplicate([1, 2, 3, 4]) is False)

    s = SolutionBest()
    assert (s.containsDuplicate([]) is False)
    assert (s.containsDuplicate([1]) is False)
    assert (s.containsDuplicate([1, 2]) is False)
    assert (s.containsDuplicate([1, 2, 3, 1]) is True)
    assert (s.containsDuplicate([1, 2, 3, 4, 4]) is True)
    assert (s.containsDuplicate([1, 2, 3, 4]) is False)
