def duplikat_buah(fruits):
    fruits_duplikat = [buah for buah in fruits for _ in range(2)]
    return fruits_duplikat

fruits = ["pepaya", "mangga", "pisang", "durian", "jambu"]
buah_duplikat = duplikat_buah(fruits)
print(buah_duplikat)