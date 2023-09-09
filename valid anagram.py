#Program to find valid Anagram
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        if len(s)!=len(t):
            return False
        for ch in s:
            if ch in d1:
                d1[ch]+=1
            else:
                d1[ch]=1
        for ch in t:
            if ch in d2:
                d2[ch]+=1
            else:
                d2[ch]=1
        return d1==d2
'''
Example 1:

Input: s = "anagram", t = "nagaram"
Output: true
Example 2:

Input: s = "rat", t = "car"
Output: false
'''
