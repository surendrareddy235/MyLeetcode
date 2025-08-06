def reversevowels(rev):
    vowels = ["a","e","i","o","u","A","E","I","O","U"]
    rev = list(rev)
    left,right = 0,len(rev)-1
    while left < right:
        if rev[left] not in vowels:
            left = left+1
        elif rev[right] not in vowels:
            right = right -1
        else:
            rev[left],rev[right] = rev[right],rev[left]
            left = left+1
            right = right-1
    return ''.join(rev)
print(reversevowels("IceCreAm"))


