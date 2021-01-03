class Solution:
    def minNumber(self, nums: List[int]) -> str:

        #if nums == []: return 0  不需要

        def quicksort(l, r):
            if l >= r: return
            i, j = l, r
            while (i < j):
                while (s[j] + s[l] >= s[l] + s[j] and i < j):
                    j -= 1
                while (s[i] + s[l] <= s[l] + s[i] and i < j):
                    i += 1
                s[i], s[j] = s[j], s[i]  # 指针交换
            s[l], s[i] = s[i], s[l]  # pivot换至目标位置
            quicksort(l, i - 1)  # 递归
            quicksort(i + 1, r)

        s = [str(n) for n in nums]
        quicksort(0, len(s) - 1)

        return "".join(s)