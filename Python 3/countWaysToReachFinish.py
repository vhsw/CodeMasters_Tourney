# Consider a sequence of cells which are either free or blocked. The distance between each pair of consecutive cells is 1. Initially you are standing in the first cell (1-based), you may visit only free cells, and your goal is to reach the last cell (both the first and the last cells are free). You move between cells only by jumping. You can make jumps of any integer length and in either direction with only two restrictions: you cannot make two jumps of equal length and you cannot jump out of the cell sequence.
# Given a cell sequence, count the number of such sequences of jumps that after following them you will end up at the last cell. Two sequences of jumps are considered different either if they consist of different number of jumps or if for some i, the ith jumps of these two sequences differ.


def countWaysToReachFinish(cells):

    n = len(cells)
    MAX_MASK = 1 << n

    # dp[m][k] - the number of ways to reach the k-th cell using jumps
    # that are marked in the mask m.
    dp = []
    was = []
    for m in range(MAX_MASK):
        dp.append([0] * n)
        was.append([False] * n)
    dp[0][0] = 1
    was[0][0] = True

    def get(m, k):
        if k < 0 or k >= n or not cells[k]:
            return 0
        if was[m][k]:
            return dp[m][k]
        for i in range(1, n):
            if (m >> i & 1) == 1:
                dp[m][k] += get(m ^ (1 << i), k - i)
                dp[m][k] += get(m ^ (1 << i), k + i)
        was[m][k] = True
        return dp[m][k]

    ans = 0
    for m in range(0, MAX_MASK):
        ans += get(m, n - 1)

    return ans
