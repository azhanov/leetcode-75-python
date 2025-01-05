
word1 = 'abcxy'
word2 = 'pqr'

# find the smaller string and get its length
# iterate over a longer string
# get idx and char from a smaller string
# place both chars into a result
# append remaining


def version_1():
    result = ''

    for idx in range(len(word1)):
        result += word1[idx] + word2[idx]
        if len(word1) <= len(word2) and idx == len(word1) - 1:
            break
        elif len(word1) > len(word2) and idx == len(word2) - 1:
            break

    if len(word1) < len(word2):
        result += word2[idx+1:]
    elif len(word1) > len(word2):
        result += word1[idx+1:]

    print (result)


def version_2():
    result = ''
    len1 = len(word1)
    len2 = len(word2)
    p1 = p2 = 0
    while p1 < len1 or p2 < len2:
        if p1 < len1:
            result += word1[p1]
            p1 += 1
        if p2 < len2:
            result += word2[p2]
            p2 += 1
    print(result)


version_1()
version_2()
