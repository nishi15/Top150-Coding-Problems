
# for creating tree node
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# for creating tree
class Tree:
    def __init__(self) -> None:
        self.head = None

    def insert_node(self,arr):
        self.head = TreeNode(arr[0])
        node = self.head

        for i in range(1,len(arr)):
            self.__insert_node(arr[i],self.head)

    def __insert_node(self,data,node):
        if data < node.val:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self.__insert_node(data,node.left)

        elif data > node.val:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.__insert_node(data,node.right)
        else:
            print("Node already present")


    def show_tree(self):
        self._show_tree(self.head)
        return self.head

    def _show_tree(self,root):
        if not root:
            return None
        
        print(root.val)
        print("------->",root.left.val if root.left else None)
        print("------->",root.right.val if root.right else None)
        
        if root.left:
            self._show_tree(root.left)
        if root.right:
            self._show_tree(root.right)


class BinaryTree:
    def __init__(self) -> None:
        self.head = None

    def insert_node(self,arr):
        self.head = TreeNode(arr[0])

        for i in range(1,len(arr)):
            
            self.__insert_node(i,arr[i],self.head)

    def __insert_node(self,i,data,node):
        if i%2 != 0:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self.__insert_node(i,data,node.left)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self.__insert_node(i,data,node.right)
        


    def show_tree(self):
        self._show_tree(self.head)
        return self.head

    def _show_tree(self,root):
        if not root:
            return None
        
        print(root.val)
        print("------->",root.left.val if root.left else None)
        print("------->",root.right.val if root.right else None)
        
        if root.left:
            self._show_tree(root.left)
        if root.right:
            self._show_tree(root.right)

if __name__ == "__main__":
    # tree = Tree()
    # tree.insert_node([1,2,3,4,5,6])
    # tree.show_tree()

    tree = BinaryTree()
    tree.insert_node([1,2,3,4,5,6])
    tree.show_tree()