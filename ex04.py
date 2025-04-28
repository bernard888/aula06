valor_a = [1, 2, 3, 4, 5]
valor_m = [0, 0, 0, 0, 0]
valor_x = float(input("digite um valor x: "))

for y in range(len(valor_a)):
    valor_m[y] = valor_x * valor_a

for i in range(len(valor_m)):
    valor_m[i] = valor_x*valor_a[i]

print(valor_m)