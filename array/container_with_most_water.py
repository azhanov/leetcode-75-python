class SolutionNaive(object):
    def maxArea(self, heights):
        """
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        for i in range(len(heights)):
            height_at_i = heights[i]
            for j in range(i+1, len(heights)):
                length = j - i
                height_at_j = heights[j]
                cur_area = min(height_at_i, height_at_j) * length
                if cur_area > max_area:
                    max_area = cur_area
        return max_area


class Solution(object):
    def maxArea(self, heights):
        """
        Two pointer
        :type height: List[int]
        :rtype: int
        """
        max_area = 0
        left = 0
        right = len(heights) - 1
        while left < right:
            area = min(heights[left], heights[right]) * (right-left)
            max_area = max(max_area, area)
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        return max_area


if __name__ == '__main__':
    sn = SolutionNaive()
    assert sn.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
    s = Solution()
    assert s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]) == 49
