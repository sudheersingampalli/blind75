'''Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

 

Example 1:

Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:

Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]


Hint: maintain prefix-products and postfix-products arrays. Later arrive at a solution to do both in one array

'''
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = []
        pre = 1
        post = 1
        for i in range(len(nums)):
            res.append(pre)
            pre = pre * nums[i]
        
        
        for j in range(len(nums)-1,-1,-1):
            res[j] = res[j]*post
            post = post * nums[j]
        
        return res


'''
Solution in Golang
===================
func productExceptSelf(nums []int) []int {
    //declare
    pre, post := 1, 1
    l := len(nums)
    res := make([]int,l)
    
    //initialise res with 1s
    for i,_ := range(res){
        res[i]=1
    }
    
    for id, ele := range(nums){
        res[id] = pre
        pre = pre*ele
    }
    
    for j:= l-1; j >-1; j--{
        res[j] = res[j]*post
        post = post * nums[j]
    }
    
    return res
}
'''
