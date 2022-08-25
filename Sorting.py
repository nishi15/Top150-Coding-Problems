'''
We will try to implement sorting techniques 
'''

# 1. Insertion sort -- Time = O(n2)
# 2. Selection sort -- Time = O(n2)
# 3. Bubble sort -- Time = O(n2)
# 4. Merge sort -- Time = O(n2)

def insertion_sort(arr):
    for i in range(1, len(arr)):
        for j in range(i-1,-1,-1):
            if arr[j] > arr[j+1]:
                print(f"Swapping array for posittion = {i} , val = {arr[i]} with position j = {j}, val = {arr[j]}")
                arr[j],arr[j+1] = arr[j+1],arr[j]
                
            else:
                break
            
            print("-"*20,"swapped array","-"*20)
            print(arr)

def insertion_sort_optimised(arr):
    # instead of swapping each element we will store the element in temp varibale 
    # and try to find out the correct position of the element
    for i in range(1,len(arr)):
        curr = arr[i]
        for j in range(i-1,-1,-1):
            if arr[j] > curr:
                arr[j+1] = arr[j]
                hole = j
        arr[hole] = curr
        print("-"*20,"swapped array","-"*20)
        print(f'pass {i} {arr}')
    
    print(arr)


def selection_sort(arr):

    for i in range(len(arr)):
        c_min = i
        for j in range(i+1,len(arr)):
            if arr[j] < arr[c_min]:
                c_min = j

        arr[i],arr[c_min] = arr[c_min],arr[i]
        print("-"*20,"swapped array","-"*20)
        print(f'pass {i} {arr}')
    
    return arr


def bubble_sort(arr):
    # in this algorithm we will try to compare two adjacent values 
    # need to repeat this step for n times

    for i in range(len(arr)):
        # setting the flag to check if array is already sorted or not
        flag = False

        for j in range(len(arr)-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                flag = True
        
        print("-"*20,"swapped array","-"*20)
        print(f'pass {i} {arr}')

        if not flag:
            break
    
    print(arr)


def merge(left,right,arr):
    i=j=k=0

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            arr[k] = left[i]
            i =i+1
        else:
            arr[k] = right[j]
            j +=1
        
        k +=1
    
    while i < len(left):
        arr[k] = left[i]
        i +=1

    while j < len(right):
        arr[k] = right[j]
        j +=1
    
    return arr
            


def mergesort(arr):
    if len(arr) < 2:
        return

    mid = len(arr)//2
    left = arr[0:mid]
    right = arr[mid:]

    mergesort(left)
    mergesort(right)
    merge(left,right,arr)

    print(arr)

if __name__ == "__main__":
    arr = [7,2,4,1,5,3,0]
    # insertion_sort(arr)
    # insertion_sort_optimised(arr)
    # print(selection_sort(arr))
    # bubble_sort(arr)
    mergesort(arr)