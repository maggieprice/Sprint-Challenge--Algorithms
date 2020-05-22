'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''
def count_th(word):
    n = len(word)
    substring = "th"
    if (n == 0 ):
        return 0
    if (n > 1):
        count = word.count(substring)
        return count
    
