import random
s = input("Enter a word: ")
for i in random.sample(s,len(s)):
    print(i.upper())