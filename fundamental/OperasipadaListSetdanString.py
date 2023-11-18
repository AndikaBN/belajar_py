# len()

a = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
print(len(a));

b = set([1, 3, 3, 5, 5, 5, 7, 7, 9])
print(b)
print(len(b))

c = "Belajar Python"
print(len(c))

angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
print(f"berikut angka minimal: {min(angka)}")
print(f"berikut angka maximal: {max(angka)}")

genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
print(f"muncul sebanyak: {genap.count(6)} kali")

string = "Belajar Python di Dicoding sangat menyenangkan"
substring = "a"
print(f"muncul sebanyak {string.count(substring)} kali")

kalimat = "Belajar Python di Dicoding sangat menyenangkan"
print('Dicoding' in kalimat)
print('tidak' in kalimat)
print('Dicoding' not in kalimat)
print('tidak' not in kalimat)

print("<==========>")
# Memberikan Nilai untuk Multiple Variable
data = ['shirt', 'white', 'L']
apparel, color, size = data

print(data)
print(apparel)
print(color)
print(size)

#Sort
#Anda bisa menggunakan fungsi sort() untuk mengurutkan angka atau urutan huruf.
kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
kendaraan.sort()
print(kendaraan)

kendaraan.sort(reverse=True)
print(kendaraan)

""" 
- Metode sort tidak dapat mengurutkan list yang memiliki angka dan string sekaligus di dalamnya.

- Metode sort menggunakan urutan ASCII sehingga nilai huruf kapital (uppercase) akan lebih dahulu dibandingkan huruf kecil (lowercase).
"""
