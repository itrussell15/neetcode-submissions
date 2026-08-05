class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False
        
        s_count = {}
        t_count = {}

        for i in range(len(s)):
            s_val = s[i]
            t_val = t[i]

            s_count[s_val] = s_count.get(s_val, 0) + 1
            t_count[t_val] = t_count.get(t_val, 0) + 1

        return s_count == t_count
