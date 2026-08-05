class Solution:
    def isValid(self, s: str) -> bool:
        
        _map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []
        for char in s:
            if char in _map:
                stack.append(_map[char])
                continue
            
            if len(stack) <= 0:
                return False
            candidate = stack.pop()
            if char != candidate:
                return False

        return len(stack) == 0 
            
