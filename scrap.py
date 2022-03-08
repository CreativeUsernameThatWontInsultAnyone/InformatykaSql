 except ValueError:
      print("Integers only...")
      ch = input("Retry or exit? 1/2\n")
      print(ch)
      if ch == 1:
       main(c)
      else:
         break
 break

 def main():
   for i in range(6):
    cn = input("Choose a number from 1 to 49\n")
    cn = int(cn)
    l = list(range( 1 , 50 ))
    r = random.choice(l)
   if r == cn:
      score = score + 1
      print("You've got" , score , "points!")
      l.pop(r - 1)
     # c - 1
     # print(c)
   else:
    print("Lost")
    print("Answer" ,r)
    l.pop(r - 1)
    #c - 1
    #print(c) 