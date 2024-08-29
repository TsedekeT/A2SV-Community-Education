class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:        
        p_count = Counter(p)
        s_count = Counter()
        result = []
        
        for i in range(len(s)):
            # Add the current character to the sliding window
            s_count[s[i]] += 1
            if i >= len(p):
                if s_count[s[i - len(p)]] == 1:
                    del s_count[s[i - len(p)]]
                else:
                    s_count[s[i - len(p)]] -= 1
            
            # Compare frequency maps
            if s_count == p_count:
                result.append(i - len(p) + 1)
        
        return result

