# You're given a substring s of some cyclic string.
# What's the length of the smallest possible string that can be concatenated 
# to itself many times to obtain this cyclic string?


def cyclicString(s1):

    for answer in range(1, len(s1)):
        correct = True
        for position in range(answer, len(s1)):
            if s1[position] != s1[position - answer]:
                correct = False
        if correct:
            return answer
    return len(s1)
