class Solution:
    def maxArea(self, height: List[int]) -> int:
        res = 0
        l,r = 0,len(height)-1
        while l<r:
            res = max(res,min(height[l],height[r])*(r-l))
            if height[l]<height[r]:
                l+=1
            elif height[r]<=height[l]:
                r-=1
        return res
'''
Example 1: 

Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:

Input: height = [1,1]
Output: 1
'''
