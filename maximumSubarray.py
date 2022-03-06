'''
Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

Solution: Use Kadane's Algo
'''

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums)>0:
            mstn = ptr = start = end = 0
            maxSum = nums[0]
            
            for i in range(len(nums)):
                mstn += nums[i]
                
                if mstn  > maxSum:
                    maxSum = mstn
                    end = i
                    start = ptr # needed to get the range of array
                
                if mstn < 0:
                    mstn = 0
                    ptr = i+1
            
            return maxSum
      
