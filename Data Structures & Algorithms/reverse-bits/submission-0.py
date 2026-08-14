class Solution:
    def reverseBits(self, n: int) -> int:
        
        output = ""
        while n > 0:
            output += str(n % 2)
            n = n // 2
        
        total = 0
        for i in range(len(output)):
            position = 31 - i
            total += int(output[i]) * (2 ** position)
        return total