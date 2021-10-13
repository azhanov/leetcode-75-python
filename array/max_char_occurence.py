

def find_most_frequent_char(input_string):
    """
    Given a string, find and return a character with the most frequent occurrence.
    If more then one char have the same largest occurrence, the first one will be returned.
    If an empty string is send, the function returns None
    :param input_string:
    :return: char
    """
    # Sanity check
    if not input_string:
        return None
    # Get the characters occurrence counts
    counts = {}
    for char in input_string:
        if char not in counts:
            counts[char] = 0
        counts[char] += 1
    # Now, that we have all the counts - find the most frequest
    max_occurrence_char = ''
    max_occurrence_char_count = -1
    for char, count in counts.items():
        if count > max_occurrence_char_count:
            max_occurrence_char_count = count
            max_occurrence_char = char
    return max_occurrence_char


#print(find_most_frequent_char(input_string="aabbbbccccdd"))
print(find_most_frequent_char(input_string=None))
