class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        else:
           s_dict= Counter(s)
           t_dict = Counter(t)
           for key in s_dict.keys():
              if s_dict[key] != t_dict[key]:
                return False
        return True
