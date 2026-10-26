class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        if not s:
            return 0

        left = 0
        best = 0 
        current = set()

        for right in range(len(s)):
            while s[right] in current:
                current.remove(s[left])
                left +=1
                
            current.add(s[right])
            best = max(best, right - left + 1)
        return best

