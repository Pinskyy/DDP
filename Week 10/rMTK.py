import math

def penjumlahan(bilangan1, bilangan2):
    hasil = bilangan1 + bilangan2
    print("Hasil penjumlahan dari:",bilangan1,"+",bilangan2,"=",hasil)

def pengurangan(bilangan1, bilangan2):
    hasil = bilangan1 - bilangan2
    print("Hasil pengurangan dari:",bilangan1,"-",bilangan2,"=",hasil)

def perkalian(bilangan1, bilangan2):
    hasil = bilangan1 * bilangan2
    print("Hasil perkalian dari:",bilangan1,"*",bilangan2,"=",hasil)

def pembagian(bilangan1, bilangan2):
    hasil = bilangan1 / bilangan2
    print("Hasil pembagian dari:",bilangan1,"/",bilangan2,"=",hasil)

def perpangkatan(bilangan1, bilangan2):
    hasil = math.pow(bilangan1, bilangan2)
    print("Hasil perpangkatan dari:",bilangan1,"^",bilangan2,"=",hasil)

def faktorial(bilangan1):
    hasil = math.factorial(bilangan1)
    print("Hasil faktorial dari:",bilangan1,"=",hasil)

def sin(bilangan1):
    hasil = math.sin(bilangan1)
    print("Hasil Sin dari:",bilangan1,"=",hasil)

def log10(bilangan1):
    hasil = math.log10(bilangan1)
    print("Hasil Log10 dari:",bilangan1,"=",hasil)

def hasil_bagi(bilangan1, bilangan2):
    hasil = bilangan1 // bilangan2
    print("Hasil bagi dari:",bilangan1,"//",bilangan2,"=",hasil)

def sisa_bagi(bilangan1, bilangan2):
    hasil = bilangan1 % bilangan2
    print("Hasil sisa bagi dari:",bilangan1,"%",bilangan2,"=",hasil)