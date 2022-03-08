import random
from random import randint
score = 0
c = 6

while 1:
 try:    
  for i in range(6):
    cn = input("Choose a number from 1 to 49\n")
    cn = int(cn)
    l = list(range( 1 , 50 ))
    r = random.choice(l)
    if r == cn:
      score = score + 1
      print("You've scored" , score , "points!")
      l.pop(r - 1)
     # c - 1
     # print(c)
    else:
     print("This isn't quite right")
     print("Answer" ,r)
     l.pop(r - 1)
     #c - 1
     #print(c) 
 except ValueError:
      #print("Integers only...")
      #ch = input("Retry or exit? 1/2\n")
      #print(ch)
      #if ch == 1:
      # main(c)
      #else:
         break
 break
#For loop into function , counter can be provided then externally each time it runs succesfully:
#Space to test define: