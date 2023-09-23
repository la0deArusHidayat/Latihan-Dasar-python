print("Selamat datang di Kalkulator BMI!")

tinggi_badan = float(input("Masukan tinggi anda ( dalam meter) : "))
berat_badan = int(input("masukan berat badan anda ( dalam kilogram ):"))

BM_I = berat_badan / tinggi_badan**2

if BM_I < 18.5:
    print("Hasil perhitungan BMI : ")
    print(f"BMI anda adalah : {BMI}")
    print("anda Kurang berat badan")
elif 18.5 <= BM_I < 24.9:
    print("Hasil perhitungan BMI : ")
    print(f"BMI anda adalah : {BMI}")
    print("Berat badan normal")
elif 25 <= BM_I < 29.9:
    print("Hasil perhitungan BMI : ")
    print(f"BMI anda adalah : {BMI}")
    print("anda Kelebihan berat badan")
elif BMI_I > 30:
    print("Hasil perhitungan BMI : ")
    print(f"BMI anda adalah : {BMI}")
    print("anda obesitas")

