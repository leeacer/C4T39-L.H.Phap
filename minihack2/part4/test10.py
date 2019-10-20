a = [int(x) for x in input("Enter a list element separated by space ").split()]
for num in a: 
	if num % 2 == 0: 
	    print(num, end=" ") 