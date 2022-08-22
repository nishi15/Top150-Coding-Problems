'''
Given the head of a singly linked list, group all the nodes with odd indices together followed by the nodes with even indices, and return the reordered list.

The first node is considered odd, and the second node is even, and so on.

Note that the relative order inside both the even and odd groups should remain as it was in the input.

You must solve the problem in O(1) extra space complexity and O(n) time complexity.

 

Example 1:


Input: head = [1,2,3,4,5]
Output: [1,3,5,2,4]

Example 2:


Input: head = [2,1,3,5,6,4,7]
Output: [2,3,6,7,1,5,4]
 

Constraints:

The number of nodes in the linked list is in the range [0, 104].
-106 <= Node.val <= 106

'''

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def __init__(self) -> None:
        self.head = None

    def oddEvenList(self):
        curr_odd = ListNode(-1)
        odd = curr_odd

        curr_even = ListNode(-1)
        even = curr_even
        count = 1
        curr = self.head

        while curr:
            if count % 2 == 0:
                print("even")
                even.next = curr
                even = curr
            else:
                print("odd")
                odd.next = curr
                odd = curr
            
            curr = curr.next
            count += 1

        even.next = None
        odd.next = curr_even.next
        self.head = curr_odd.next


    def insert(self,arr):
        self.head = ListNode(arr[0])
        node = self.head

        for i in range(1,len(arr)):
            node.next = ListNode(arr[i])
            node = node.next

        # return self.head

    def show(self):
        curr = self.head

        while curr:
            print(curr.val,end="->")
            curr = curr.next



if __name__ == "__main__":
    sol = Solution()
    sol.insert(arr=[1,2,3,4,5])
    sol.show()
    sol.oddEvenList()
    sol.show()