print("""
Menghitung Luas dan Keliling Trapesium
Pilih rumus:
1. Luas
2. Keliling
""")

LuasdanKeliling_Trapesium = int(input("Masukkan pilihan: "))

panjang_atas = int(input("Masukkan panjang sisi atas Trapesium: "))
panjang_bawah = int(input("Masukkan panjang sisi bawah Trapesium: "))
tinggi = int(input("Masukkan tinggi Trapesium: "))
panjang_miring = int(input("Masukkan panjang sisi miring Trapesium: "))

# Gunakan `elif` untuk mengecek pilihan
if LuasdanKeliling_Trapesium == 1:
    Luas = 0.5 * (panjang_atas + panjang_bawah) * tinggi
    print("Luas Trapesium adalah:", Luas)
elif LuasdanKeliling_Trapesium == 2:
    Keliling = panjang_atas + panjang_bawah + (2 * panjang_miring)
    print("Keliling Trapesium adalah:", Keliling)
else:
    print("Pilihan tidak valid")
