"""
Fibonacci sequence:
0, 1, 1, 2, 3, 5, 8, 13, 21, 3

i=0 : 0
i=1: 1
i=2: 1
i=3: (i-1) + (i-2) -> 2
i=4: (i-1) + (i-2) -> 3
i=5: (i-1) + (i-2) -> 5
...
i=n: (i-1) + (i-2)
"""


class Solution(object):
    def calc(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        if n == 2:
            return [0, 1, 1]
        f_seq = [0, 1, 1]
        for i in range(3, n+1):
            f_seq.append(f_seq[i-1] + f_seq[i-2])
        return f_seq


if __name__ == '__main__':
    s = Solution()
    print(s.calc(10))
