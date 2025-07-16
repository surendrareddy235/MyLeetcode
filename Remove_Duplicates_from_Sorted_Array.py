def removeDuplicates(nums):
    us =  sorted(set(nums))
    print(us)
    for i in range(len(us)):
        nums[i] = us[i]
    print(nums, end=' ')
    return len(nums)
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))