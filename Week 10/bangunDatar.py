def persegi(sisi):
    luas = sisi * sisi
    keliling = 4 * sisi
    print("Luas Persegi: ", luas)
    print("Keliling Persegi: ", keliling)

def persegi_panjang(panjang, lebar):
    luas = panjang * lebar
    keliling = 2 * (panjang + lebar)
    print("Luas Persegi Panjang: ", luas)
    print("Keliling Persegi Panjang: ", keliling)

def lingkaran(jari2):
    en = 3.14
    luas = en * jari2 * jari2
    keliling = 2 * en * jari2
    print("Luas Lingkaran: ", luas)
    print("Keliling Lingkaran: ", keliling)

def segitiga_samasisi(alas, tinggi):
    luas = 0.5 * alas * tinggi
    keliling = alas * 3
    print("Luas Segitiga: ", luas)
    print("Keliling Segitiga: ", keliling)

def belah_ketupat(diagonal1, diagonal2, sisi):
    luas = 0.5 * diagonal1 * diagonal2
    keliling = 4 * sisi
    print("Luas Belah Ketupat: ", luas)
    print("Keliling Belah Ketupat: ", keliling)

def jajargenjang(alas, tinggi, sisi_miring):
    luas = alas * tinggi
    keliling = 2 * alas + sisi_miring
    print("Luas Jajargenjang: ", luas)
    print("Keliling Jajargenjang: ", keliling)

def layang_layang(diagonal1, diagonal2, sisi_atas, sisi_bawah):
    luas = 0.5 *  diagonal1 * diagonal2
    keliling = (sisi_atas * 2) + (sisi_bawah * 2)
    print("Luas Layang-Layang: ",luas)
    print("Keliling Layang-Layang: ",keliling)