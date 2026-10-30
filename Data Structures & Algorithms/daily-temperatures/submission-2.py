class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        result = [0 for _ in range(len(temperatures))]
        stack = []

        for n, temp in enumerate(temperatures):
            # print(f"Stack: {stack}")
            # print(f"Idx: {n} - Temp: {temp}")

            while stack and temp > stack[-1][1]:
                pop_idx, pop_temp  = stack.pop()
                # print(f"Popped: {pop_idx}")
                result[pop_idx] = n - pop_idx
            stack.append([n, temp])
            # print(result)
        return result        
                
        