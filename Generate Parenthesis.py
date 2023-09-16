class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        res = []
        def backtrack(op,cl):
            if op==cl==n:
                res.append("".join(stack))
                return 
            if op<n:
                stack.append('(')
                backtrack(op+1,cl)
                stack.pop()
            if cl<op:
                stack.append(')')
                backtrack(op,cl+1)
                stack.pop()
        backtrack(0,0)
        return res
  ''' 
  Example 1:

Input: n = 3
Output: ["((()))","(()())","(())()","()(())","()()()"]
Example 2:

Input: n = 1
Output: ["()"]
  
  '''
