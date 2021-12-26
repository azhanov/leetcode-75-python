

class SolutionNaive(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_subarray = -float("inf")
        for i in range(len(nums)):
            current_subarry = 0
            for j in range(i, len(nums)):
                current_subarry += nums[j]
                max_subarray = max(max_subarray, current_subarry)
        return max_subarray


class SolutionBest(object):
    def maxSubArray(self, nums):
        """
        Summary: each idx local max is either: (idx val + previous max) or idx val. Whichever is greater. In other
        words if a new val is making max worse, then just consider the val going forward and thus starting NEW SEQUENCE!

        Kadane algorithm
        https://medium.com/@rsinghal757/kadanes-algorithm-dynamic-programming-how-and-why-does-it-work-3fd8849ed73d#id_token=eyJhbGciOiJSUzI1NiIsImtpZCI6IjhkOTI5YzYzZmYxMDgyYmJiOGM5OWY5OTRmYTNmZjRhZGFkYTJkMTEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL2FjY291bnRzLmdvb2dsZS5jb20iLCJuYmYiOjE2MzI3Mjg2OTYsImF1ZCI6IjIxNjI5NjAzNTgzNC1rMWs2cWUwNjBzMnRwMmEyamFtNGxqZGNtczAwc3R0Zy5hcHBzLmdvb2dsZXVzZXJjb250ZW50LmNvbSIsInN1YiI6IjExMjg4NDYxMjI1NjcxNjQ4NjkzOSIsImVtYWlsIjoiYXpoYW5vdkBnbWFpbC5jb20iLCJlbWFpbF92ZXJpZmllZCI6dHJ1ZSwiYXpwIjoiMjE2Mjk2MDM1ODM0LWsxazZxZTA2MHMydHAyYTJqYW00bGpkY21zMDBzdHRnLmFwcHMuZ29vZ2xldXNlcmNvbnRlbnQuY29tIiwibmFtZSI6IkFsZXggWiIsInBpY3R1cmUiOiJodHRwczovL2xoMy5nb29nbGV1c2VyY29udGVudC5jb20vYS9BQVRYQUp3eUVWMnQtMWp4Y2dTOVBZTk9mbGl6b0V4b0NLMGxGWVVHY0tSZD1zOTYtYyIsImdpdmVuX25hbWUiOiJBbGV4IiwiZmFtaWx5X25hbWUiOiJaIiwiaWF0IjoxNjMyNzI4OTk2LCJleHAiOjE2MzI3MzI1OTYsImp0aSI6ImY1ZTdkMWY5N2JiYTMwOGY0NmJiY2Y1YjUyNTUxMTA5Njg4NTc4YTcifQ.WCEWEbI7lQ5-agX2GgLCCljbOuG4moWEcxwrrcxKtIgN_8fI_ZZZ6LO8UdxjIKqQinbufXQy-6KgFC_FbVHDV2CeHLffA7VesrBXTB9YXvCVnHcy3t2GUr2dqDy3dMl5Gh6c4mPxqsbHPFy_LB3vx0h96pEkrfhdMuR33ufV1UVthGFoIF771JVMncbcQrhzOo5DriUQTVBwxXVv4FAcoIhR6wzuZhDG4VjdZElm9VZOhD85tDfkY9b-0vqGJPdyFMTqqkM92UmAXth0JtMmJqRSPZhKeqtLyfIj3327ij9_e9plRMu53vupP2Lek1eaYoX4UxmJn8ymMzPZMjVfsw
        :param nums:
        :return:
        """
        max_sum = float("-inf")
        curr_max = 0
        for num in nums:
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)
        return max_sum


if __name__ == "__main__":

    s = SolutionNaive()
    assert (s.maxSubArray([-2, 1, -3, 4, - 1, 2, 1, -5, 4]) == 6)
    assert (s.maxSubArray([-1]) == -1)

    s = SolutionBest()
    assert (s.maxSubArray([-2, 1, -3, 4, - 1, 2, 1, -5, 4]) == 5)
    assert (s.maxSubArray([-1]) == -1)
