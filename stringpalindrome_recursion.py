'''
To check if a string is palindrome or not
'''


def palindrome(s,res):
    if len(s) < 2:
        return s

    if s  == s[::-1]:
        res = s
        return res

    return palindrome(s[:-1],res)


print(palindrome("aba",""))