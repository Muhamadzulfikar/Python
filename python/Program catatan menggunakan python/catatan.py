judul = []
tanggal = []
isi = []

print("\t\t\tProgram Catatan menggunakan python")
print("\t\t\t==================================")
jumlah = int(input("\nBerapa jumlah catatan yang ingin kamu inputkan:"))

for i in range(jumlah):
    print("\n")
    j = input("Judul catatan \t\t:")
    judul.append(j)
    t = input("tanggal Catatan dibuat \t:")
    tanggal.append(t)
    c = input("isi catatan \t\t:")
    isi.append(c)

for i in range(jumlah):
    print("\n\t\t\tCatatan")
    print("========================================================")
    print("\n")
    print("Judul catatan \t\t:",judul[i])
    print("Tanggal catatan \t:",tanggal[i])
    print("Isi Catatan \t\t:",isi[i])
