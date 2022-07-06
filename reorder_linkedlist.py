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
    
    def inserNode(self,arr1):
        node1 = ListNode(arr1[0])
        self.head1 = node1 

        for item in range(1,len(arr1)):
            node1.next = ListNode(arr1[item])
            node1 = node1.next

        return self.head1

    
    def showlist(self,head):
        node = head
        while node:
            print(node.val,end=" -> ")
            node = node.next
        print()

    
    def reverse_list(self,node):
        current = node
        prev = None

        while current:
            nextt = current.next
            current.next = prev
            prev = current
            current = nextt

        return prev


    def reorderList(self, head) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        slow = head
        fast = head

        # finding the middle element of list
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        print(slow.val)

        # reversing the second half
        revversed_list = self.reverse_list(slow.next)
        slow.next = None
        self.showlist(revversed_list)

        # merege list
        first,second = head,revversed_list

        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2

        return head

if __name__ == "__main__":
    sol = Solution()
    list1 = [1,2,3,4,5]
    head1 = sol.inserNode(list1)
    sol.showlist(head1)    
    res = sol.reorderList(head1)
    sol.showlist(res)
    