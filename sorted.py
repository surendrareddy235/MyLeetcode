def sorted(num1,m,num2,n):
    num1[m:] = num2
    num1.sort()
    return num1

print(sorted([1,2,3,0,0,0],3,[2,4,5],3))


