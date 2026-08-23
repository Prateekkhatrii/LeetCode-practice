#power set: generate all the subsets of a give array
class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        ans=[]
        n=len(nums)
        subset= 1 << n
        for i in range(subset):
            li=[]
            for j in range(n):
                if i & (1<<j):
                    li.append(nums[j])
            ans.append(li)

        return ans
                

        
