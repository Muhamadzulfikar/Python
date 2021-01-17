print("\t \t Program mencari gaji karyawan")
print("====================================================================")

#tahap input data
nama = input("Masukan nama karyawan \t \t:")
nik = input("Masukan nik \t \t \t:")
gj_pokok = input("Masukan nominal gaji pokok \t:")

#tahap proses
if int(gj_pokok) <= 500000:
    gaji = int(gj_pokok)

    #proses output data
    print("\n ====================================")
    print("\n \t Data karyawan PT XYZ")
    print("\n ====================================")
    print("\n Nama Karyawan \t :",nama)
    print("\n NIK Karayawan \t :",nik)
    print("\n Tunjangan     \t : Tidak ada")
    print("\n Gaji Karyawan \t : Rp",gaji)

#tahap percabangan
else :
    tunjangan = int(gj_pokok) * 0.1
    gaji = int(gj_pokok) + int(tunjangan)
    
    #tahap output data
    print("\n ====================================")
    print("\n \t Data karyawan PT XYZ")
    print("\n =====================================")
    print("\n Nama Karyawan \t:",nama)
    print("\n NIK Karyawan  \t: Rp",nik)
    print("\n Tunjangan     \t:",tunjangan)
    print("\n Gaji Karyawan \t:",gaji)



