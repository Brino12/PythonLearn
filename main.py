"""
Ini demo python
"""
print("hello world")
print("my name is robby")

# First Task
jumlah_botol_susu = 100
jumlah_telur = 1587
harga_sebotol_susu = 10000
harga_sebutir_telur = 1500
Uang_andi = 20000

print("Kondisi Toko Mpok Imah")
print(f"Jumlah botol susu {jumlah_botol_susu} botol")
print(f"Jumlah butir telur {jumlah_telur} butir")

if jumlah_botol_susu > 0:
    print("Berapa Harga 1 botol susu?")
    print(f"Harga susu botol {harga_sebotol_susu} per botol")
    print("Apakah telur ada?")

    if jumlah_telur > 0:
        print("Berapa harga 1 butir telur?")
        print(f"Harga satu butir telur {harga_sebutir_telur} per butir")

    if jumlah_telur and jumlah_botol_susu > 0:
        print("mpok imah beli 1 botol susu dan 6 butir telur")
        print(Uang_andi - (1 * harga_sebotol_susu + 6 * harga_sebutir_telur))
        print("Terima Kasih kembalianya")
        print("ini bu belanjaanya")



