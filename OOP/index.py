class mobil:
    warna = "merah"

mobil_1 = mobil()
mobil_1.warna = "biru"
print(mobil_1.warna)

mobil_2 = mobil()
mobil_3 = mobil()

print(mobil_2.warna)
print(mobil_3.warna)

mobil.warna = "IRENG"

print(mobil_2.warna)
print(mobil_3.warna)