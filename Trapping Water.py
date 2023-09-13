class Solution:
    def trap(self, height: List[int]) -> int:
        c = height.index(max(height))
        vol = 0
        for arr in [height[:c],height[:c:-1]]:
            first = 0
            for h in arr:
                if h<first:
                    vol+=first-h
                else:
                    first = h
        return vol
'''
Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.
Example 2:

Input: height = [4,2,0,3,2,5]
Output: 9
'''
