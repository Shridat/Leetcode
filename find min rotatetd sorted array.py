class Solution:
    def findMin(self, nums: List[int]) -> int:
        l = 0
        r = len(nums)-1
        res = nums[0]

        while l<=r:
            if nums[l]<=nums[r]:
                res = min(res,nums[l])
                break
            m = (l+r)//2
            res = min(res,nums[m])
            if nums[m]>=nums[l]:
                l=m+1
            else:
                r = m-1
        return res

'''
Example 1:

Input: nums = [3,4,5,1,2]
Output: 1
Explanation: The original array was [1,2,3,4,5] rotated 3 times.
Example 2:

Input: nums = [4,5,6,7,0,1,2]
Output: 0
Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
Example 3:

Input: nums = [11,13,15,17]
Output: 11
Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
'''
