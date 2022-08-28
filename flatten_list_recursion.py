'''
Flat the n-dimensional list to 1-D using recursion
'''

def flatten(test_list):
    if isinstance(test_list, list):
        if len(test_list) == 0:
            return []
        first, rest = test_list[0], test_list[1:]
        return flatten(first) + flatten(rest)
    else:
        return [test_list]

if __name__ == "__main__":
    res = flatten([1,[2,3],[4,5,[6,7]]])
    print(res)