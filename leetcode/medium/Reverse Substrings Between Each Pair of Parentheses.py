class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        
        for char in s:
            if char == ')':
                # Collect characters until opening parenthesis
                portion = []
                while stack and stack[-1] != '(':
                    portion.append(stack.pop())
                
                # Pop the '('
                stack.pop()
                
                # Push back in reversed order
                stack.extend(portion)
            else:
                stack.append(char)
                
        return "".join(stack)
s=Solution()
i=input("enter a text you want to reverse (can include parantheses! : )")
print(s.reverseParentheses(i))