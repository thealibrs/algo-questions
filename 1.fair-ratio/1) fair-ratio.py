"""
You are the benevolent ruler of Rankhacker Castle, 
and today you're distributing bread. Your subjects are in 
a line, and some of them already have some loaves. 
Times are hard and your castle's food stocks are dwindling, 
so you must distribute as few loaves as possible according to the following rules:

- Every time you give a loaf of bread to some person, 
you must also give a loaf of bread to the person immediately 
in front of or behind them in the line (i.e., i+1 persons or i-1).

- After all the bread is distributed, each person must 
have an even number of loaves.Given the number of loaves already 
held by each citizen, find and print the minimum number of loaves 
you must distribute to satisfy the two rules above. If this is not possible, print NO.

"""

def fairRations(B):
    given_bread = 0

    for i in range(len(B)-1):
      if B[i] % 2 != 0:
        B[i] += 1
        B[i+1] += 1
        given_bread += 2
    
    if B[-1] % 2 == 1:
      return "NO"

    return given_bread