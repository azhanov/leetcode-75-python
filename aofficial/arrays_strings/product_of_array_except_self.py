
def productExceptSelfON(nums):
    """
    nums:       1,   2,   3,   4
    prefix:     1,   1,   2,   6
    suffix:     24,  12,  4,   1
    answer:     24,  12,  8,   6
    :param nums:
    :return:
    """
    prefix = [0] * len(nums)
    suffix = [0] * len(nums)
    for idx, num in enumerate(nums):
        if idx == 0:
            prefix[idx] = 1
        else:
            prefix[idx] = prefix[idx-1] * nums[idx - 1]

    for idx in range(len(nums) - 1, -1, -1):
        if idx == len(nums) - 1:
            suffix[idx] = 1
        else:
            suffix[idx] = suffix[idx + 1] * nums[idx + 1]

    answer = [0] * len(nums)
    for idx in range(len(nums)):
        answer[idx] = prefix[idx] * suffix[idx]

    return answer


def productExceptSelf(nums):
    """
    nums:       1,   2,   3,   4
    prefix:     1,   1,   2,   6
    -----------------------------
                                |
    answer:     1,   1,   2,   6   right = 1
                          |
    answer:     1,   1,   8,   6   right = 4
                      |
    answer:     1,   12,   8,   6   right = 12
                |
    answer:     24,   12,   8,   6   right = 24
    answer:     24,  12,  8,   6

    suffix:     24,  12,  4,   1
    answer:
    :param nums:
    :return:
    """
    answer = [0] * len(nums)
    for idx, num in enumerate(nums):
        if idx == 0:
            answer[idx] = 1
        else:
            answer[idx] = answer[idx-1] * nums[idx - 1]

    right = 1

    for idx in range(len(nums) - 1, -1, -1):
        if idx == len(nums) - 1:
            right = 1
        else:
            right = right * nums[idx+1]
        answer[idx] = answer[idx] * right

    return answer

print(productExceptSelfON([1, 2, 3, 4]))
print(productExceptSelf([1, 2, 3, 4]))
