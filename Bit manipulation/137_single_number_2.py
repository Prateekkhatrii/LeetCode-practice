
"""137. Single Number II
Given an integer array nums where every element appears three times except for one, which appears exactly once. Find the single element and return it.

You must implement a solution with a linear runtime complexity and use only constant extra space."""

class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        res=0
        for i in range(32):
            temp = 1<<i
            count_ones=0
            count_zeroes=0
            for num in nums:
                if num & temp==0:
                    count_zeroes+=1
                else:
                    count_ones+=1
            if count_ones%3==1:
                res = res | temp
            
        if res >= 2**31:
            res -= 2**32

        return res

            
                 
