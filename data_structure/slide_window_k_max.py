class Solution:
    def maxSlidingWindow(self, nums, k: int):
        """deque solution
        执行用时： 56 ms , 在所有 Python3 提交中击败了 98.38% 的用户 内存消耗： 16.9 MB , 在所有 Python3 提交中击败了 30.60% 的用户"""
        if nums ==[]: return []
        result =[]
        que_max = []
        max_tmp = None
        if not max_tmp:  # init
            max_tmp = max(nums[0:k])
            result.append(max_tmp)
            que_max.append(max_tmp)
        for i in range(1,len(nums)-k+1):
            if nums[i-1] == que_max[0]:   # head
                que_max.pop(0)
            if que_max == []:
                que_max.append(max(nums[i:i+k]))  # re-calculate current max
            elif nums[i+k-1] >= que_max[-1]:    # tail
                que_max.append(nums[i+k-1])
            result.append(que_max[-1])
        return result

    def maxSlidingWindow2(self, nums, k: int):
        """compare the new and old
        执行用时： 56 ms , 在所有 Python3 提交中击败了 98.33% 的用户 内存消耗： 16.8 MB , 在所有 Python3 提交中击败了 49.07% 的用户
        """
        if nums ==[]: return []
        result = []
        max_val = None
        for i in range(len(nums)-k+1):
            if not max_val:
                max_val = max(nums[i:i+k])
            else:  # max exist
                if nums[i+k-1]>nums[i-1]:  # new > old, new max_val
                    max_val = max([nums[i+k-1],max_val])  # 3 val compare
                if nums[i-1]==max_val:  # old max out, re-calculate
                    max_val = max(nums[i:i+k])
            result.append(max_val)
        return result


    def maxSlidingWindow3(self, nums, k: int):
        """
        naive solution by calculating each slide window
        执行用时： 536 ms , 在所有 Python3 提交中击败了 24.73% 的用户 内存消耗： 16.9 MB , 在所有 Python3 提交中击败了 21.06% 的用户
        """
        if nums ==[]: return []
        result = []
        for i in range(len(nums)-k+1):
            max_val = max(nums[i:i+k])
            result.append(max_val)
        return result

nums = [1, 3, -1, -3, 5, 3, 6, 7]
#nums = [1,-1]
so = Solution()
#print(so.maxSlidingWindow(nums,1))
print(so.maxSlidingWindow(nums,3))


