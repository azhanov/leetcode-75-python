from collections import defaultdict


class SolutionGood(object):
    def groupAnagrams(self, strs):
        """
        O(N * k log(k) - time complexity, where k-max str length in strs and N is strs length
        O(N * k) - space complexity
        :param strs:
        :return:
        """
        result = []
        tracker = defaultdict(list)
        for s in strs:
            str_as_sorted_tuple = tuple(sorted(s))
            if str_as_sorted_tuple in tracker:
                (tracker[str_as_sorted_tuple]).append(s)
            else:
                tracker[str_as_sorted_tuple] = [s]
        for key, value in tracker.items():
            result.append(value)
        return result


class Solution(object):
    def groupAnagrams(self, strs):
        """
        O(N * k + N*26) - time complexity, where k-max str length in strs and N is strs length
         O(N * k + N*26) - space complexity
        :param strs:
        :return:
        """
        tracker = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            tracker[tuple(count)].append(s)
        return tracker.values()


if __name__ == '__main__':
    s = Solution()
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    output = [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]]
    print(s.groupAnagrams(strs))
    assert s.groupAnagrams(strs) == output

    # strs = [""]
    # output = [[""]]
    # assert s.groupAnagrams(strs) == output
    #
    # strs = ["a"]
    # output = [["a"]]
    # assert s.groupAnagrams(strs) == output
