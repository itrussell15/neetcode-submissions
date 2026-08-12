class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid_chars = "".join([char.lower() for char in s if char.isalnum()])
        print(valid_chars)
        return valid_chars == valid_chars[::-1]