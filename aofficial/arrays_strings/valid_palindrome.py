def isPalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    l = 0
    r = len(s) - 1
    while l < r:
        while not s[l].isalnum() and l < r:
            l += 1
        while not s[r].isalnum() and l < r:
            r -= 1
        if s[l].lower() != s[r].lower():
            return False
        l += 1
        r -= 1
    return True


# print(isPalindrome("A man, a plan, a canal: Panama"))
#
# print(isPalindrome("race a car"))
#
print(isPalindrome("tar xx rat"))


print(isPalindrome(".,"))
