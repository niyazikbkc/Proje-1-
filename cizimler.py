import math

def draw_square():
    size = int(input("Karenin boyutunu giriniz: "))
    for i in range(size):
        print("█ " * size)

def draw_triangle():
    size = int(input("Üçgenin yüksekliğini giriniz: "))
    for i in range(size):
        print(" " * (size - i - 1) + "* " * (i + 1))

def draw_circle():
    radius = int(input("Çemberin yarıçapını giriniz: "))
    for y in range((2 * radius) + 1):
        for x in range((2 * radius) + 1):
            if math.sqrt((x - radius) ** 2 + (y - radius) ** 2) < radius + 0.5:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
