'''
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, and /. Each operand may be an integer or another expression.

Note that division between two integers should truncate toward zero.

It is guaranteed that the given RPN expression is always valid. That means the expression would always evaluate to a result, and there will not be any division by zero operation.

 

Example 1:

Input: tokens = ["2","1","+","3","*"]
Output: 9
Explanation: ((2 + 1) * 3) = 9
Example 2:

Input: tokens = ["4","13","5","/","+"]
Output: 6
Explanation: (4 + (13 / 5)) = 6
Example 3:

Input: tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"]
Output: 22
Explanation: ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
= ((10 * (6 / (12 * -11))) + 17) + 5
= ((10 * (6 / -132)) + 17) + 5
= ((10 * 0) + 17) + 5
= (0 + 17) + 5
= 17 + 5
= 22
 

Constraints:

1 <= tokens.length <= 104
tokens[i] is either an operator: "+", "-", "*", or "/", or an integer in the range [-200, 200].
'''

class Solution:
    def evalRPN(self, tokens) -> int: #140s time
        stack = []
        result = 0
        operator_list = ["+","*","-","/"]

        for tok in tokens:
            if tok in operator_list:
                if len(stack) > 1:
                    op1,op2 = stack.pop(-1),stack.pop(-1)
                    res = int(eval(op2+tok+op1))
                stack.append(str(res))
            else:
                stack.append(tok)

        
        result = stack.pop()
        print(int(result))


    def evalRPN_2(self, tokens) -> int: #82s time
        stack = []

        for ele in tokens:
            if ele == "+":
                stack.append(stack.pop()+stack.pop())
            elif ele == "-":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(op2-op1)
            elif ele == "*":
                stack.append(stack.pop()*stack.pop())
            elif ele == "/":
                op1 = stack.pop()
                op2 = stack.pop()
                stack.append(int(op2/op1))
            else:
                stack.append(int(ele))

        return stack.pop()


if __name__ == "__main__":
    sol = Solution()
    print(sol.evalRPN_2(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]))
    # sol.evalRPN_2(["2","1","+","3","*"])