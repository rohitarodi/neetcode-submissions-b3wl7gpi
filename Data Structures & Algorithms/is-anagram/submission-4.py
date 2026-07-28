class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s = "".join(sorted(s))
        t = "".join(sorted(t))
        print(s)
        print(t)
        if s == t :
            return True
        else :
            return False