# Given an integer bound, find the maximal integer n such that 1 + 2 + ... + n ≤ bound.


def sumBelowBound(bound):
    
    s = 0
    i = 0
    while True:
        s+=i
        print(s, i)
        
        if s>bound:
            return i-1
        i+=1