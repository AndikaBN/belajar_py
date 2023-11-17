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