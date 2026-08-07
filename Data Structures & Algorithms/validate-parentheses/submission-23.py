class Solution:
    def isValid(self, s: str) -> bool:
        
        map_ = {
            "(": ")",
            "[": "]",
            "{": "}"
        }

        if len(s) % 2 == 1:
            return False

        stack = []
        for char in s:
            if char in map_:
                stack.append(map_[char])
            else:
                if len(stack) <= 0:
                    print('Not enough chars')
                    return False
                if stack.pop() != char:
                    print("Mismatch")
                    return False
                
        return len(stack) == 0