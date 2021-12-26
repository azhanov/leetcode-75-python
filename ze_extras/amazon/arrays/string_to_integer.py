class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        number = 0
        MAX_NUM = 2 ** 31 - 1
        MIN_NUM = -2 ** 31

        if not s:
            return number

        digits = ''
        number_positive = True
        processed_sign = False
        reached_numbers = False
        for char in s:
            if not reached_numbers and not processed_sign:
                # at the beginning, skip spaces if any
                if char.isspace():
                    continue
                # if found a minus - set the number to be negative
                elif char == '-':
                    number_positive = False
                elif char == '+':
                    continue
                # found a letter before digits - exit
                elif not ('0' <= char <= '9'):
                    break
                else:
                    digits += char
                    reached_numbers = True
            else:
                # processing numbers
                if char.isdecimal():
                    digits += char
                else:
                    break

        for idx, char in enumerate(digits[::-1]):
            char_to_digit = ord(char) - ord('0')
            number = number + (10 ** idx * char_to_digit)
            if number > MAX_NUM // 10:
                if number_positive:
                    return MAX_NUM
                else:
                    return MIN_NUM

        if not number_positive:
            number = number * -1

        return number


class SolutionOrig:
    def myAtoi(self, s: str) -> int:

        MAX_NUM = 2 ** 31 - 1
        MIN_NUM = -2 ** 31

        # trim the leading white space first
        s = s.strip()
        sign = 1
        index = 0
        num = 0
        if not s:
            return num

        if s[0] == '-':
            sign = -1
            index += 1
        elif s[0] == '+':
            index += 1

        while index < len(s) and s[index].isdigit():
            curr_digit = ord(s[index]) - ord('0')
            if num > MAX_NUM // 10 or (
                    num == MAX_NUM // 10 and curr_digit > 7):  # here we do the check before adding current digit
                return MAX_NUM if sign == 1 else MIN_NUM
            num = num * 10 + curr_digit
            index += 1

        num = sign * num
        return num


class SolutionDFA:
    def myAtoi(self, str: str) -> int:
        value, state, pos, sign = 0, 0, 0, 1

        if len(str) == 0:
            return 0

        while pos < len(str):
            current_char = str[pos]
            if state == 0:
                if current_char == " ":
                    state = 0
                elif current_char == "+" or current_char == "-":
                    state = 1
                    sign = 1 if current_char == "+" else -1
                elif current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 1:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    return 0
            elif state == 2:
                if current_char.isdigit():
                    state = 2
                    value = value * 10 + int(current_char)
                else:
                    break
            else:
                return 0
            pos += 1

        value = sign * value
        value = min(value, 2 ** 31 - 1)
        value = max(-(2 ** 31), value)

        return value
"""
  2147483647
  214748364
  
  214748364
  234567891
  
  2345678912
  234567891
  
  
  
  2147483647
  214748364
  
  214748364
  214748364
  
  2147483646
  214748364

"""
if __name__ == '__main__':
    MAX_NUM = 2 ** 31 - 1
    # print(5//2.1)
    print(MAX_NUM)
    # print(MAX_NUM // 10)

    s = SolutionOrig()
    assert (s.myAtoi('42') == 42)
    assert (s.myAtoi('    -42') == -42)
    assert (s.myAtoi('4193 with words') == 4193)
    assert (s.myAtoi('words and 987') == 0)
    #                 2147483647
    assert (s.myAtoi('2147483647') == 2147483647)
    #                   2147483647
    assert (s.myAtoi('-91283472332') == (-2 ** 31))

    s = SolutionDFA()
    assert (s.myAtoi('42') == 42)
    assert (s.myAtoi('    -42') == -42)
    assert (s.myAtoi('4193 with words') == 4193)
    assert (s.myAtoi('words and 987') == 0)
    #                 2147483647
    assert (s.myAtoi('2147483647') == 2147483647)
    #                   2147483647
    assert (s.myAtoi('-91283472332') == (-2 ** 31))
