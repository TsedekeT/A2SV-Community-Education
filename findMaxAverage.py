class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        window_sum = sum(nums[:k])
        max_average = window_sum / k
        for slide_in in range(k, len(nums)):
            window_sum = window_sum + nums[slide_in] - nums[slide_in - k]
            max_average = max(max_average, window_sum / k)
        return max_average
