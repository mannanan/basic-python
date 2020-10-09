#Program yang menentukan siswa lulus ujian atau tidak. Siswa dikatakan lulus apabila nilai ujian teori dan nilai ujian praktek adalah 70

t = 69 #teori
p = 69 #praktik
kkm = 70 

if t >= kkm and p >= kkm :
    print ("Selamat !!! Anda lulus ujian")
elif t < kkm and p >= kkm :
    print ("Anda harus mengulang ujian teori")
elif t >= kkm and p < kkm :
    print ("Anda harus mengulang ujian praktek")
elif t < kkm and p < kkm :
    print ("Anda harus mengulang ujian teori dan ujian praktek")