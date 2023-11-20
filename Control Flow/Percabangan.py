ketersediaan = "Daging Ayam"

if ketersediaan == "Daging Ayam":
    print("Emak akan memasak ayam")
else :
    print("Emak akan memasak tempe cuy")

score = int(input("Masukkan score anda: "))

if score == 100:
    print("nilai anda sempurna")
elif score >= 90:
    print("Nilai anda lumayan")
else :
    print("Jangan pernah menyerah")


nilai = 81
perilaku = 'tidak baik'

if nilai>=80 and perilaku == 'baik':
   print("Selamat! Anda mendapat nilai A dan telah berkelakuan baik")
   print("Pertahankan!")
elif nilai>=80 and perilaku != 'baik':
   print("Kamu mendapatkan nilai A, tetapi perilaku Anda kurang baik")
   print("Perbaiki lagi ya!")
else:
   print("Yuk belajar lebih giat lagi!")

# Ternary Operators

lulus = True
print("selamat") if lulus else print("perbaiki")

lulus = False
kelulusan = ("Perbaiki, Anda belum lulus.","Selamat, Anda lulus!")[lulus]
print(kelulusan)