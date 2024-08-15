class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        ans = 0
        n = len(skill)
        
        # If the array has only two players
        if n == 2:
            return skill[0] * skill[1]
        
        # Sort the skills
        skill.sort() # 1 2 3 3 4 5
        
        i = n // 2 - 1
        j = n // 2
        sum_val = skill[i] + skill[j]
        
        while i >= 0 and j < n:
            tmp = skill[i] + skill[j]
            
            # Ensure teams are divided equally
            if tmp == sum_val:
                # Calculate the chemistry
                ans += skill[i] * skill[j]
            else:
                # If unable to divide teams equally
                return -1
            
            i -= 1
            j += 1
        
        return ans
