class Solution:
    def isValid(self, s: str) -> bool:
        

        char_map = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        # Non even numbered strings will be false
        if len(s) % 2 == 1:
            return False

        stack = []
        for char in s:
            if char in char_map:
                stack.append(char_map[char])
            else:
                if len(stack) <= 0:
                    return False
                candidate = stack.pop()
                if char != candidate:
                    return False
                    
        return len(stack) == 0
