def searchinsert(nums,target):
    for i in nums:
        if i == target:
            return nums.index(target)
        else:
            nums.append(target)
            nums.sort()
            return nums.index(target)
print(searchinsert([1,3,5,6],5))
print(searchinsert([1,3,5,6],2))
print(searchinsert([1,3,5,6],7))