/*
https://leetcode.com/problems/contains-duplicate/
Solution: Use a hashMap.
Time Complexity : O(n)
Space Complexity : O(n)
*/
func containsDuplicate(nums []int) bool {
    // create a hashMap
    hashMap := make(map[int]int)
    // loop through the nums and check if num is is in hashMap
    for _,n := range nums{
        _, ok := hashMap[n]
        if ok{
            return true
        }
        // else condition
        hashMap[n]=1
    }
    return false   
}
