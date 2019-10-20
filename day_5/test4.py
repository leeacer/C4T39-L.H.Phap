string = input("Enter a number")
digit = 0

for i in range(len(string)):
    if(string[i].isdigit()):
        digit = digit + 1

print(string)
print(digit)