from typing import List

class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        MOD = 10**9 + 7
        n = len(arr)
        
        prev_less = [-1] * n
        next_less = [n] * n
        
        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                stack.pop()
            if stack:
                prev_less[i] = stack[-1]
            stack.append(i)
        
        stack = []
        for i in range(n-1, -1, -1):
            while stack and arr[stack[-1]] > arr[i]:
                stack.pop()
            if stack:
                next_less[i] = stack[-1]
            stack.append(i)
        
    
        result = 0
        for i in range(n):
            left_distance = i - prev_less[i]
            right_distance = next_less[i] - i
            result += arr[i] * left_distance * right_distance
            result %= MOD
        
        return result

        
