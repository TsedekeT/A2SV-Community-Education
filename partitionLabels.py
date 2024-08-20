class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIdx = {}
        for i in range(len(s)):
            lastIdx[s[i]] = i
        
        curLast = 0
        accu = 0
        res = []
        for i in range(len(s)):
            curLast = max(curLast, lastIdx[s[i]])
            if i == curLast:
                res.append(i + 1 - accu)
                accu = i + 1
        
        return res
