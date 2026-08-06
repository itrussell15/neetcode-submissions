class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        left = 0
        result = 0
        counts = {}
        
        for right in range(len(s)):
            counts[s[right]] = 1 + counts.get(s[right], 0)
            # While the number of replacements is too high - shrink window
            while (right - left + 1) - max(counts.values()) > k:
                counts[s[left]] -= 1
                left += 1
                
            # Number of replacements is viable, calculate length
            result = max(result, right - left + 1)
        return result

