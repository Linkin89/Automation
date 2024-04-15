# Issue_1
def dergee_converter_to_fahrenheit(num):
    fahrenheit_degree = num * 9/5 + 32
    return fahrenheit_degree

celsius_degree = int(input())

print(dergee_converter_to_fahrenheit(celsius_degree))

# Issue_2
# Вычисление факториала
def factorial(num):
    fact = 1
    for i in num:
        fact *= i
    return fact
