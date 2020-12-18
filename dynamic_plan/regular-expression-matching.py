class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # todo s, p could be empty
        if not p:
            if not s: return True
            else: return False
        len_s = len(s)
        len_p = len(p)
        dp= [[0] * (len_p+1) for iii in range(len_s)]
        if not s:
            #todo could p be "*"?
            for test_i in range(2,len_s,2):
                if p[test_i]!='*':
                    return False
                return True
            else: return False
        i = 0
        j = 0
        while i < len_s:
            for j in range(len_p):
                if p[j]!='*':
                    if p[j]=='.': # .
                        dp[i][j] = dp[i-1][j-1]
                    elif s[i]==p[j]:  # letter match
                        dp[i][j]=1
                elif p[j]=='*':
                    if dp[i][j-2]: dp[i][j]=1  # cancel last letter, most right column is zero
                    if dp[i][j-1]: dp[i][j]=1  # as no * exist
                    if s[i]==s[i-1] and dp[i-1][j]:
                        dp[i][j]=1  # more repeats
            i+=1
        print(dp)
        if dp[i-1][j-1]: return True
        else: return False






ss = Solution()
print(ss.isMatch("aa","a*"))



"""
https://leetcode-cn.com/leetbook/read/illustration-of-algorithm/9a1ypc/

https://leetcode-cn.com/problems/regular-expression-matching/
"""