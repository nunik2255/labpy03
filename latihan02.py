print("LATIHAN02")
print("Menampilkan bilangan dan berhenti ketika memasukan angka 0 dan menampilkan bilangan terbesar")
max=0
while True:
    a=int(input("Masukan bilangan : "))
    if max < a :
        max = a
    if a==0:
        break
print("Bilangan terbesarnya adalah = ",max)