def addbinary(a,b):
    i = int(a, 2)
    j = int(b, 2)
    k = i+j
    return bin(k)[2:]
print(addbinary("11","1"))