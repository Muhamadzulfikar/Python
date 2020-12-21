#Judul Program
print("\n\t\tToko Online Muhamad Zulfikar")

#Produk di dalam toko
print("\nKode Barang \tNama Barang \tHarga Barang")
print("k001 \t\tShampo \t\tRp.3000")
print("k002 \t\tSabun \t\tRp.5000")
print("k003 \t\tPasta Gigi \tRp.7000")
print("k004 \t\tSikat Gigi \tRp.5000")
print("k005 \t\tSabun Muka \tRp.10000")

#Variabel
i = 1
#Memasukan banyak belanja
banyakbelanja=int(input("\nMasukan berapa banyak anda ingin belanja:"))

jumlah = []
subtotal = []
kodebarang = []

#memasukan kode barang dan jumlah beli
while i <= banyakbelanja:
    k = input("\nMasukan kode barang ke {}:". format(i))
    j = int(input("Masukan Jumlah barang ke {}:". format(i)))

    if k == "k001":
        s = 3000 * j
    elif k == "k002":
        s = 5000 * j
    elif k == "k003":
        s = 7000 * j
    elif k == "k004":
        s = 5000 * j
    elif k == "k005":
        s = 10000 * j
    else :
        s = 0
    
    kodebarang.append(k)
    jumlah.append(j)
    subtotal.append(s)
    
    i = i + 1

def total(subtotal):
    z=0;
    x = subtotal
    jml = len(x)
    for i in range(jml):
        y = x[i]
        z+=y
    return z

total = total(subtotal)

if total >=10000:
    diskon = total * (10/100)
    harga = total - diskon
elif total >=20000:
    diskon = total * (20/100)
    harga = total - diskon
elif total >= 30000:
    diskon = total * (30/100)
else:
    diskon = 0
    harga = total

print("\nTotal harga pembelian anda Rp.{}". format(total))
print("Potongan harga anda Rp.{}". format(diskon))
print("Harga yang harus anda bayar Rp.{}". format(harga))
