class Solution:
    def isValid(self, s: str) -> bool:
        op = ['(','{','[']
        cl = [')','}',']']
        stack = []
        for ch in s:
            if ch in op:
                stack.append(ch)
            elif ch in cl:
                pos = cl.index(ch)
                if (len(stack)>0 and op[pos]==stack[len(stack)-1]):
                    stack.pop()
                else:
                    return False
        if len(stack)==0:
            return True
        else:
            return False
        
'''
Example 1:

Input: s = "()"
Output: true
Example 2:

Input: s = "()[]{}"
Output: true
Example 3:

Input: s = "(]"
Output: false
'''        
