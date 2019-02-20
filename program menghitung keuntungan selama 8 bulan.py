print ("program menghitung keuntungan perusahaan dengan modal awal 100 juta")
print ("note:")
print ("keuntungan bulan ke 1 : 0%")
print ("keuntungan bulan ke 2 : 0%")
print ("keuntungan bulan ke 3 : 1%")
print ("keuntungan bulan ke 5 : 5%")
print ("keuntungan bulan ke 8 : 2%")

a=1000000
for x in range(1,9):
    if(x>1 and x<=2):
        b=a*0
        print("keuntungan bulan ke-",x," : ",b)
    if(x>=3 and x<=4):
        c=a*0.1
        print("keuntungan bulan ke-",x," : ",c)
    if(x>=5 and x<=7):
        d=a*0.5
        print("keuntungan bulan ke-",x," : ",d)
    if(x==8):
        e=a*0.2
        print("keuntungan bulan ke-",x," : ",e)
total=b+b+c+c+d+d+d+e
print("\ntotal : ",total)