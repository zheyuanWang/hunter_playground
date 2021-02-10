# -*- coding:utf8 -*-

class Solution:
    def sortArray(self, nums) :
        def quick(l, r, arr):
            if l >= r: # 递归,起手先设定终止条件
                return arr
             # 起始量要记住, 后面分段递归要分领地用
            pivot, init_right = l, r
            while l < r:
                 # "="很关键,没有等号会有死循环
                while arr[r] >= arr[pivot] and l < r:
                    r -= 1
                while arr[l] <= arr[pivot] and l < r:
                    l += 1

                arr[r], arr[l] = arr[l], arr[r]
            # print(pivot, r,init_right)
            arr[r], arr[pivot] = arr[pivot], arr[r]
            # pivot就位了, 分成左右两小段分治&递归
            quick(pivot, r - 1, arr)
            quick(r + 1, init_right, arr)
            return arr

        return quick(0, len(nums) - 1, nums)

ss = Solution()
t = [1,1,1,1,3,4,6,-5]
print(ss.sortArray(t))
