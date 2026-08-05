class Solution:
    def isValid(self, s: str) -> bool:
        
        _map = {
            "{": "}",
            "[": "]",
            "(": ")"
        }

        if len(s) % 2 == 1:
            return False

        stack = []
        for char in s:
            if char in _map:
                stack.append(_map[char])
                continue
            
            if len(stack) <= 0 or stack.pop() != char:
                return False             

        return len(stack) == 0