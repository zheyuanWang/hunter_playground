class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # todo s, p could be empty
        if not p:
            if not s: return True
            else: return False
        len_s = len(s)
        len_p = len(p)
        if not s:
            #todo could p be "*"?
            if len_p==2 & p[1]=='*': return True
            else: return False
        tmp_character = None
        i = 0
        j = 0
        while j < len_p:
            if p[j].isalpha():
                if p[j]!=s[i]:
                    if j+1 == len_p: return False  # end
                    elif p[j+1] =='*': return True
                    else: return False
                i += 1

            elif p[j] == '.':
                i += 1

            elif p[j] == '*':
                if s[i] != s[i-1]: return False

                while s[i+1]==s[i]:
                    i+=1
                i += 1
            else: return False
            j += 1



ss = Solution()
print(ss.isMatch("aa","a"))





"""
https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/9a1ypc/

https://leetcode-cn.com/problems/regular-expression-matching/
"""