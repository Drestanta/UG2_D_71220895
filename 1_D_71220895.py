print("=============== MAKANAN ===============")
print("1. Telor Bakar           : Rp. 7.000")
print("2. Lele Terbang Mas Bhe  : Rp. 10.000")
print("3. Es Coklat Lempu       : Rp. 5.000")
print("4. Es Doger Langensari   : Rp. 13.000")

print("=============== PESANAN ===============")
telor_bakar = int(input("Telor Bakar\t:"))
lele_terbang = int(input("Lele Terbang\t:"))
es_coklat = int(input("Es Coklat\t:"))
es_doger = int(input("Es Doger\t:"))

print("================ TOTAL ================")
ttb = telor_bakar*7000
tlt = lele_terbang*10000
tec = es_coklat*5000
ted = es_doger*13000
total = ttb+tlt+tec+ted
print("TOTAL TELOR BAKAR x ",telor_bakar,"\t: Rp ",ttb)
print("TOTAL LELE TERBANG x ",lele_terbang,"\t: Rp ",tlt)
print("TOTAL ES COKLAT x ",es_coklat,"\t: Rp ",tec)
print("TOTAL ES DOGER x ",es_doger,"\t: Rp ",ted)
print("Jumlah total biaya yang harus dibayar adalah ",total)