def plusone(digit):
    op = ''.join(str(d) for d in digit)
    num = int(op)
    ic = num+1
    li = [int(c) for c in str(ic)]
    return li

print(plusone([1,2,3]))
print(plusone([4,3,2,1]))
print(plusone([9]))