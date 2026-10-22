class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        S_dict, T_dict = {}, {}
        for i in range(len(s)):
            S_dict[s[i]] = S_dict.get(s[i],0) + 1
            T_dict[t[i]] = T_dict.get(t[i],0) + 1

        return S_dict == T_dict