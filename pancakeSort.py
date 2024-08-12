class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        result = []
        n = len(arr)
        
        for size in range(n, 1, -1):
            # Find the index of the largest element in the unsorted part of the array
            max_index = arr.index(size)
            
            # If the largest element is not already in its correct position
            if max_index != size - 1:
                # If it's not at the start, flip it to the start
                if max_index != 0:
                    result.append(max_index + 1)
                    arr[:max_index + 1] = arr[:max_index + 1][::-1]
                
                # Flip it to its final position
                result.append(size)
                arr[:size] = arr[:size][::-1]
        
        return result
      
