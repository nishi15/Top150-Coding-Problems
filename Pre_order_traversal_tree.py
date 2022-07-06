'''
Pre order traversal of Binary tree is one of the type of depth-first search traversal.


For traversing a (non-empty) binary tree in a preorder fashion, we must do these three things for every node n starting from the tree’s root:

(N) Process n itself.
(L) Recursively traverse its left subtree. When this step is finished, we are back at n again.
(R) Recursively traverse its right subtree. When this step is finished, we are back at n again.

(N)->(L)->(R)

Construct the following tree
               1
             /   \
            /     \
           2       3
          /      /   \
         /      /     \
        4      5       6
              / \
             /   \
            7     8

Pre-order traversal will be :-

1 -> 2 -> 4 -> 3 -> 5 -> 7 -> 8 -> 6
'''

# Data structure to store a binary tree node
class Node:
    def __init__(self, data=None, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# class used for tree traversal.
class Traversal:

    def iterative_approach(self,root):
        if not root:
            return False

        stack = []
        
        stack.append(root)

        while stack:

            curr = stack.pop()

            print(curr.data,end=" -> ") 

            if curr.right:
                stack.append(curr.right)

            if curr.left:
                stack.append(curr.left)


    def recursive_approach(self,root):
        if not root:
            return False

        print(root.data,end=" -> ")

        self.recursive_approach(root.left)
        self.recursive_approach(root.right)



if __name__ == '__main__':
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(5)
    root.right.right = Node(6)
    root.right.left.left = Node(7)
    root.right.left.right = Node(8)

    sol = Traversal()
    sol.recursive_approach(root)
    print()
    sol.iterative_approach(root)


