
from collections import Counter
from typing import List


class Solution(object):

    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        result = []
        counter = Counter(nums)
        sorted_counter = dict(sorted(counter.items(), key=lambda e: e[1], reverse=True))
        keys = list(sorted_counter.keys())
        for idx in range(k):
            result.append(keys[idx])
        return result

    def topKFrequentHeapBucketSort(self, nums: List[int], k: int) -> List[int]:
        counter = {}
        for num in nums:
            counter[num] = 1 + counter.get(num, 0)
        freqs = [[] for i in range(len(nums) + 1)]
        for num, freq in counter.items():
            bucket = freqs[freq]
            bucket.append(num)
        print(freqs)
        result = []
        for idx in range(len(nums), 0, -1):
            print(idx)
            # for n in freqs[idx]:
            #     result.append(n)
            #     if len(result) == k:
            #         return result


if __name__ == '__main__':
    s = Solution()
    print(s.topKFrequentHeapBucketSort(nums = [1,1,1,2,2,3], k = 2))
    #print(s.topKFrequent([4, 1, -1, 2, -1, 2, 3], 2))
