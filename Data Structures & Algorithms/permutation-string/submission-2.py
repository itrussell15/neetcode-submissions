class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}
        for char in s1:
            target[char] = target.get(char, 0) + 1
        print(f"Target: {target}")

        left = 0
        for right in range(len(s1), len(s2) + 1):
            window = s2[right - len(s1): right]
            check = {}
            for char in window:
                check[char] = check.get(char, 0) + 1
            

            if check == target:
                return True
        return False
            