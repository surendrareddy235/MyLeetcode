def lengthoflastword(s):
    words = s.split()
    i = words[-1]
    return len(i)
    
print(lengthoflastword("luffy is still joyboy"))