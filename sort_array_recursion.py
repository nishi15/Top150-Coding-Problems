'''
We are required to sort an array in increasing order.
We will use recursion for the same.
'''


def sortarray(arr):
    if not arr:
        return
    
    temp = arr.pop()
    sortarray(arr)
    insert(arr,temp)

    return arr


def insert(arr,temp):
    if not arr or arr[-1] <= temp:
        arr.append(temp)
        return

    item = arr.pop()
    insert(arr,temp)
    arr.append(item)
    return 



if __name__ == "__main__":
    arr = [6,2,0,3,1]
    print(sortarray(arr))