
class SolutionNaive(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0

        overall_max_count = 0
        for i in range(len(s)):
            for j in range(i, len(s)):
                ss = s[i:j+1]
                if SolutionNaive.has_no_duplciates(ss):
                    overall_max_count = max(overall_max_count, len(ss))
        return overall_max_count

    @staticmethod
    def has_no_duplciates(ss):
        return len(ss) == len(set(ss))


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s:
            return 0
        left = right = 0
        overall_max_count = 0
        # Maps a char to it's last seen position
        seen = dict()
        for right in range(len(s)):
            if s[right] not in seen:
                overall_max_count = max(overall_max_count, right-left+1)
            else:
                if seen[s[right]] < left:
                    overall_max_count = max(overall_max_count, right-left+1)
                else:
                    left = seen[s[right]] + 1
            seen[s[right]] = right
        return overall_max_count


if __name__ == '__main__':
    s = SolutionNaive()
    assert (s.lengthOfLongestSubstring(' ') == 1)
    assert (s.lengthOfLongestSubstring('abcabcbb') == 3)
    assert (s.lengthOfLongestSubstring('bbbbb') == 1)
    assert (s.lengthOfLongestSubstring('pwwkew') == 3)
    assert (s.lengthOfLongestSubstring('') == 0)

    s = Solution()
    assert (s.lengthOfLongestSubstring(' ') == 1)
    assert (s.lengthOfLongestSubstring('abcabcbb') == 3)
    assert (s.lengthOfLongestSubstring('bbbbb') == 1)
    assert (s.lengthOfLongestSubstring('pwwkew') == 3)
    assert (s.lengthOfLongestSubstring('') == 0)
