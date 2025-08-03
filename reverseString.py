def revstring(rev):
    left, right=0, len(rev)-1
    while left < right:
        rev[left],rev[right] = rev[right],rev[left]
        left += 1
        right -= 1
    return rev
print(revstring(['h','e','l','l','o']))



