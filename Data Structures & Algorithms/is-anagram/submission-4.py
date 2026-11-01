class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        seens = {}
        seent = {}
        for i in range(len(s)):
            seens[s[i]]= seens.get(s[i],0)+1
            seent[t[i]]= seent.get(t[i],0)+1
        
        if seent == seens:
            return True
        else:
            return False
