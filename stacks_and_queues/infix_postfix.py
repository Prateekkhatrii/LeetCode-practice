class Solution:
    def infixToPostfix(self, s: str) -> str:
        # Your code goes here
        def precedence(op):
            if op=="^":
                return 3
            if op=="*" or op=="/":
                return 2
            if op=="+" or op=="-":
                return 1
            else:
                return 0
        stack = []
        ans = ""
        for ch in s:
            if ch.isalnum():
                ans += ch

            elif ch == '(':
                stack.append(ch)

            elif ch==")":
                while stack and stack[-1]!='(':
                    ans += stack.pop()

                stack.pop()
            else:
                while stack and stack[-1] != '(' and precedence(ch) <= precedence(stack[-1]):
                    ans+=stack.pop()
                stack.append(ch)
        while stack:
            ans += stack.pop()

        return ans
