class Solution:
    def countBits(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            value = i    
            output.append(0)
            while value > 0:
                output[-1] += value % 2
                value = value // 2
        return output
