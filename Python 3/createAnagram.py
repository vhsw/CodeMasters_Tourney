# You are given two strings s and t of the same length, consisting
# of uppercase English letters. Your task is to find the minimum number
# of "replacement operations" needed to get some anagram of the string t from the string s.
# A replacement operation is performed by picking exactly one character from the string s 
# and replacing it by some other character.


def createAnagram(s, t):

    cnt1 = [0] * 26
    cnt2 = [0] * 26
    for i in range(len(s)):
        cnt1[ord(s[i]) - ord('A')] += 1
        cnt2[ord(t[i]) - ord('A')] += 1

    ans = 0
    for i in range(26):
        ans += abs(cnt1[i] - cnt2[i])

    return  ans//2

