'''
Given the heads of two singly linked-lists headA and headB, return the node at which the two lists intersect. If the two linked lists have no intersection at all, return null.

For example, the following two linked lists begin to intersect at node c1:


The test cases are generated such that there are no cycles anywhere in the entire linked structure.

Note that the linked lists must retain their original structure after the function returns.

Custom Judge:

The inputs to the judge are given as follows (your program is not given these inputs):

intersectVal - The value of the node where the intersection occurs. This is 0 if there is no intersected node.
listA - The first linked list.
listB - The second linked list.
skipA - The number of nodes to skip ahead in listA (starting from the head) to get to the intersected node.
skipB - The number of nodes to skip ahead in listB (starting from the head) to get to the intersected node.
The judge will then create the linked structure based on these inputs and pass the two heads, headA and headB to your program. If you correctly return the intersected node, then your solution will be accepted.

 

Example 1:


Input: intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3
Output: Intersected at '8'
Explanation: The intersected node's value is 8 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [4,1,8,4,5]. From the head of B, it reads as [5,6,1,8,4,5]. There are 2 nodes before the intersected node in A; There are 3 nodes before the intersected node in B.
Example 2:


Input: intersectVal = 2, listA = [1,9,1,2,4], listB = [3,2,4], skipA = 3, skipB = 1
Output: Intersected at '2'
Explanation: The intersected node's value is 2 (note that this must not be 0 if the two lists intersect).
From the head of A, it reads as [1,9,1,2,4]. From the head of B, it reads as [3,2,4]. There are 3 nodes before the intersected node in A; There are 1 node before the intersected node in B.
Example 3:


Input: intersectVal = 0, listA = [2,6,4], listB = [1,5], skipA = 3, skipB = 2
Output: No intersection
Explanation: From the head of A, it reads as [2,6,4]. From the head of B, it reads as [1,5]. Since the two lists do not intersect, intersectVal must be 0, while skipA and skipB can be arbitrary values.
Explanation: The two lists do not intersect, so return null.
 

Constraints:

The number of nodes of listA is in the m.
The number of nodes of listB is in the n.
1 <= m, n <= 3 * 104
1 <= Node.val <= 105
0 <= skipA < m
0 <= skipB < n
intersectVal is 0 if listA and listB do not intersect.
intersectVal == listA[skipA] == listB[skipB] if listA and listB intersect.
 

Follow up: Could you write a solution that runs in O(m + n) time and use only O(1) memory?

'''


class Solution:
    def getIntersectionNode(self, headA, headB):
        
        '''
        Time complexity :- O(M+N)
        Space complexity :- O(1) 
        '''
        l1,l2 = headA,headB
        
        while l1 != l2:
            l2 = l2.next if l2 else headA
            l1 = l1.next if l1 else headB
        
        return l1

    def getIntersectionNode_hashmap(self, headA, headB): 

        '''
        Time complexity :- O(M+N)
        Space complexity :- O(M) 
        '''
        
        # hashmap for storing occurence of each node in list1
        hash_a = {}       
        
        while headA:
            if headA not in hash_a:
                hash_a[headA] = 1
            headA = headA.next        

        
        while headB:
            # check if given node already present in hashmap
            # if yes :- return node
            # else :- return None
            if headB in hash_a:
                return headB
            headB = headB.next
        
        return None

    def getIntersectionNode_diffinlen(self, headA, headB):
        len_a = len_b = 0
        pointer1 = headA
        pointer2 = headB

        while headA:
            len_a += 1
            headA = headA.next

        while headB:
            len_b += 1
            headB = headB.next

        diff = abs(len_a - len_b)

        # moving the pointers of linked list till the diff b/w length of lists
        if len_a > len_b:
            # list 1 needs to be skipped
            for i in diff:
                pointer1 = pointer1.next
        else:
            for i in diff:
                pointer2 = pointer2.next

        while pointer1 and pointer2:
            if pointer1 == pointer2:
                return pointer1

        return pointer1



