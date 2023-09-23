print("Selamat datang di Kalkulator BMI!")

tinggi_badan = float(input("Masukan tinggi anda ( dalam meter) : "))
berat_badan = int(input("masukan berat badan anda ( dalam kilogram ):"))

BMI = berat_badan / tinggi_badan**2

if BMI < 18.5:
    print("Hasil perhitungan BMI : ")
    print(f"BMI anda adalah : {BMI}")
    print("anda Kurang berat badan")
elif 18.5 <= BMI < 24.9:
    print("Hasil perhitungan BMI : ")
    print(f"BMI anda adalah : {BMI}")
    print("Berat badan normal")
elif 25 <= BMI < 29.9:
    print("Hasil perhitungan BMI : ")
    print(f"BMI anda adalah : {BMI}")
    print("anda Kelebihan berat badan")
elif BMI > 30:
    print("Hasil perhitungan BMI : ")
    print(f"BMI anda adalah : {BMI}")
    print("anda obesitas")

