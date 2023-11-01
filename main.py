print("="*50)
print("                 Warkop Siap Saji         ")
print("="*50)
print("                     Minuman              ")
print("="*50)
print("             Minuman            Harga     ")
print("="*50)
print("             Americano          Rp. 15000 ")
print("             Mocca              Rp. 15000 ")
print("             Cappucino          Rp. 10000 ")
print("             Thai Tea           Rp. 5000  ")
print("             Matcha             Rp. 8000  ")
print("             Susu Soda          Rp. 8000  ")
print("="*50)
print("                     Makanan              ")
print("="*50)
print("             Makanan            Harga     ")
print("="*50)
print("             Roti Bakar         Rp. 10000 ")
print("             Indomie            Rp. 10000 ")
print("             Seblak             Rp. 10000 ")
print("             Bakso Aci          Rp. 10000 ")
print("             Pancong            Rp. 10000 ")
print("             Kentang Goreng     Rp. 5000  ")
print("             Pisang Goreng      Rp. 5000  ")
print("="*50)
print('\n')

pesanan = []
qty = []
nama_pesanan = []
jumlah = []
banyak_pesanan = []

banyak_pesanan = input('Masukkan Banyak jenis pesanan : ')
pesanan = input('Masukkan Nama Menu : ')
qty = int(input("Masukkan Qty : "))

i= 0
while i<banyak_pesanan:

    print("Jenis Ke - ", i+1)
    if pesanan[i].lower() == "amerikano" :
        nama_pesanan.append("Amerikano")
        harga.append("15000")
        jumlah.append(qty[i]*int("15000"))

    elif pesanan[i].lower() ==  "mocca" :
        nama_pesanan.append("Mocca")
        harga.append("15000")
        jumlah.append(qty[i]*int("15000"))

    elif pesanan[i].lower() ==  "cappucino" :
        nama_pesanan.append("Cappucino")
        harga.append("10000")
        jumlah.append(qty[i]*int("10000"))

    elif pesanan[i].lower() ==  "thai tea" :
        nama_pesanan.append("Thai Tea")
        harga.append("5000")
        jumlah.append(qty[i]*int("5000"))

    elif pesanan[i].lower() ==  "matcha" :
        nama_pesanan.append("Matcha")
        harga.append("8000")
        jumlah.append(qty[i]*int("8000"))

    elif pesanan[i].lower() ==  "susu soda" :
        nama_pesanan.append("Susu Soda")
        harga.append("8000")
        jumlah.append(qty[i]*int("8000"))
    else :
        nama_pesanan.append("Tidak ada dimenu")
        harga.append("0")
        jumlah.append(qty[i]*int("0"))
        print()

    
