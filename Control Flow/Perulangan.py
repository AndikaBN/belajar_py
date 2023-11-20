
var_list = [1,2,3,4,5,6,7,8,9,10]
for i in var_list:
    print(i)

# range(star, stop, step)
for i in range(1, 10):
    print("* " * i)

# while
count = 1
while count <= 5:
    print(count)
    count += 1

# For Bersarang 
for i in range(1, 3):
    for j in range(1, 3):
        print(i,j)

for i in range(1, 10):
     spaces = " " * (10-i)
     star = "*" * i
     print(spaces + star)

# Kontrol Perulangan
for i in range(2):  # Perulangan tingkat pertama
    print("Perulangan luar:", i)
    for j in range(10):  # Perulangan tingkat kedua
        print("Perulangan dalam:", j)
        if j == 1:
            break  # Menghentikan perulangan dalam jika j = 1

for huruf in 'Dico ding':
    if huruf == ' ':
        break
    print('Huruf saat ini: {}'.format(huruf))


n = 10
while n >= 0:
    n = n - 1
    if n == 7:
        break
    print(n)
else:
    print("Loop selesai")

angka = [1, 2, 3, 4]
pangkat = []
for n in angka:
  pangkat.append(n**2)
print(pangkat)

angka = [1, 2, 3, 4]
pangkat = [n**2 for n in angka]
print(pangkat)

