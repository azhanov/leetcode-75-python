from typing import List


class Solution:
    def sortByBitsX(self, arr: List[int]) -> List[int]:
        return sorted(arr, key=lambda x: (bin(x).count('1'), x))

    def sortByBits(self, arr: List[int]) -> List[int]:
        num_to_ones = {}
        # Iterate over all nums
        for num in arr:
            # For each num determine a number of 1
            count = self.calc_num_of_ones(num)
            # Add to dict
            num_to_ones[num] = count

        # Sort the dict first by value and if same - than by key
        num_to_ones_sorted = dict(sorted(num_to_ones.items(), key=lambda x: (x[1], x[0])))
        return list(num_to_ones_sorted.keys())

    def calc_num_of_ones(self, num: int) -> int:
        """
        Checking LSB
        :param num:
        :return:
        """
        count = 0
        while num:
            if num & 1 == 1:
                count += 1
            num = num >> 1
        print(count)
        return count


if __name__ == '__main__':
    s = Solution()
    #print(s.sortByBits([0,1,2,3,4,5,6,7,8]))
    print(s.sortByBits([10000, 10000]))