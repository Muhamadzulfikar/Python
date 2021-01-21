nama = []
p1 = []
p2 = []
pasaruang = []
obligasi = []
saham = []
level =[]
uang = []
print("\tProgram pemilihan reksadana yang cocok menurut profil resiko")

data = int(input("\nMasukan banyak data:"))

for i in range(data):
    a = input("\nMasukan Nama anda:")
    nama.append(a)

    print("\n{} silahkan jawab pertanyaan dibawah ini".format(nama[i]))

    print("\nDalam Investasi apa yang paling penting")
    print("1.Memaksimalkan Keuntungan")
    print("2.Menghindari Kerugian")
    print("3.Keduanya sama penting")

    b = int(input("\nMasukan jawaban anda dengan memasukan angka 1-3:"))
    p1.append(b)

    print("\nPasar uang seringkali naik-turun jika nilai investasi kamu turun 15%")
    print("dalam sebulan dengan keadaan pasar yang tidak menentu, apa yang akan")
    print("kamu lakukan?")
    print("1.Jual Semua")
    print("2.Jual Sebagian")
    print("3.Simpan Semua")
    print("4.Beli Lagi")

    c = int(input("\nMasukan jawaban anda dengan memasukan angka 1-4:"))
    p2.append(c)

    if b==1 and c==1:
        d = (10/100)
        e = (65/100)
        f  = (25/100)
        g = "moderat"
    elif b==1 and c==2:
        d = (10/100)
        e = (53/100)
        f = (37/100)
        g = "konservatif"
    elif b==1 and c==3:
        d = (10/100)
        e = (43/100)
        f = (47/100)
        g = "moderat"
    elif b==1 and c==4:
        d = (10/100)
        e = (34/100)
        f = (56/100)
        g = "agresif"
    pasaruang.append(d)
    obligasi.append(e)
    saham.append(f)
    level.append(g)
    
for i in range(data):
    print("\n{} Profile resiko kamu di level {}".format(nama[i],level[i]))
    print("Pasar uang {}%".format(pasaruang[i] * 100))
    print("Obligasi {}%".format(obligasi[i] * 100))
    print("Saham {}%".format(saham[i] * 100))

for i in range (data):
    h = int(input("\n{} Masukan jumlah uang yang ingin kamu investasikan:Rp.".format(nama[i])))
    uang.append(h)
    print("{} Berikut ini kami tampilkan pembagian uang kamu kedalam instrumen reksadana".format(nama[i])) 
    print("\nReksadana Pasar Uang\t:Rp.{}".format(uang[i] * pasaruang[i]))
    print("Reksadana Obligasi\t:Rp.{}".format(uang[i] * obligasi[i]))
    print("Reksadana Saham\t\t:Rp.{}".format(uang[i] * saham[i]))
