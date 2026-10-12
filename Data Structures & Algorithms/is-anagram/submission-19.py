class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_cache = {}
        t_cache = {}
        for i in range(len(s)):
            s_cache[s[i]] = 1 + s_cache.get(s[i], 0)
            t_cache[t[i]] = 1 + t_cache.get(t[i], 0)
        
        return s_cache == t_cache