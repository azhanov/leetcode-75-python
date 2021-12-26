class SolutionMine:
    """
    Subtracting:
    IV - 4
    IX - 9
    XL - 40
    XC - 90
    CD - 400
    CM - 900
    """
    def romanToInt(self, s: str) -> int:
        result = 0
        if not s:
            return result
        roman = {'M': 1000, 'D': 500, 'C': 100, 'L': 50, 'X': 10, 'V': 5, 'I': 1}
        subtract_patterns = {"IV": 4, "IX": 9, "XL": 40, "XC": 90, "CD": 400, "CM": 900}
        prev_char = " "
        for idx in range(len(s)-1, -1, -1):
            char = s[idx]
            subtract_candidate = char + prev_char
            if subtract_candidate in subtract_patterns:
                result += subtract_patterns[subtract_candidate]
                prev_char = ' '
            else:
                if prev_char != ' ':
                    result += roman[prev_char]
                if idx == 0:
                    result += roman[char]
                prev_char = char

        return result


class Solution(object):
    def romanToInt(self, s):
        """
        An observation: subtraction occurs only if a current char (as a number) is less then previous one.
        :type s: str
        :rtype: int
        """
        values = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }
        total = values.get(s[-1])
        for i in reversed(range(len(s) - 1)):
            if values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]
        return total


if __name__ == '__main__':
    s = SolutionMine()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    assert s.romanToInt("MMMXLV") == 3045

    s = Solution()
    assert s.romanToInt("III") == 3
    assert s.romanToInt("IV") == 4
    assert s.romanToInt("IX") == 9
    assert s.romanToInt("LVIII") == 58
    assert s.romanToInt("MCMXCIV") == 1994
    assert s.romanToInt("MMMXLV") == 3045
