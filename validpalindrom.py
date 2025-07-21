import re
s = " "
clean = re.sub(r'[^a-zA-Z0-9]'," ",s).lower()
if clean == clean[::-1]:
    print('True')
else:
    print(False)
print(clean[::-1].lower())

