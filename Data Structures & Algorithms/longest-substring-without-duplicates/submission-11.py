class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        left = 0 
        best = 0
        locations = {}

        for right in range(len(s)):
            if s[right] in locations:
                left = max(left, locations[s[right]] + 1)
            locations[s[right]] = right
            best = max(best, right - left + 1)
        return best

        