'''
We are given a stack, we need to delete the middle elemnt from stack and then print the new stack

Example :
s = [5,4,3,2,1]
mid = 3
o/p = [5,4,2,1]

s = [1,2,4,5,6,7]
mid = (size/2) + 1 = 4th elemnt 5
o/p = [1,2,4,6,7]
'''


def del_middle(stack,mid):
    if not mid:
        stack.pop(0)
        return 

    itemm = stack.pop(0)
    print(itemm)
    del_middle(stack,mid-1)
    stack.insert(0,itemm)
    return stack


def reverse_stack(stack):
    if not stack:
        return
    item = stack.pop(0)
    reverse_stack(stack)
    stack.append(item)
    return stack

if __name__ == "__main__":
    s = [5,4,3,2,1,8]
    if len(s)%2 == 0:
        mid = (len(s) + 1)//2
    else:
        mid = len(s)//2
    print(mid)
    # res = del_middle(s,mid)
    # print(res)

    print(reverse_stack(s))

