

def execute(candies, extraCandies):
    result = []
    max_can = candies[0]
    for candy in candies:
        if candy > max_can:
            max_can = candy
    for idx, candy in enumerate(candies):
        if candy + extraCandies >= max_can:
            result.append(True)
        else:
            result.append(False)

    return result
