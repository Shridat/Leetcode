class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        res = [0]*len(temperatures)
        index = 0
        for i,temp in enumerate(temperatures):
            while stack and temp>temperatures[stack[-1]]:
                index = stack.pop()
                res[index] = i-index
            stack.append(i)
        return res 
''' 
Example 1:

Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]
Example 2:

Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]
Example 3:

Input: temperatures = [30,60,90]
Output: [1,1,0]
'''
