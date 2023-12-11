print("""
Menghitung luas bangun datar

Pilih rumus:
1. Persegi
2. Lingkaran
3. Segitiga
""")

LuasBangunDatar = int(input("Masukkan pilihan (1/2/3): " ))

match LuasBangunDatar:
    case 1:
        sisi = int(input("Masukkan panjang sisi persegi:"))
        print("Luas persegi adalah: ", sisi * sisi, "\n")
    case 2:
        jari_jari = int(input("Masukan jari-jari lingkaran: "))
        print("Luas lingkaran adalah: ", 3.14 * jari_jari * jari_jari, "\n")
    case 3:
        alas = int(input("Masukan alas segitiga: "))
        tinggi = int(input("Masukan tinggi segitiga: "))
        print("Luas segitiga adalah: ", 0.5 * alas * tinggi, "\n")
    case _:
        print("Mohon memilih nomor yang sesuai...")