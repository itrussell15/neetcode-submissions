class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        def _get_counts(word: str) -> Dict[str, int]:
            counts = {}
            for char in word:
                counts[char] = counts.get(char, 0) + 1
            return counts
        
        counts = []
        groups = []
        for word in strs:
            count = _get_counts(word)
            match = False

            if count not in counts:
                counts.append(count)
                groups.append([word])
                continue
            
            for n, item in enumerate(counts):
                if item == count:
                    groups[n].append(word)
                
        return groups
            
            

            

            