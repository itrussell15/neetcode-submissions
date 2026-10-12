class Solution:
    def isPalindrome(self, s: str) -> bool:
        values = [i.lower() for i in s if i.isalnum()]
        return values == values[::-1]

            