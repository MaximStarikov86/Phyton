# Задача 2: Найдите сумму цифр трехзначного числа.

# *Пример:*

# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0) |

a = (int(input("Введите трехзначное число: ")))
a1 = a%10
a2 = (a%100 - a1)//10
a3 = a//100 
print(a1+a2+a3)