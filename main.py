# print("\n")
# print("="*50)
# print("                 Warkop Siap Saji         ")
# print("="*50)
# print("                     Minuman              ")
# print("-"*50)
# print("             Minuman            Harga     ")
# print("-"*50)
# print("             Americano          Rp. 15000 ")
# print("             Mocca              Rp. 15000 ")
# print("             Cappucino          Rp. 10000 ")
# print("             Thai Tea           Rp. 5000  ")
# print("             Matcha             Rp. 8000  ")
# print("             Susu Soda          Rp. 8000  ")
# print("-"*50)
# print("                     Makanan              ")
# print("-"*50)
# print("             Makanan            Harga     ")
# print("-"*50)
# print("             Roti Bakar         Rp. 10000 ")
# print("             Indomie            Rp. 10000 ")
# print("             Seblak             Rp. 10000 ")
# print("             Bakso Aci          Rp. 10000 ")
# print("             Pancong            Rp. 10000 ")
# print("             Kentang Goreng     Rp. 5000  ")
# print("             Pisang Goreng      Rp. 5000  ")
# print("="*50)
# print('\n')

# kategori = input('Masukkan kategori pesanan : ')
# pesanan = []
# qty = []
# nama_pesanan = []
# jumlah = []
# harga = []

# i = 0
# for i in range(kategori):
#     print("Jenis Ke - ", i + 1)
#     pesanan_input = input('Masukkan Nama Menu : ')
#     qty_input = int(input("Masukkan Qty : "))

#     pesanan.append(pesanan_input)
#     qty.append(qty_input)

#     # MINUMAN
#     if pesanan_input.lower() == "amerikano":
#         nama_pesanan.append("Amerikano")
#         harga.append(15000) 
#         jumlah.append(qty_input * 15000) 

#     elif pesanan_input.lower() == "mocca":
#         nama_pesanan.append("Mocca")
#         harga.append(15000) 
#         jumlah.append(qty_input * 15000) 

#     elif pesanan_input.lower() == "cappucino":
#         nama_pesanan.append("Cappucino")
#         harga.append(10000) 
#         jumlah.append(qty_input * 10000) 

#     elif pesanan_input.lower() == "thai tea":
#         nama_pesanan.append("Thai Tea")
#         harga.append(5000) 
#         jumlah.append(qty_input * 5000) 

#     elif pesanan_input.lower() == "matcha":
#         nama_pesanan.append("Matcha")
#         harga.append(8000) 
#         jumlah.append(qty_input * 8000) 

#     elif pesanan_input.lower() == "susu soda":
#         nama_pesanan.append("Susu Soda")
#         harga.append(8000) 
#         jumlah.append(qty_input * 8000)
#     # AKHIR MINUMAN

#     # MAKANAN
#     elif pesanan_input.lower() == "roti bakar":
#         nama_pesanan.append("Roti Bakar")
#         harga.append(10000)
#         jumlah.append(qty_input * 10000)

#     elif pesanan_input.lower() == "indomie":
#         nama_pesanan.append("Indomie")
#         harga.append(10000)
#         jumlah.append(qty_input * 10000)
        
#     elif pesanan_input.lower() == "seblak":
#         nama_pesanan.append("Seblak")
#         harga.append(10000)
#         jumlah.append(qty_input * 10000)

#     elif pesanan_input.lower() == "baso aci":
#         nama_pesanan.append("Baso Aci")
#         harga.append(10000)
#         jumlah.append(qty_input * 10000)

#     elif pesanan_input.lower() == "pancong":
#         nama_pesanan.append("Pancong")
#         harga.append(10000)
#         jumlah.append(qty_input * 10000)
    
#     elif pesanan_input.lower() == "kentang goreng":
#         nama_pesanan.append("Kentang Goreng")
#         harga.append(5000)
#         jumlah.append(qty_input * 5000)

