'''
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

Implement the MinStack class:

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
 

Example 1:

Input
["MinStack","push","push","push","getMin","pop","top","getMin"]
[[],[-2],[0],[-3],[],[],[],[]]

Output
[null,null,null,null,-3,null,0,-2]

Explanation
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin(); // return -3
minStack.pop();
minStack.top();    // return 0
minStack.getMin(); // return -2
 

Constraints:

-231 <= val <= 231 - 1
Methods pop, top and getMin operations will always be called on non-empty stacks.
At most 3 * 104 calls will be made to push, pop, top, and getMin.
'''

class MinStack:

    def __init__(self):
        self.min = None
        self.stack = []
        pass
        

    def push(self, val: int) -> None:
        if self.min is None: self.min = val
        self.min = min(self.min, val)
        self.stack.append((val,self.min))
                

    def pop(self) -> None:
        
        if self.stack:
            item = self.stack.pop()
            if self.stack: self.min = self.stack[-1][1]
            else: self.min = None
        else:
            print("stack is empty")        
                

    def top(self) -> int:
        item = -1
        if self.stack:
            item = self.stack[-1][0]
        return item       
        

    def getMin(self) -> int:
        return self.min
        pass
        


# Your MinStack object will be instantiated and called as such:
minStack = MinStack()
minStack.push(2)
minStack.push(0)
minStack.push(3)
minStack.push(0)
print(minStack.stack)
print(minStack.getMin()) 
minStack.pop()
print(minStack.getMin()) # return -2
minStack.pop()
print(minStack.getMin()) 
minStack.pop()
print(minStack.getMin()) 
