class Solution:
    def countBits(self, n: int) -> List[int]:
        
        def _count(number: int) -> int:
            bit_count = 0
            i = 0
            while number > 0:
                bit_count += number % 2
                number = number // 2
            return bit_count
        
        return [_count(i) for i in range(n + 1)]
            