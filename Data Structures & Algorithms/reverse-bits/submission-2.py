class Solution:
    def reverseBits(self, n: int) -> int:
        
        output = 0
        position = 31
        while n > 0:
            output += n % 2 * (2 ** position)
            n = n // 2
            position -= 1
        return output