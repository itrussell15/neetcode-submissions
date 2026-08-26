class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        cache = {}
        for i, word in enumerate(strs):
            tmp = {}
            for char in sorted(word):
                tmp[char] = tmp.get(char, 0) + 1
            encoded = tuple(tmp.items())
            if encoded not in cache:
                cache[encoded] = []    
            cache[encoded].append(i)
        
        output = []
        for group in cache:
            output.append([strs[i] for i in cache[group]])
        return output
