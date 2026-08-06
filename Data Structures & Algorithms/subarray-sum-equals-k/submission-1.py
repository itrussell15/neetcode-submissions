class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        result = 0
        current_sum = 0
        map_ = {0: 1}

        for num in nums:
            current_sum += num
            distance_from_k = current_sum - k
            result += map_.get(distance_from_k, 0)
            map_[current_sum] = map_.get(current_sum, 0) + 1
        return result
