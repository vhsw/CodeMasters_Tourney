# The NAND operation (also known as a Sheffer stroke) is an operation on two logical values.
# It produces true, if - and only if - at least one of the operands is false.

def shefferStroke(a, b):
    return not (a and b)