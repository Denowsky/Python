def check_triangle(side1, side2, side3):
    if side1 >= side2 + side3 or side2 >= side3 + side1 or side3 >= side1 + side2:
        return "Такой треугольник не существует"
    elif side1 == side2 == side3:
        return "Треугольник является равносторонним"
    elif side1 == side2 or side1 == side3 or side2 == side3:
        return "Треугольник является равнобедренным"
    else:
        return "Треугольник разносторонний"
    
a = int(input("Введите сторону а: "))
b = int(input("Введите сторону b: "))
c = int(input("Введите сторону c: "))

print(check_triangle(a, b, c))