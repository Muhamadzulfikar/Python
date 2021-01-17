#Judul Program
print("\n\t\tProgram menghitung diskon belanja")

#Memasukan total belanja
total=int(input("\nMasukan total belanja :"))

#Kondisi 1
if total >=50000 :
    harga = total * (10/100)
    bayar = total - harga
    print("\nHarga yang anda bayar Rp.",bayar)

#Kondisi 2
elif total >=100000 :
    harga = total * (20/100)
    bayar = total - harga
    print("\nHarga yang anda bayar Rp.",bayar)

#Kondisi 3
elif total >=150000 :
    harga = total * (30/100)
    bayar = total - harga
    print("\nHarga yang anda bayar Rp.",bayar)

#Kondisi bernilai false
else :
    print("\nAnda tidak mendapat diskon")
