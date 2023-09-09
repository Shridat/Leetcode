#To find pair of sum equals to target
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d ={}
        for i in range(len(nums)):
            temp = target-nums[i]
            if temp in d:
                return i,d[temp]
            d[nums[i]] = i
'''
Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
'''
