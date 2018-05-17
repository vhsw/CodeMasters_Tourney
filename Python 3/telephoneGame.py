# You're given the array messages of message versions: message[0] is the statement the 1st person told the 2nd one (i.e. it is the initial phrase),
# message[1] is the statement the 2nd person told the 3rd one, etc.
# The last element of message corresponds to the phrase announced to the entire group by the last player.
# Find the index (0-based) of the first player who failed to reproduce exactly what she should have heard or identify that nobody made a mistake.


def telephoneGame(messages):
    for i, m in enumerate(messages):
        if m != messages[0]:
            return i
    return -1
