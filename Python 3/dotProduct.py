# Given two 3D vectors, find their dot product.


def dotProduct(v1, v2):
    return sum(i*j for i,j in  zip(v1,v2))