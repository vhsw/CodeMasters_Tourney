# We define the weakness of number x as the number of positive integers smaller than x that have more divisors than x.
# It follows that the weaker the number, the greater overall weakness it has. For the given integer n, you need to answer two questions:
# what is the weakness of the weakest numbers in the range [1, n]?
# how many numbers in the range [1, n] have this weakness?
# Return the answer as an array of two elements, where the first element is the answer to the first question, and the second element is the answer to the second question.

def weakNumbers(n):
    def d(n):
        if n == 1:
            return 1
        if n == 2:
            return 2
        counter = 1
        for i in range(2, n//2+1):
            if n % i == 0:
                counter += 1
        return counter+1

    weakness = []
    res = []
    for i in range(1, n + 1):
        divs = d(i)
        weakness.append(sum(e>divs for e in res))
        res.append(divs)
    return [max(weakness), weakness.count(max(weakness))]