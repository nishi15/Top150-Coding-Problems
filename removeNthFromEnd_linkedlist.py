'''
Given the head of a linked list, remove the nth node from the end of the list and return its head.

 

Example 1:


Input: head = [1,2,3,4,5], n = 2
Output: [1,2,3,5]
Example 2:

Input: head = [1], n = 1
Output: []
Example 3:

Input: head = [1,2], n = 1
Output: [1]
 

Constraints:

The number of nodes in the list is sz.
1 <= sz <= 30
0 <= Node.val <= 100
1 <= n <= sz

Follow up: Could you do this in one pass?


'''


# Definition for singly-linked list.

from list_helper import LinkedListHelper

class Solution:
    def removeNthFromEnd(self, head, n: int):
        
        if head.next == None:
            return None

        temp =  head
        temp2 =  head
        len_count = 0 

        while temp:
            len_count+=1
            temp = temp.next
            
        last_node = len_count - n -1

        while last_node:
            temp2 = temp2.next
            last_node -=1
        
        t = temp2.next
        temp2.next = t.next

        head = temp2

        return head

if __name__ == "__main__":
    sol = Solution()
    list1 = [1]
    root = LinkedListHelper()
    head  = root.inserNode(list1)
    sol.removeNthFromEnd(head,1)
    root.showlist()

    
    
