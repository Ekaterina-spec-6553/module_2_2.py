first = int(input("first: "))
second = int(input("second: "))
third = int(input("third: "))
if first == second == third:
    print(3)
elif first == second != third != first or first != second == third != first or first == third != second != first:
    print(2)
else:
    print(0)


