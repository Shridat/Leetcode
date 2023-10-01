class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        d = {}
        for ele in nums:
            if ele in d:
                d[ele]+=1
            else:
                d[ele]=1
        for key in d:
            if d[key]>1:
                return key
''' 
Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3
'''
