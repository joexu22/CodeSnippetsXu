string = "admeDCAB"

strMap = {}
maxString = "-1"
for i in string:
    if i.isupper():
        if i not in strMap:
            strMap[i] = True
        if i.lower() in strMap:
            if i.upper() > maxString:
                maxString = i.upper()
    elif i.islower():
        if i not in strMap:
            strMap[i] = True
        if i.upper() in strMap:
            if i.upper() > maxString:
                maxString = i.upper()

print(maxString)