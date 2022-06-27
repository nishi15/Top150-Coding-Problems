'''
You are given the heads of two sorted linked lists list1 and list2.

Merge the two lists in a one sorted list. The list should be made by splicing together the nodes of the first two lists.

Return the head of the merged linked list.

 

Example 1:


Input: list1 = [1,2,4], list2 = [1,3,4]
Output: [1,1,2,3,4,4]
Example 2:

Input: list1 = [], list2 = []
Output: []
Example 3:

Input: list1 = [], list2 = [0]
Output: [0]
'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self):
        self.head1 = None
        self.head2 = None
    
    def inserNode(self,arr1,arr2):
        node1 = ListNode(arr1[0])
        node2 = ListNode(arr2[0])
        self.head1 = node1 
        self.head2 = node2        

        for item in range(1,len(arr1)):
            node1.next = ListNode(arr1[item])
            node1 = node1.next

        for item in range(1,len(arr2)):
            node2.next = ListNode(arr2[item])
            node2 = node2.next

        return self.head1,self.head2

    
    def showlist(self,head):
        node = head
        while node:
            print(node.val,end=" -> ")
            node = node.next
        print()

    def mergeTwoLists(self, list1, list2):
        dummy = ListNode()
        tail = dummy

        while list1 and list2:
            if list1.val < list2.val:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next

            tail = tail.next
        
        if list1:
            tail.next = list1
        elif list2:
            tail.next = list2

        return dummy.next

        
if __name__ == "__main__":
    sol = Solution()
    list1 = [1,2,4]
    list2 = [1,3,4]
    head1,head2 = sol.inserNode(list1,list2)
    sol.showlist(head1)
    sol.showlist(head2)
    res = sol.mergeTwoLists(head1,head2)
    sol.showlist(res)
    