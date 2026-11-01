class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = defaultdict(list)
        for str in strs:
            sortedS = ''.join(sorted(str))
            seen[sortedS].append(str)
        
        return list(seen.values())