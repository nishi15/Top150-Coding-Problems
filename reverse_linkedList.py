'''
Given the head of a singly linked list, reverse the list, and return the reversed list.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]
Example 2:


Input: head = [1,2]
Output: [2,1]
Example 3:

Input: head = []
Output: []
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def __init__(self):
        self.head = None

    def inserNode(self,arr):
        node = ListNode(arr[0])
        self.head = node        

        for item in range(1,len(arr)):
            node.next = ListNode(arr[item])
            node = node.next

    def showlist(self):
        node = self.head
        while node:
            print(node.val,end=" -> ")
            node = node.next


    def reverseList(self):
        head = self.head
        current = head
        prev = None

        while current:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node

        self.head = prev
        return prev


if __name__ == "__main__":
    sol = Solution()
    sol.inserNode([1,2,3,4,5])

    sol.showlist()
    sol.reverseList()
    print("\n---------------------")
    sol.showlist()