#     elif pesanan_input.lower() == "pisang goreng":
#         nama_pesanan.append("Pisang Goreng")
#         harga.append(5000)
#         jumlah.append(qty_input * 5000)
#     # AKHIR MAKANAN

#     else :
#         nama_pesanan.append("Tidak ada di menu")
#         harga.append(0)
#         jumlah.append(qty_input * 0)
#         print()

#     i += 1

    
# print("\n")
# print("============================================================================")
# print("                           Warkop Siap Saji                               ")
# print("============================================================================")
# print("{:<5} {:<30} {:<15} {:<15} {:<15}".format("No.", "Pesanan", "Harga", "Banyak", "Jumlah"))
# print("============================================================================")

# a = 0
# total_harga = 0
# nomor_pesanan = 1
# while a < banyak_pesanan:
#     print("{:<5} {:<30} {:<15} {:<15} {:<15}".format(nomor_pesanan, nama_pesanan[a], harga[a], qty[a], jumlah[a]))
#     total_harga += jumlah[a]
#     a = a + 1
#     nomor_pesanan += 1

# print("============================================================================")
# print("Total Bayar              : Rp. {}".format(int(total_harga)))
# pajak = total_harga * 0.1 
# total_bayar = total_harga + pajak
# print("jumlah bayar             : Rp. {}".format(int(total_harga)))
# print("Pajak 10 %               : Rp. {}".format(int(pajak)))
# print("Total Bayar              : Rp. {}".format(int(total_bayar)))
# uang_bayar = int(input("Masukkan Uang Pembayaran : Rp. "))
# uang_kembalian = uang_bayar - total_bayar
# print("Kembalian                : Rp. {}".format(int(uang_kembalian)))
# print("============================================================================")



# pakai kategori

# print("\n")
# print("="*50)
# print("                 Warkop Siap Saji         ")
# print("="*50)

# kategori = input('Pilih kategori pesanan (Makanan/Minuman): ')

# menu_makanan = {
#     "roti bakar": 10000,
#     "indomie": 10000,
#     "seblak": 10000,
#     "bakso aci": 10000,
#     "pancong": 10000,
#     "kentang goreng": 5000,
#     "pisang goreng": 5000
# }

# menu_minuman = {
#     "americano": 15000,
#     "mocca": 15000,
#     "cappucino": 10000,
#     "thai tea": 5000,
#     "matcha": 8000,
#     "susu soda": 8000
# }

# if kategori.lower() == "makanan":
#     print("                     Makanan              ")
#     print("-"*50)
#     print("{:<20} {:<15}".format("Makanan", "Harga"))
#     print("-"*50)
#     for makanan, harga in menu_makanan.items():
#         print("{:<20} Rp. {:<15}".format(makanan, harga))
#     print("-"*50)
# elif kategori.lower() == "minuman":
#     print("                     Minuman              ")
#     print("-"*50)
#     print("{:<20} {:<15}".format("Minuman", "Harga"))
#     print("-"*50)
#     for minuman, harga in menu_minuman.items():
#         print("{:<20} Rp. {:<15}".format(minuman, harga))
#     print("-"*50)
# else:
#     print("Kategori pesanan tidak valid. Silakan pilih 'Makanan' atau 'Minuman'.")

# pesanan = []
# nama_pesanan = []
# harga = []
# total_harga = 0

# while True:
#     pesanan_input = input('Masukkan Nama Menu (ketik "selesai" untuk selesai): ')

#     if pesanan_input.lower() == "selesai":
#         break

#     if pesanan_input.lower() in menu_makanan and kategori.lower() == "makanan":
#         pesanan.append(pesanan_input)
#         nama_pesanan.append(pesanan_input)
#         harga.append(menu_makanan[pesanan_input])
#         total_harga += menu_makanan[pesanan_input]
#     elif pesanan_input.lower() in menu_minuman and kategori.lower() == "minuman":
#         pesanan.append(pesanan_input)
#         nama_pesanan.append(pesanan_input)
#         harga.append(menu_minuman[pesanan_input])
#         total_harga += menu_minuman[pesanan_input]
#     else:
#         print("Menu tidak valid.")

