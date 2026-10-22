class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
   
        SortedS = ''.join(sorted(s))
        SortedT = ''.join(sorted(t))
        return SortedS == SortedT
        