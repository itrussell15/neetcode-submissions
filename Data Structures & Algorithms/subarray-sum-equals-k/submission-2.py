class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        
        total = 0
        output = 0
        # This maps any distance of 0 to be a solution. ie k = 2 and nums[0] = 2
        locations = {0: 1}

        for n, num in enumerate(nums):
            # Add value to total
            total += num
            # Calculate the distance to the target
            distance = total - k
            # If we previously cached locations that needed this distance value, add to total
            
            output += locations.get(distance, 0)
            # Store the total sum at this location
            locations[total] = locations.get(total, 0) + 1
            # print(f"Distance: {distance}")
            # print(f"total: {total}")
            # print(f"Locations: {locations}")
        return output