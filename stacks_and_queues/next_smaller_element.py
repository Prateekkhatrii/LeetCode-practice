class Solution:
    def nextSmallerElements(self, arr):
        # Your code goes here
        n=len(arr)
        stack=[]
        ans=[-1]*n
        for i in range(n-1,-1,-1):
            while stack and stack[-1]>=arr[i]:
                stack.pop()
            if stack:
                ans[i]=stack[-1]
            
            stack.append(arr[i])
        return ans
