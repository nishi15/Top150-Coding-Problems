'''
print powerset of given string

Example :
ip - "ab"
op - ["","a","b","ab"]
'''

'''
We have solved this probem using the Decission tree approach of recursion, bcs we can have the choice of taking or not the i/p 
'''

def powerset(string):
    if not string:
        return ""

    powset = set()
    op = ""
    print(solve(string,powset,op))

def solve(s,powset,op):
    # base condition
    if not s:
        powset.add(op)
        return

    # not taking substr
    left = op

    # taking substr
    right = op+s[0]

    # recursive calls for each o/p
    solve(s[1:],powset,left)
    solve(s[1:],powset,right)

    return powset


powerset("aab")
