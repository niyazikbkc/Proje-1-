def calculate_bmi():
    height = float(input("Boyunuzu (metre cinsinden) giriniz: "))
    weight = float(input("Kilonuzu (kg cinsinden) giriniz: "))
    bmi = weight / (height ** 2)
    print(f"Vücut Kitle İndeksiniz: {bmi:.2f}")
    if bmi < 18.5:
        print("Kilo: Zayıf")
    elif 18.5 <= bmi < 24.9:
        print("Kilo: Normal")
    elif 25 <= bmi < 29.9:
        print("Kilo: Fazla Kilolu")
    else:
        print("Kilo: Obez")
