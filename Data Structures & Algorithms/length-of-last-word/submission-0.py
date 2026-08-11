class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        words =[word for word in s.split(" ")]
        return len(words[-1])
            