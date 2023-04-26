n = int(input("Количество долек по горизонтале: "))
m = int(input("Количество долек по вертикале: "))
k = int(input("Количество отломленных долек: "))
x = n * m
if k <= x and (k % n == 0 or k % m == 0):
    print("yes")
else:
    print("no")
