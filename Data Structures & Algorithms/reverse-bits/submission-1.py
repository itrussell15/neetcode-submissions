class Solution:
    def reverseBits(self, n: int) -> int:
        
        output = 0
        position = 31
        while n > 0:
            output += n % 2 * (2 ** position)
            n = n // 2
            position -= 1
        return output
        
        # total = 0
        # for i in range(len(output)):
        #     position = 31 - i
        #     total += int(output[i]) * (2 ** position)
        # return total