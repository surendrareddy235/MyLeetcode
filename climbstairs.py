def climbstairs(n):
    if n == 1: return n
    if n == 2: return n
    result = [0]* (n+1)
    result[1] = 1
    result[2] = 2

    for i in range(3,n+1):
        result[i] = result[i-1]+ result[i-2]
    return result[n]
    
print(climbstairs(5))