# It is a common tradition to play Hangman game during classes. Too bad it's difficult 
# to do so if you and your friend sit far from each other.
# You, however, came up with a great idea.
# First, you write down a word. After that your friend writes down distinct 
# letters and passes the list with them to you.
# Now you look at the letters in his list one by one. 
# If the current letter is present in your word, you erase all occurrences
# of this letter from it, otherwise you call it a miss.
# If you erase the entire word before 6 misses, then your friend wins.
# If you count 6 misses or run out of letters before the word is erased, you win.
# Given the word you made and your friend's letters, return true if he wins or false otherwise.


def hangman(word, letters):

    neededLetters = [False] * 26
    need = 0
    for i in range(len(word)):
        c = ord(word[i]) - ord('a')
        if not neededLetters[c]:
            neededLetters[c] = True
            need += 1

    missed = 0
    for i in range(len(letters)):
        if not (missed <= 6 and need > 0):
            break
        c = ord(letters[i]) - ord('a')
        if neededLetters[c]:
            neededLetters[c] = False
            need -= 1
        else:
            missed += 1

    return need == 0

