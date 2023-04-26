a = input("Введите шестизначный номер билета: ")

a1 = int(a[0])
a2 = int(a[1])
a3 = int(a[2])
a4 = int(a[3])
a5 = int(a[4])
a6 = int(a[5])

if a1 + a2 + a3 == a4 + a5 + a6:
    print("yes")
else:
    print("no")
