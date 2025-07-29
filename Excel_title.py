def execl(num):
    result = ""
    while num>0:
        num -= 1
        result = chr((num % 26)+65) +result
        num //=26
    return result
print(execl(1234))



        


