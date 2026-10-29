class Solution:
    def isValid(self, s: str) -> bool:
        
        if len(s) <= 1:
            return False

        map_ = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        stack = []
        for char in s:
            if char in map_:
                stack.append(map_[char])
                continue
            else:
                if len(stack) <= 0:
                    return False
                    
                closing = stack.pop()
                if closing != char:
                    return False
            
        return len(stack) == 0

            
            
