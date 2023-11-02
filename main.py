print("\n")
print("="*50)
print("                 Warkop Siap Saji         ")
print("="*50)
print("                     Minuman              ")
print("-"*50)
print("             Minuman            Harga     ")
print("-"*50)
print("             Americano          Rp. 15000 ")
print("             Mocca              Rp. 15000 ")
print("             Cappucino          Rp. 10000 ")
print("             Thai Tea           Rp. 5000  ")
print("             Matcha             Rp. 8000  ")
print("             Susu Soda          Rp. 8000  ")
print("-"*50)
print("                     Makanan              ")
print("-"*50)
print("             Makanan            Harga     ")
print("-"*50)
print("             Roti Bakar         Rp. 10000 ")
print("             Indomie            Rp. 10000 ")
print("             Seblak             Rp. 10000 ")
print("             Bakso Aci          Rp. 10000 ")
print("             Pancong            Rp. 10000 ")
print("             Kentang Goreng     Rp. 5000  ")
print("             Pisang Goreng      Rp. 5000  ")
print("="*50)
print('\n')

banyak_pesanan = int(input('Masukkan Banyak jenis pesanan : '))
pesanan = []
qty = []
nama_pesanan = []
jumlah = []
harga = []

i = 0
while i < banyak_pesanan:
    print("Jenis Ke - ", i + 1)
    pesanan_input = input('Masukkan Nama Menu : ')
    qty_input = int(input("Masukkan Qty : "))

    pesanan.append(pesanan_input)
    qty.append(qty_input)

    # MINUMAN
    if pesanan_input.lower() == "amerikano":
        nama_pesanan.append("Amerikano")
        harga.append(15000) 
        jumlah.append(qty_input * 15000) 

    elif pesanan_input.lower() == "mocca":
        nama_pesanan.append("Mocca")
        harga.append(15000) 
        jumlah.append(qty_input * 15000) 

    elif pesanan_input.lower() == "cappucino":
        nama_pesanan.append("Cappucino")
        harga.append(10000) 
        jumlah.append(qty_input * 10000) 

    elif pesanan_input.lower() == "thai tea":
        nama_pesanan.append("Thai Tea")
        harga.append(5000) 
        jumlah.append(qty_input * 5000) 

    elif pesanan_input.lower() == "matcha":
        nama_pesanan.append("Matcha")
        harga.append(8000) 
        jumlah.append(qty_input * 8000) 

    elif pesanan_input.lower() == "susu soda":
        nama_pesanan.append("Susu Soda")
        harga.append(8000) 
        jumlah.append(qty_input * 8000)
    # AKHIR MINUMAN

    # MAKANAN
    elif pesanan_input.lower() == "roti bakar":
        nama_pesanan.append("Roti Bakar")
        harga.append(10000)
        jumlah.append(qty_input * 10000)

    elif pesanan_input.lower() == "indomie":
        nama_pesanan.append("Indomie")
        harga.append(10000)
        jumlah.append(qty_input * 10000)
        
    elif pesanan_input.lower() == "seblak":
        nama_pesanan.append("Seblak")
        harga.append(10000)
        jumlah.append(qty_input * 10000)

    elif pesanan_input.lower() == "baso aci":
        nama_pesanan.append("Baso Aci")
        harga.append(10000)
        jumlah.append(qty_input * 10000)

    elif pesanan_input.lower() == "pancong":
        nama_pesanan.append("Pancong")
        harga.append(10000)
        jumlah.append(qty_input * 10000)
    
    elif pesanan_input.lower() == "kentang goreng":
        nama_pesanan.append("Kentang Goreng")
        harga.append(5000)
        jumlah.append(qty_input * 5000)

    elif pesanan_input.lower() == "pisang goreng":
        nama_pesanan.append("Pisang Goreng")
        harga.append(5000)
        jumlah.append(qty_input * 5000)
    # AKHIR MAKANAN

    else :
        nama_pesanan.append("Tidak ada di menu")
        harga.append(0)
        jumlah.append(qty_input * 0)
        print()

    i += 1

    
print("\n")
print("============================================================================")
print("                           Warkop Siap Saji                               ")
print("============================================================================")
print("{:<5} {:<30} {:<15} {:<15} {:<15}".format("No.", "Pesanan", "Harga", "Banyak", "Jumlah"))
print("============================================================================")

a = 0
total_harga = 0
nomor_pesanan = 1
while a < banyak_pesanan:
    print("{:<5} {:<30} {:<15} {:<15} {:<15}".format(nomor_pesanan, nama_pesanan[a], harga[a], qty[a], jumlah[a]))
    total_harga += jumlah[a]
    a = a + 1
    nomor_pesanan += 1

print("============================================================================")
print("Total Bayar              : Rp. {}".format(int(total_harga)))
pajak = total_harga * 0.1 
total_bayar = total_harga + pajak
print("jumlah bayar             : Rp. {}".format(int(total_harga)))
print("Pajak 10 %               : Rp. {}".format(int(pajak)))
print("Total Bayar              : Rp. {}".format(int(total_bayar)))
uang_bayar = int(input("Masukkan Uang Pembayaran : Rp. "))
uang_kembalian = uang_bayar - total_bayar
print("Kembalian                : Rp. {}".format(int(uang_kembalian)))
print("============================================================================")
