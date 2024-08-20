class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        ans = []
        i, j = 0, 0
        n, m = len(s), len(spaces)
        
        while j < m:
            if i == spaces[j]:
                ans.append(' ')
                j += 1
            ans.append(s[i])
            i += 1
        
        while i < n:
            ans.append(s[i])
            i += 1
        
        return ''.join(ans)
