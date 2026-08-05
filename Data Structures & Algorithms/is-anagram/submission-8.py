class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # s = "".join(sorted(s))
        # t = "".join(sorted(t))
        # print(s)
        # print(t)
        # if s == t :
        #     return True
        # else :
        #     return False

        # hashmap_s = {}
        # hashmap_t = {}
        # for i in range(len(s)):
        #     if s[i] not in hashmap_s:
        #         hashmap_s[s[i]] = 1
        #     else : 
        #         hashmap_s[s[i]] += 1
        # for j in range(len(t)):
        #     if t[j] not in hashmap_t:
        #         hashmap_t[t[j]] = 1
        #     else : 
        #         hashmap_t[t[j]] += 1
        # print(hashmap_s)
        # print(hashmap_t)
        # if hashmap_s == hashmap_t :
        #     return True
        # else :
        #     return False



        # s = sorted(s)
        # t = sorted(t)
        # if s==t:
        #     return True
        # else:
        #     return False

        s_hashmap = {}
        t_hashmap = {}

        for i in range(len(s)):
            if s[i] not in s_hashmap:
                s_hashmap[s[i]] = 1
            else:
                s_hashmap[s[i]]+= 1

        for j in range(len(t)):
            if t[j] not in t_hashmap:
                t_hashmap[t[j]] = 1
            else:
                t_hashmap[t[j]]+= 1

        if s_hashmap == t_hashmap:
            return True
        else:
            return False
        # print(s_hashmap) 