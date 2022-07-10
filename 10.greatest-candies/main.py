def kidsWithCandies(candies, extraCandies):
    maxCandy = max(candies)
    result = list()

    for i in range(len(candies)):
        sumCandy = extraCandies + candies[i]
        if sumCandy >= maxCandy:
            result.append(True)
        result.append(False)
    
    return result
    
    
    ## Solution2 return [ True if candy + extraCandies >= max(candies) else False for candy in candies]