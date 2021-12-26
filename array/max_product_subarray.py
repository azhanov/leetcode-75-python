class SolutionNaive(object):
    def maxProduct(self, nums):
        """
        O(N^2) - time complexity
        ON(1) - space complexity

        :type nums: List[int]
        :rtype: int
        """
        # Sanity check
        if not nums:
            return None

        overall_max = -float("inf")
        # Loop over every number
        for i in range(len(nums)):
            current_max = nums[i]
            cumulative_product = 1
            for j in range(i, len(nums)):
                cumulative_product = cumulative_product * nums[j]
                if cumulative_product > current_max:
                    current_max = cumulative_product
            if current_max > overall_max:
                overall_max = current_max
        return overall_max


class Solution(object):
    def maxProduct(self, nums):
        """
        1 2 3 0 4 5 6   : 0 disrupts the chain by resetting the product to zero no matter what the value was before
        1 2 3 -4        : negative turns the value into the opposite value, no good
        1 2 3 -4 5 -6   : however another negative will reverse it and make it good
        1 2 3 -4 5 0 -6 : and yet if there is zero before 2nd negative no reversal will occur


        O(N^2) - time complexity
        ON(1) - space complexity

        :type nums: List[int]
        :rtype: int
        """
        # Sanity check
        if not nums:
            return None

        # initialize to the first element
        max_so_far = nums[0]
        for i in range(1, len(nums)):
            max_so_far = max(max_so_far, max_so_far * nums[i])




if __name__ == '__main__':
    s = SolutionNaive()
    assert (s.maxProduct([2, 3, -2, 4]) == 6)
    assert (s.maxProduct([-2, 0, -1]) == 0)

