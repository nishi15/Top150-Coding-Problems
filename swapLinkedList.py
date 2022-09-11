''''
24. Swap Nodes in Pairs
Medium

7968

329

Add to List

Share
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

 

Example 1:


Input: head = [1,2,3,4]
Output: [2,1,4,3]
Example 2:

Input: head = []
Output: []
Example 3:

Input: head = [1]
Output: [1]
 

Constraints:

The number of nodes in the list is in the range [0, 100].
0 <= Node.val <= 100

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:

    def insert(self,arr):
        head = ListNode(arr[0])
        node = head

        for i in range(1,len(arr)):
            node.next = ListNode(arr[i])
            node = node.next

        return head

    def swapPairs(self, head):
        if not head:
            return None
        
        dummy = ListNode(next=head)
        curr = head
        prev = dummy
        # print("---------------------->",n)
        
        while curr and curr.next:
            nextpair = curr.next.next
            second = curr.next

            second.next = curr
            curr.next = nextpair
            prev.next = second

            prev = curr
            curr = nextpair
        
        return dummy.next

    def show(self,head):
        while head:
            print(head.val,end="->")
            head = head.next
        print("\n")


sol = Solution()
head = sol.insert([1,2,3,4])
ans = sol.swapPairs(head)
print("ANS")
sol.show(ans)