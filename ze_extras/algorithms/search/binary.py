

def binary_search(in_list, search_term):
    left = 0
    right = len(in_list) - 1
    while left <= right:
        mid = (left + right)//2
        if in_list[mid] < search_term:
            left = mid + 1
        elif in_list[mid] > search_term:
            right = mid - 1
        else:
            return mid
    return None


def binary_search_rec(in_list, search_term, left, right):
    if right < left:
        return None
    else:
        mid = (right+left)//2
        if in_list[mid] < search_term:
            # search the right side
            return binary_search_rec(in_list, search_term, left + 1, right)
        elif in_list[mid] > search_term:
            # search to the left
            return binary_search_rec(in_list, search_term, left, right - 1)
        else:
            return mid


search_term = 3
in_list = list(range(10))
in_list = [0, 1, 2, 3, 5, 6, 7, 8, 9]
print(binary_search(in_list, search_term))
print(binary_search_rec(in_list, search_term, 0, len(in_list) - 1))

search_term = 12
print(binary_search(in_list, search_term))
print(binary_search_rec(in_list, search_term, 0, len(in_list) - 1))
