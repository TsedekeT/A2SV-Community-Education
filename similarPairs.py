class Solution:
    def similarPairs(self, words: List[str]) -> int:
        count = 0
        n = len(words)
        
        # Convert each word to a set of characters
        word_sets = [set(word) for word in words]
        
        # Compare each pair of sets
        for i in range(n):
            for j in range(i + 1, n):
                if word_sets[i] == word_sets[j]:
                    count += 1
        
        return count
