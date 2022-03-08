import random
from random import randint
c = 6
l = list(range( 1 , 50 ))
def main():
    i = len(l)
    print(i)
    print(l)
    r = int(input("Which index do you want removed?\n"))
    l.pop(r)
    print(l)
main()