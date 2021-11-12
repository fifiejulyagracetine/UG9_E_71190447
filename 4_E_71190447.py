a = int(input("Masukkan bilangan awal pada deret geometri: "))
n = int(input("Masukkan jumlah suku ke n: "))
r = int(input("Masukkan ratio: "))

total = 0
nilai = a
print("Hasil deret geometri adalah sebagai berikut :", end = " ")
for i in range(n):
    print("%d  " %nilai, end = " ")
    total = total + nilai
    nilai = nilai * r
    
print("\nJumlah dari deret geometri sampai suku ke 11 adalah :" , total)
