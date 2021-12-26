from collections import OrderedDict


class Solution(object):
    def firstNonRepeatingChar(self, input_string):
        chars_tracker = OrderedDict()
        for char in input_string:
            if char not in chars_tracker:
                chars_tracker[char] = 1
            else:
                chars_tracker[char] = chars_tracker[char] + 1

            for key, value in chars_tracker.items():
                if value == 1:
                    return key
            return None


if __name__ == "__main__":
    s = Solution()
    print(s.firstNonRepeatingChar('web rewrite'))