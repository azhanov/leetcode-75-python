class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        left = 0
        right = len(numbers) - 1
        while left < right:
            two_sum = numbers[left] + numbers[right]
            if two_sum == target:
                return [left+1, right+1]
            elif two_sum > target:
                right -= 1
            else:
                left += 1


if __name__ == '__main__':
    s = Solution()
    assert s.twoSum([2, 7, 11, 15], 9) == [1, 2]
    assert s.twoSum([2,3,4], 6) == [1, 3]
    assert s.twoSum([-1,0], -1) == [1, 2]
