class Solution:
    def isHappy(self, n: int) -> bool:
        
        seen = set()

        total = n
        while total != 1:
            total = sum([int(i)**2 for i in str(total)])
            print(f"Seen: {seen} - Total: {total}")
            if total in seen:
                return False
            seen.add(total)
        return True
        
