def isPalindrome(x):
    x = str(x)
    if x == x[::-1]:
        return True
    else:
        return False
print(isPalindrome(-121))