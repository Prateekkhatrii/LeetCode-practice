'''
Example 1:

Input: nums = [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number. 
The second 1's next greater number needs to search circularly, which is also 2.
'''
class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n = len(nums)

        nge = [-1] * n
        stack = []

        for i in range(2 * n - 1, -1, -1):

            while stack and stack[-1] <= nums[i % n]:
                stack.pop()

            if i < n:
                if stack:
                    nge[i] = stack[-1]

            stack.append(nums[i % n])

        return nge
