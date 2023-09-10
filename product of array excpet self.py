class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1]*len(nums)

        for i in range(1,len(nums)):
            res[i] = res[i-1]*nums[i-1]
        postfix = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] = res[i]*postfix
            postfix *= nums[i]
        return res 
'''
Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]
Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]
 
'''