# print("\n")
# print("============================================================================")
# print("                 Warkop Siap Saji - Rincian Pesanan                       ")
# print("============================================================================")
# print("{:<5} {:<30} {:<15}".format("No.", "Pesanan", "Harga"))
# print("============================================================================")

# for i, (nama, hrg) in enumerate(zip(nama_pesanan, harga), start=1):
#     print("{:<5} {:<30} Rp. {:<15}".format(i, nama, hrg))

# print("============================================================================")
# print("Total Bayar              : Rp. {}".format(total_harga))
# pajak = total_harga * 0.1
# total_bayar = total_harga + pajak
# print("Jumlah bayar             : Rp. {}".format(total_harga))
# print("Pajak 10 %               : Rp. {}".format(pajak))
# print("Total Bayar              : Rp. {}".format(total_bayar))
# uang_bayar = int(input("Masukkan Uang Pembayaran : Rp. "))
# uang_kembalian = uang_bayar - total_bayar
# print("Kembalian                : Rp. {}".format(uang_kembalian))
# print("============================================================================")


# tidak pakai kategori

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

menu_makanan = {
    "roti bakar": 10000,
    "indomie": 10000,
    "seblak": 10000,
    "bakso aci": 10000,
    "pancong": 10000,
    "kentang goreng": 5000,
    "pisang goreng": 5000
}

menu_minuman = {
    "americano": 15000,
    "mocca": 15000,
    "cappucino": 10000,
    "thai tea": 5000,
    "matcha": 8000,
    "susu soda": 8000
}

pesanan = []
nama_pesanan = []
harga = []
qty_pesanan = []
total_harga = 0

while True:
    pesanan_input = input('Masukkan Nama Menu (ketik "selesai" untuk selesai): ')

    if pesanan_input.lower() == "selesai":
        break

    if pesanan_input.lower() in menu_makanan or pesanan_input.lower() in menu_minuman:
        qty_input = int(input('Masukkan Qty: '))
        
        if pesanan_input.lower() in menu_makanan:
            pesanan.append(pesanan_input)
            nama_pesanan.append(pesanan_input)
            harga.append(menu_makanan[pesanan_input])
            qty_pesanan.append(qty_input)
            total_harga += menu_makanan[pesanan_input] * qty_input
        elif pesanan_input.lower() in menu_minuman:
            pesanan.append(pesanan_input)
            nama_pesanan.append(pesanan_input)
            harga.append(menu_minuman[pesanan_input])
            qty_pesanan.append(qty_input)
            total_harga += menu_minuman[pesanan_input] * qty_input
    else:
        print("Menu tidak valid.")

print("\n")
print("============================================================================")
print("                 Warkop Siap Saji - Rincian Pesanan                       ")
print("============================================================================")
print("{:<5} {:<30} {:<15} {:<10} {:<15}".format("No.", "Pesanan", "Harga", "Qty", "Jumlah"))
print("============================================================================")

for i, (nama, hrg, qty, jumlah) in enumerate(zip(nama_pesanan, harga, qty_pesanan, [h * q for h, q in zip(harga, qty_pesanan)]), start=1):
    print("{:<5} {:<30} Rp. {:<15} {:<10} Rp. {:<15}".format(i, nama, hrg, qty, jumlah))

print("============================================================================")
print("Total Bayar              : Rp. {}".format(total_harga))
pajak = total_harga * 0.1
total_bayar = total_harga + pajak
print("Jumlah bayar             : Rp. {}".format(total_harga))
print("Pajak 10 %               : Rp. {}".format(pajak))
print("Total Bayar              : Rp. {}".format(total_bayar))
uang_bayar = int(input("Masukkan Uang Pembayaran : Rp. "))
uang_kembalian = uang_bayar - total_bayar
print("Kembalian                : Rp. {}".format(uang_kembalian))
print("============================================================================")
