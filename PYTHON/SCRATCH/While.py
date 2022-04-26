testArray = "Hello World"
newArrays = testArray.split()
print(newArrays)

stringBuilder = ""
for i in range(max(len(newArrays[0]), len(newArrays[1]))):
    stringBuilder += newArrays[0][i] + newArrays[1][i]
    
print(stringBuilder)