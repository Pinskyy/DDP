nilai = int(input("Masukkan Nilai: "))

def kriteria(nilai):
    if nilai < 60:
        return "Gagal"
    elif 61 <= nilai <= 70:
        return "Baik"
    elif 71 <= nilai <= 80:
        return "Sangat Baik"
    elif 81 <= nilai <= 100:
        return "Istimewa"
    else:
        return "Nilai tidak valid"

print(kriteria(nilai))
