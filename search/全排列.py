class Solution:
    def permute(self, nums):
        res = []
        def choose(nums,tmp):
            if not nums:  #抵达终点
                res.append(tmp)
                return
            for i in range(len(nums)):
                nums_c=nums[:] # 返回一个shadow copy
                nums_c.pop(i)
                tmp_c = tmp[:] # 返回一个shadow copy
                tmp_c.append(nums[i])
                #递归的时候传新copy的参数, 不影响原参数
                choose(nums_c,tmp_c)

        choose(nums,[])
        return res

ss = Solution()
t = [1,2,3]
print(ss.permute(t))
