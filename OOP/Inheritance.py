class Mobil:
    def __init__(self, warna, merek, kecepatan):
        self.warna = warna
        self.merek = merek
        self.kecepatan = kecepatan
    
    def tambah_kecepatan(self):
        print(f"menambah kecepatan: {True}")
        self.kecepatan += 10

class MobilSport(Mobil):
    def turbo(self):
        self.kecepatan += 50


mobil_WTC = Mobil("IRENG", "WTC", 123)
mobil_sport_wtc = MobilSport("PUTIH", "WTC", 225)
print(f"mobil sport wtc: {mobil_sport_wtc.kecepatan} km/jam")
mobil_sport_wtc.tambah_kecepatan()
print(f"mobil sport wtc: {mobil_sport_wtc.kecepatan} km/jam")
# print(mobil_WTC.kecepatan)
# mobil_WTC.tambah_kecepatan()
# print(mobil_WTC.kecepatan)
print(" ")
print("<=======Override=======>")
