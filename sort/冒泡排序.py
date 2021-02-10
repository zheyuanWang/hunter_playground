# -*- coding:utf8 -*-

def bubble_sort(nums):
    for i in range(len(nums)):
        for j in range(i,len(nums)):
            if nums[i]> nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums

print(bubble_sort([4,3,56,8,7,4,2,1]))