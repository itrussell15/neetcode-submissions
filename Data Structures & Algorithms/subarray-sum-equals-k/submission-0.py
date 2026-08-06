class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        _map = {0: 1}
        total = 0
        count = 0

        for num in nums:
            total += num
            diff = total - k
            count += _map.get(diff, 0)
            _map[total] = 1 + _map.get(total, 0)
        return count
        
