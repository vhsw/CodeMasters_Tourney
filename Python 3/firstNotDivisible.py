# Find the smallest integer not less than the given limit
# which is not divisible by any of the integers from the given array.


def firstNotDivisible(divisors, start):
    while True:
        if all(map(lambda n: start%n != 0, divisors)):
            return start
        start += 1