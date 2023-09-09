class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for num in nums:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        sorted_d = {key:val for key,val in sorted(d.items(),key=lambda x: x[1],reverse = True)}
        res = list(sorted_d.keys())
        return res[:k]
'''
Example 1:

Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]
Example 2:

Input: nums = [1], k = 1
Output: [1]
 

'''
