class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        carry = 1
        i = 0
        digits = digits[::-1]
        while i <= len(digits) - 1:
            digits[i] += carry
            if digits[i] < 10:
                carry = 0
            else:
                carry = 1
                digits[i] = 0
            i += 1

        if carry > 0:
            digits.append(carry)
        return digits[::-1]
            