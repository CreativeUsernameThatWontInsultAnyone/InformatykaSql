mylist = ["Katarzyna", "Marek", "Anna", "Maria", "Zofia",  "Kacper", "Julia",  "Klaudiusz",  "Jakub", "Radek"]
for element in range(len(mylist)):
    print(mylist[element])
    e = mylist[element]
    lenght = len(e)
    last_char = e[lenght -1]
    if last_char == "a":
        print("Imie Zenskie")
    else:
        print("Imie Meskie")