def greeting(nama, pesan):
    return "Halo, " + nama + "! " + pesan

print(greeting("Dicoding", "Selamat pagi!"))
print(greeting(pesan="Selamat sore!", nama="Dicoding"))

def hitung_total(*args):
    print(type(args))
    total = sum(args)
    return total

print(hitung_total(1, 2, 3))

def cetak_info(**kwargs):
    info = ""
    for key, value in kwargs.items():
        info += key + ': ' + value + ", "
    return info

print(cetak_info(nama="AndikaBN", usia="19", pekerjaan="Python Programmer"))

mencari_luas_persegi_panjang = lambda panjang, lebar: panjang*lebar
print(mencari_luas_persegi_panjang(5,10))

a = 10

def add(b):
    result = a+b
    return result

bilanganPertama = add(20)
print(bilanganPertama)

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")
    return 
  
greeting("Indira")