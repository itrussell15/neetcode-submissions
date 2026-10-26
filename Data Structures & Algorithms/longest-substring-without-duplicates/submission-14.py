class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        left = 0 
        best = 1
        current = set()

        for right in range(len(s)):
            while s[right] in current:
                current.remove(s[left])
                left += 1
            window_size = right - left + 1
            
            current.add(s[right])
            best = max(best, window_size)
        
        return best
