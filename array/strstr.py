class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not haystack and not needle:
            return 0

        h_len = len(haystack)
        n_len = len(needle)
        """
        asdf - 4
        Hello World! - 12
                8 
        12 - 4 = 8
        """
        for idx in range(0, h_len - n_len + 1):
            if needle == haystack[idx:idx+n_len]:
                return idx
        return -1


if __name__ == '__main__':
    s = Solution()
    assert s.strStr(haystack="hello", needle="ll") == 2
    assert s.strStr(haystack="hello", needle="lo") == 3
    assert s.strStr(haystack="aaaaa", needle="bba") == -1
    assert s.strStr(haystack="", needle="") == 0
    assert s.strStr(haystack="", needle="a") == -1
