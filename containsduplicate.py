def containsduplicate(dub):
    nums = set()
    for i in dub:
        if i in nums:
            return True
        nums.add(i)
    return False
print(containsduplicate([1,2,3]))