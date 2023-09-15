class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for ch in tokens:
            if ch=='+':
                stack.append(stack.pop()+stack.pop())
            elif ch=='-':
                a,b = stack.pop(),stack.pop()
                stack.append(b-a)
            elif ch=='*':
                stack.append(stack.pop()*stack.pop())
            elif ch=='/':
                a,b = stack.pop(),stack.pop()
                stack.append(int(float(b)/a))
            else:
                stack.append(int(ch))
        return stack[0]
''' 
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
'''
