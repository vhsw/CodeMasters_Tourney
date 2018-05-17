# Imagine the following situation for a given integers n and k. There are n people standing in a circle.
# They are numbered from 1 through n in clockwise direction.
# The counting out begins at person #1 and continues around the circle in a clockwise direction.
# In each step, k-1 people are skipped and the next person is removed from the circle.
# The elimination proceeds around the circle (which is becoming smaller and smaller as people get removed), until only one person remains, who is announced a winner.
# The task is to find the place in the initial circle that would guarantee a win.


def josephusProblem(n, k):
    def remove(n, k):
        if n == 1:
            return 0
        return (remove(n-1, k)+k) % n

    return remove(n, k) + 1
