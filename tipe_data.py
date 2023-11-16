#tipe data primitif
#1. integer
umur = 19
bb = 70.0
minus = -90

#2. float
phi = 3.14
semb = 4.01E+1

#3. complex
vA = 1+2j

#4. boolean
x = True
y= False

#5. String
z = "Dicoding"

print(type(umur))
print(type(phi))
print(type(vA))
print(id(bb))
print(z[0])
print(z[2:])
print(f'hallo saya belajar coding ini di {z}, sangat {x}')
print('hallo gueh di %s' %(z))
print('kalo buat aplikasi ya {}'.format(z))

print("<=====================================>")
#tipe data collection

variabel_list = [1, "AnbinDev", True, 3.14];

variabel_list[0] = "Indira"

print(variabel_list[0])

a = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]

print(a[0])
print(a[2])
print(a[-1])
print(a[-3])

# sequence[start:stop:step]

print(a[0:5:2])
print(a[1:])
print(a[2:7:2])

#Tuple
variabel_tuple = (12, "Machine Learning", 1+2j)
# variabel_tuple[0] = 'Java'

#Set
set_1 ={1,2,3,4,5} 
set_2 ={4,5,6,7,8}

union = set_1.union(set_2)
print("union", union)

intersection = set_1.intersection(set_2)
print(intersection)

#Dictionary

id = {"name":"andika bintang nursalih", "age":19, "isMarried":False}
