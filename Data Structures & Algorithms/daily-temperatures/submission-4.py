class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for n, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                pop_idx, pop_temp = stack.pop()
                result[pop_idx] = n - pop_idx
            stack.append([n, temp])
        return result