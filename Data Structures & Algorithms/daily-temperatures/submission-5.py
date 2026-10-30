class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        stack = []
        output = [0 for _ in range(len(temperatures))]

        for n, temp in enumerate(temperatures):
            while stack and stack[-1][1] < temp:
                pop_idx, pop_temp = stack.pop()
                output[pop_idx] = n - pop_idx
            stack.append([n, temp])

        return output