import random
from random import randint

num = [ 1, 49 ]

print("Choose a number from 1 to 49")
r = num.randint
print(r)
cnum = int(input)
score = 0

if r == cnum:
     score + 1
     print(score) 