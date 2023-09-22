class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums)-1

        while l<=r:
            mid = (l+r)//2
            if target<nums[mid]:
                r = mid-1
            elif target>nums[mid]:
                l = mid+1
            else:
                return mid
        return -1
  ''' 
  Example 1:

Input: nums = [-1,0,3,5,9,12], target = 9
Output: 4
Explanation: 9 exists in nums and its index is 4
Example 2:

Input: nums = [-1,0,3,5,9,12], target = 2
Output: -1
Explanation: 2 does not exist in nums so return -1
  '''
