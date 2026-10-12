class Solution:
    def isValid(self, s: str) -> bool:
        
        map_ = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []
        for n, char in enumerate(s):
            if char in map_:
                stack.append(map_[char])
                continue
            if len(stack) <= 0:
                return False
            expected = stack.pop()
            if char != expected:
                return False
        
        return len(stack) == 0

