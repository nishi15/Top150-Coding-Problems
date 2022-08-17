'''
We will be using recursion to solve sort array problem
'''

import inspect, sys

max_recursion_depth = 10

def rec_func(recursion_index):
    if recursion_index == 0:
        return

    rec_func(recursion_index-1)

    current_frame = inspect.currentframe()
    calframe = inspect.getouterframes(current_frame, 2)

    frame_object = calframe[0][0]

    print("Recursion-%d: %s" % (max_recursion_depth - recursion_index, frame_object.f_locals))
    print("Passed parameters: %s" % (sys._getframe(1).f_locals.values()) )






def insert(arr,ele):
    if len(arr) == 0 or arr[-1] <= ele:
        arr.append(ele)
        return

    temp = arr[-1]
    arr.pop()
    insert(arr,ele)
    arr.append(temp)

def recursive_sort(arr):
    # rec_func(max_recursion_depth)
    if len(arr) == 1:
        return 
    ele = arr[-1]
    arr.pop()
    recursive_sort(arr)
    insert(arr,ele)

    return arr



print(recursive_sort([2,41,24,9,0]))