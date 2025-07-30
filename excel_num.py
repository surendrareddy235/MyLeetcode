def excel(alpha):
    result = 0
    for i in alpha:
        j = ord(i)-ord("A")+1
        result = result * 26 + j
    return result
print(excel("ZA"))