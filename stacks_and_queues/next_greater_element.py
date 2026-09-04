'''
Example 1:

Input: nums1 = [4,1,2], nums2 = [1,3,4,2]
Output: [-1,3,-1]
Explanation: The next greater element for each value of nums1 is as follows:
- 4 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
- 1 is underlined in nums2 = [1,3,4,2]. The next greater element is 3.
- 2 is underlined in nums2 = [1,3,4,2]. There is no next greater element, so the answer is -1.
'''
class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        st=[]
        nge={}
        n=len(nums2)
        for i in range(n-1,-1,-1):
            while st and st[-1]<=nums2[i]:
                st.pop()
            if st:
                nge[nums2[i]]=st[-1]
            else:
                nge[nums2[i]]=-1
            st.append(nums2[i])
        ans=[]
        for num in nums1:
            ans.append(nge[num])
        
        return ans
