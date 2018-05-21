# You are processing the results of an online poll and
# your task is to exclude answers that might have been
# submitted by bots from the final results.
# The poll consists of three questions, the answer to each one is either true or false.
# You think that a response is suspicious (i.e. it might be from a bot)
# if all of the submissions are the same.
# Given a response list to each of the three questions,
# check if it might have come from a bot using the above described criteria.


def isSuspiciousRespondent(ans1, ans2, ans3):
    return (ans1 and ans2 and ans3) or (ans1 and not ans2 and not ans3)
