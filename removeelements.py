def removeelements(nums,val):
    i = 0
    while i < len(nums):
        if nums[i] == val:
            nums.pop(i)
        else:
            i = i+1
    return len(nums)


print(removeelements([1,2,3,4,5,6,1,2,3,4,5,],2))