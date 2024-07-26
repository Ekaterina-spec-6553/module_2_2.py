first = int(input("first: "))
second = int(input("second: "))
third = int(input("third: "))
if first == second == third:
    print(3)
elif first == second != third or first != second == third or first == third != second:
    print(2)
else:
    print(0)



