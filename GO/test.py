string = "AbCdEfG"
upper = ""
lower = ""
for i in string:
    if i.isupper():
        upper += i
    if i.islower():
        lower += i
print(upper)
print(lower)

print(upper + lower)