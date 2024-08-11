def calculate_average():
    notlar = input("Notları giriniz (virgülle ayırarak): ").split(',')
    notlar = [float(n) for n in notlar]
    ortalama = sum(notlar) / len(notlar)
    print(f"Ortalamanız: {ortalama:.2f}")

def convert_grade():
    grade = float(input("Notu giriniz: "))
    if 90 <= grade <= 100:
        print("Harf Notu: AA")
    elif 85 <= grade < 90:
        print("Harf Notu: BA")
    elif 80 <= grade < 85:
        print("Harf Notu: BB")
    elif 75 <= grade < 80:
        print("Harf Notu: CB")
    elif 70 <= grade < 75:
        print("Harf Notu: CC")
    elif 65 <= grade < 70:
        print("Harf Notu: DC")
    elif 60 <= grade < 65:
        print("Harf Notu: DD")
    elif 50 <= grade < 60:
        print("Harf Notu: FD")
    else:
        print("Harf Notu: FF")
