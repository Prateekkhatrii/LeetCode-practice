# XOR of numbers in a given range:
# Given two integers L and R. Find the XOR of the elements in the range [L , R].
# Example 1
# Input : L = 3 , R = 5
# Output : 2
# Explanation : answer = (3 ^ 4 ^ 5) = 2.
# Example 2
# Input : L = 1, R = 3
# Output : 0
# Explanation : answer = (1 ^ 2 ^ 3) = 0.

#note: by manually doing some xor we found out a pattern which the func function uses and we use that to find the xor of the given range

class Solution:      
    def findRangeXOR(self, l, r):
        def func(n):
            if n%4==1:
                return 1
            elif n%4==2:
                return n+1
            elif n%4==3:
                return 0
            else:
                return n
        return func(l-1) ^ func(r)
