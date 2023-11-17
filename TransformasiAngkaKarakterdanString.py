# Mengubah Huruf Besar/Kecil

x = "Dicoding"
print(x.upper());

y = "DICODING"
print(y.lower());

# Awalan dan Akhiran

print("Dicoding        ".rstrip())
print("           Dicoding".lstrip())
print("           Dicoding         ".strip())

z = "CodeCodeDicodingCodeCode"
print(z.strip("Code"))

print("Dicoding Indonesia".startswith('Dicoding'))
print("Dicoding Indonesia".endswith('Dicoding'))

# Memisah dan Menggabung String

print(" ".join(["Yokoso","no", "WTC"]))

print('123'.join(['Sedang','Ngoding','ini','coy']))

print("Flutter Dart Javascript Python Mechine_Learning".split())

print('''
    Halo,
    aku ikan,
    aku suka sekali menyelam
    aku tinggal di perairan.
    Badanku licin dan renangku cepat.
    Senang berkenalan denganmu.
      '''.split('\n'))

# Mengganti Elemen String
string = 'belajar coding lah'
print(string.replace("lah", "supaya bisa gapai cita2"))


