class SolutionNaive(object):
    def climbStairs(self, n):
        """
        O(N^2) - time complexity, size of a tree
        O(N) - space complexity

        :type n: int
        :rtype: int
        """
        return self.climb_stairs(0, n)

    def climb_stairs(self, i, n):
        if i > n:
            return 0
        if i == n:
            return 1
        return self.climb_stairs(i + 1, n) + self.climb_stairs(i + 2, n)


class SolutionBetter(object):
    def climbStairs(self, n):
        """
        O(N) - time complexity, tree pruned to N
        O(N) - space complexity

        :type n: int
        :rtype: int
        """
        memo = [0] * n
        return self.climb_stairs(0, n, memo)

    def climb_stairs(self, i, n, memo):
        if i > n:
            return 0
        if i == n:
            return 1
        if memo[i] > 0:
            return memo[i]
        memo[i] = self.climb_stairs(i + 1, n, memo) + self.climb_stairs(i + 2, n, memo)
        return memo[i]


class Solution(object):
    def climbStairs(self, n):
        """
        O(N) - time complexity, tree pruned to N
        O(N) - space complexity

        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]


if __name__ == '__main__':
    """                           _
                _               _|
              _|              _|
          o _|            o _|
    """
    s = SolutionNaive()
    assert (s.climbStairs(2) == 2)
    assert (s.climbStairs(3) == 3)

    s = SolutionBetter()
    assert (s.climbStairs(2) == 2)
    assert (s.climbStairs(3) == 3)
    assert (s.climbStairs(6) == 13)

    s = Solution()
    assert (s.climbStairs(2) == 2)
    assert (s.climbStairs(3) == 3)
    assert (s.climbStairs(6) == 13)
