data_diri = {"nama":"Izmil Arifin", "matkul": "DDP"}

#Akses Dictionary
print(data_diri["nama"])

#Menambah Item
data_diri["prodi"] = "Teknik Informatika"
print(data_diri)

#Update Item
data_diri["nama"] = "Adzana Shaliha"
print(data_diri)

#Menghapus Item
data_diri.pop("matkul")
print(data_diri)

if "nama" in data_diri:
    print("Terdapat nama")
else:
    print("Tidak ada nama")