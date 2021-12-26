class Solution:
    def intToRoman(self, num: int) -> str:
        """
        Greedy approach: from left to right, what's the max value that can be fit into the largest number
        :param num:
        :return:
        """
        digits = [(1000, "M"), (900, "CM"), (500, "D"), (400, "CD"), (100, "C"),
                  (90, "XC"), (50, "L"), (40, "XL"), (10, "X"), (9, "IX"),
                  (5, "V"), (4, "IV"), (1, "I")]
        roman_digits = []
        # Loop through each symbol
        for val, symbol in digits:
            if num == 0:
                break
            count, num = divmod(num, val)
            roman_digits.append(symbol * count)
        return "".join(roman_digits)


if __name__ == '__main__':
    s = Solution()
    assert s.intToRoman(3) == 'III'
    assert s.intToRoman(4) == 'IV'
    assert s.intToRoman(9) == 'IX'
    assert s.intToRoman(58) == 'LVIII'
    assert s.intToRoman(1994) == 'MCMXCIV'
