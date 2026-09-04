class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        digits = digits[::-1]

        carry = 1
        for i, value in enumerate(digits):
            tmp = value + carry
            if tmp >= 10:
                tmp = tmp % 10
                carry = 1
            else:
                carry = 0
            digits[i] = tmp
        
        if carry > 0:
            digits.append(carry)
        return digits[::-1]
            