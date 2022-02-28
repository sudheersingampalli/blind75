'''
https://leetcode.com/problems/two-sum/

Solution:
1. Use two for loops : when sum of values of the indices = target return the answer.
  Complexity : O(n2)
2. Use Hashmap :  While traversing the input array, see if the compliment exists in the hashMap.
  If exists, then return the indeces, else insert the elements compliment into the Hash.
'''
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap = {}
        for i in range(len(nums)):
            compliment = target - nums[i]
            if compliment in hashMap.keys():
                return [i, hashMap[compliment]]
            hashMap[nums[i]] = i
    
