class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]  

        for char in s:
            if char == '(':
                stack.append(0)  
            else:
                last_score = stack.pop()  
                stack[-1] += max(2 * last_score, 1)

        return stack.pop() 
