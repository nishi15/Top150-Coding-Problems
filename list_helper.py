# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class LinkedListHelper:

    def __init__(self) -> None:
        self.head = None

    def inserNode(self,arr):
        node1 = ListNode(arr[0])
        self.head = node1

        for item in range(1,len(arr)):
            node1.next = ListNode(arr[item])
            node1 = node1.next
        return self.head

    def showlist(self):
        node = self.head
        while node:
            print(node.val,end=" -> ")
            node = node.next
        print()