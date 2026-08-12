class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_cache = {}
        t_cache = {}
        for i in range(len(s)):
            s_cache[s[i]] = s_cache.get(s[i], 0) + 1
            t_cache[t[i]] = t_cache.get(t[i], 0) + 1
        return s_cache == t_cache