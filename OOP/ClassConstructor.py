class Mobil:
    def __init__(self, warna, kecepatan, merek):
        self.warna = warna
        self.kecepatan = kecepatan
        self.merek = merek

    def tambah_kecepatan(self):
        self.kecepatan += 10

mobil_1 = Mobil("Merah", 160, "SAMSUNG")
mobil_2 = Mobil("IRENG", 225, "ASUS")
print(f" mobil 1 keceparan: {mobil_1.kecepatan} km/jam")
print(f" mobil 2 merek: {mobil_2.merek}")

mobil_1.tambah_kecepatan()
print(f" mobil 1 tambah kecepatan: {mobil_1.kecepatan} km/jam")

print("<=====================METHOD=====================>")
 
def my_decorator(func):
    def wrapper():
        print("belum di eksekusi")
        func()
        print("setelah di eksekusi")
    return wrapper


@my_decorator
def say_Hello():
    print("Hello World")


say_Hello()
