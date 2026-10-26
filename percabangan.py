# input
nilai =int(input("masukan nilai:")) 
# proses
if nilai >=80 and nilai<=100:
    print("anda mendapatkan nilai A")
elif nilai >70 and nilai <=80:
    print("anda mendapatkan nilai B") 
elif nilai >=50 and nilai <=70:
    print("anda mendapatkan nilai C")    
elif nilai >=30 and nilai <=50:
    print("anda mendapatkan nilai D")
elif nilai >=0 and nilai <=20:
    print("anda mendapatkan nilai E")    
else:
    print("data tidak valid")
print("========LATIHAN========") 


#input
barang =input("masukan nama barang : ")
harga =int(input("harga barang : "))
# proses
if barang=="kulkas":
   print(harga -(0.10 * harga))
elif barang =="tv":
   print(harga-(0.5 * harga))
else:
    print(barang) 
    print(harga)     

    
    


    

