class Solution:
    def isValid(self, s: str) -> bool:
        
        _map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        stack = []

        for value in s:
            if value in _map:
                stack.append(_map[value])
            else:
                if len(stack) <= 0:
                    return False

                candidate = stack.pop()
                if candidate != value:
                    return False
                
        return len(stack) == 0