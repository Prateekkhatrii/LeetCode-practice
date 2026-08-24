"""
260. Single Number III
Given an integer array nums, in which exactly two elements appear only once and all the other elements appear exactly twice. Find the two elements that appear only once. You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only constant extra space.

 

Example 1:

Input: nums = [1,2,1,3,2,5]
Output: [3,5]
Explanation:  [5, 3] is also a valid answer.
Example 2:

Input: nums = [-1,0]
Output: [-1,0]
Example 3:

Input: nums = [0,1]
Output: [1,0]
 

Constraints:

2 <= nums.length <= 3 * 104
-231 <= nums[i] <= 231 - 1
Each integer in nums will appear twice, only two integers will appear once.
"""
class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        xored=0
        for num in nums:
            xored = xored ^ num
        ex=0
        while True:
            if xored & 1 == 1:
                break
            xored=xored>>1
            ex+=1
        setBucket=0
        unsetBucket=0
        for num in nums:
            if (num>>ex) & 1 ==1:
                setBucket^=num
            else:
                unsetBucket^=num
        return [setBucket,unsetBucket]

