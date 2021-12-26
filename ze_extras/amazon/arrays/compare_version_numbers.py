class Solution(object):
    def compareVersion(self, version1, version2):
        """
        O(N+M+max(N,M)), where NN and MM are lengths of input strings.
        O(N+M) to store arrays nums1 and nums2.
        :type version1: str
        :type version2: str
        :rtype: int
        """

        if not version1 and not version2:
            return 0

        v1_vals = version1.split('.')
        v2_vals = version2.split('.')
        self.pad_to_same_length_if_needed(v1_vals, v2_vals)

        for i in range(len(v1_vals)):
            comp1 = self.remove_leading_zeros(v1_vals[i])
            comp2 = self.remove_leading_zeros(v2_vals[i])
            if comp1 < comp2:
                return -1
            elif comp1 > comp2:
                return 1
        return 0

    def pad_to_same_length_if_needed(self, v1_vals, v2_vals):
        if len(v1_vals) == len(v2_vals):
            return
        elif len(v1_vals) > len(v2_vals):
            delta = len(v1_vals) - len(v2_vals)
            for i in range(delta):
                v2_vals.append('0')
        else:
            delta = len(v2_vals) - len(v1_vals)
            for i in range(delta):
                v1_vals.append('0')

    def remove_leading_zeros(self, val):
        if not val:
            return 0
        val = val.lstrip('0')
        if len(val) == 0:
            return 0
        else:
            return int(val)


class SolutionSameAsAboveButMorePythonic:
    def compareVersion(self, version1: str, version2: str) -> int:
        nums1 = version1.split('.')
        nums2 = version2.split('.')
        n1, n2 = len(nums1), len(nums2)

        # compare versions
        for i in range(max(n1, n2)):
            i1 = int(nums1[i]) if i < n1 else 0
            i2 = int(nums2[i]) if i < n2 else 0
            if i1 != i2:
                return 1 if i1 > i2 else -1

        # the versions are equal
        return 0


if __name__ == '__main__':

    s = Solution()
    assert s.compareVersion("1.01", "1.001") == 0
    assert s.compareVersion("1.0", "1.0.0") == 0
    assert s.compareVersion("0.1", "1.1") == -1
    assert s.compareVersion("1.0.1", "1") == 1
    assert s.compareVersion("7.5.2.4", "7.5.3") == -1

    s = SolutionSameAsAboveButMorePythonic()
    assert s.compareVersion("1.01", "1.001") == 0
    assert s.compareVersion("1.0", "1.0.0") == 0
    assert s.compareVersion("0.1", "1.1") == -1
    assert s.compareVersion("1.0.1", "1") == 1
    assert s.compareVersion("7.5.2.4", "7.5.3") == -1
