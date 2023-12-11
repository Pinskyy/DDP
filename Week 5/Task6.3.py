jumlahBaris = int(input("Masukkan Jumlah Baris: "))

for baris in range(1, jumlahBaris + 1):
    for bintang in range(baris):
        print("*", end="")
    print() 