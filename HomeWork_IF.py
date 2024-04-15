# # Issue_1
# def month_name(month):
#     if month in [1, 2, 12]:
#         return "Зима"
#     elif month in [3, 4, 5]:
#         return "Весна"
#     elif month in [6, 7, 8]:
#         return "Лето"
#     else:
#         return "Осень"

# month = int(input("Введите номер месяца: "))

# print(f"Текущее время года: {month_name(month)}")


# Issue_2
# def user_rank(num):
#     print("Новичок") if num in list(range(1, 1000)) else print("Любитель") if num in list(range(1001, 5000)) else print("Мастер")

# user_rank(int(input()))

# Issue_3
# def final_price(price):
#     discount = 0.95 if price in list(range(1000, 2001)) else 0.9
#     print(f"Сумма с учётом скидки: {round(price*discount, 2)} рублёв =)")

# price = int(input("Введите сумму покупки: "))

# final_price(price)