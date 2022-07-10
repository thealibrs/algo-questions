def reverseInteger(num):
    if num != 0: # check if num is zero
        if num % 10: # check if num has zero number at the end
          if num > 0: # if num is positive integer
            return int(str(num)[::-1]) # return reversed version
          else: # if num is negative integer
            return int("-"+(str(num)[1:])[::-1]) # return reversed version plus insert minus sign in front 
        return str(num)[:len(str(num))][::-1] 
    return 0