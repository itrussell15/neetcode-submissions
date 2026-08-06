class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if len(s) != len(t):
            return False

        s_chars = {}
        t_chars = {}

        for i in range(len(s)):
            s_val = s[i]
            t_val = t[i]

            s_chars[s_val] = s_chars.get(s_val, 0) + 1
            t_chars[t_val] = t_chars.get(t_val, 0) + 1

        return t_chars == s_chars