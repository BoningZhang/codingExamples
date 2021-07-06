# !!! Number here is number of leetcode problem

# 33, 34, 35
# binary search template
nums = [1, 3, 4, 5, 9, 10]

n = len(nums)
left, right = 0, n-1
while left<=right:
    mid = left + (right - left) // 2
    if nums[mid]==target:
        return mid
    if nums[mid]>target:
        right = mid - 1
    else:
        left = mid + 1

return -1

# for other special needs, need to think when to return and when move to left or right
# or return left/right
