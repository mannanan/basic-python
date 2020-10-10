pi = 22/7
r = int(input("Masukkan jari-jari lingkaran (cm) : "))
rumus = (pi*(r**2))

text = "Luas lingkaran dengan jari-jari {} cm adalah {} cm\u00b2" .format (r, rumus)

print(text)

#Bonus (Mengubah 2 angka dibelakang koma)

text = "Luas lingkaran dengan jari-jari {} cm adalah {:.2f} cm\u00b2" .format (r, rumus)

print(text)