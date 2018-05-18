# Inspired by AD&D (Advanced Dungeons & Dragons),
# you decide to invent your own role playing game.
# You're going to play it with your two best friends,
# so it will be for three players only.
# A brand new game needs a distinctive feature, and here it goes:
# each player uses their own die (in other words,
# each die has its own series of six numbers written on its sides),
# and these three dice form a nontransitive set.
# A set of dice is nontransitive if it contains three dice, A, B, and C,
# with the property that A beats B 
# (it rolls higher than B more times than B rolls higher than A),
# and B beats C, but it is not true that A beats C.
# In order to find the set of dice suitable for your game,
# you repeatedly generate random triplets of dice and then checkif they are nontransitive.
# Since it is too boring to check this manually each time,
# your goal is to implement a function that automates the process,
# i.e. for the given numbers on the sides of three dice,
# you should verify that this set of dice is nontransitive.


from itertools import permutations


def nontransitiveDice(dice):
    def beats(x1, x2):
        ans = 0
        for x in x1:
            for y in x2:
                if x > y:
                    ans += 1
                elif x < y:
                    ans -= 1
        return ans > 0

    for p in permutations(range(3)):
        if beats(dice[p[0]], dice[p[1]]) and \
           beats(dice[p[1]], dice[p[2]]) and \
           not beats(dice[p[0]], dice[p[2]]):
            return True
    return False
