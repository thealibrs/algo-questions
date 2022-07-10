def reverseInteger(num):
    str_x = str(num)
    if num != 0: # check if num is zero
        if num > 0: # if num is positive integer         
          return int(str_x[::-1]) # return reversed version
        else: # if num is negative integer
          return int("-"+(str_x[1:])[::-1]) # return reversed version plus insert minus sign in front 
    return 0