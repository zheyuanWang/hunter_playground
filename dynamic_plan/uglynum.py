class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp = [1]
        p2,p3,p5 = 0, 0,0
        while(n>1):
            dp.append(min(dp[p2]*2, dp[p3]*3, dp[p5]*5))
            if dp[p2]*2 ==dp[-1]:
                p2+=1
            if dp[p3]*3 ==dp[-1]:
                p3+=1
            if dp[p5]*5 ==dp[-1]:
                p5+=1
            n-=1
        return dp[-1]


