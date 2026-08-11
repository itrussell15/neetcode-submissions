class Solution:
    def romanToInt(self, s: str) -> int:
        
        map_ = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        i = 0
        total = 0
        while i < len(s):
            value = map_[s[i]]
            if i <= len(s) - 2 and map_[s[i + 1]] > value:
                total -= value
            else:
                total += value
            i += 1

        return total 

