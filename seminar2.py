# Вводятся числа, пока не введется 0. Найти сумму чисел, кратных 3.
# summa = 0
# while True:
#     number = int(input("Введите числа: "))
#     if number == 0:
#         break
#     elif number % 3 == 0:
#         summa += number
# print(summa)


# Сумма чисел: 
# number = int(input("Введите числа: "))
# summa = 0
# while number > 0:
#     summa+= number % 10
#     number //= 10
# print(summa)


# for i in "привет":
#     print (i)

# for i in range (10, 5, -1):       - переменная - итератор используется
#     print (i)

# for i (или можно писать знак _ ) in range (5):       - переменная - итератор не используется
#     print ('hello')           цикл нужен для повтора - hello выводится 5 раз




# Задача 9. По данному целому неотрицательному n вычислите
# значение n!. N! = 1 * 2 * 3 * … * N (произведение всех
# чисел от 1 до N) 0! = 1

# n = int(input("Введите целое неотрицательное число: "))
# multiply = 1
# while n > 0:
#     multiply *= n
#     n -=1
# print(multiply)



# Задача 11. Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.

# input_number = int(input("Введите натуральное число: "))
# first_fibonachi = 0
# second_fibonachi = 1
# tmp_fibonachi = first_fibonachi + second_fibonachi
# index = 2
# while tmp_fibonachi < input_number: 
#     first_fibonachi = second_fibonachi 
#     second_fibonachi = tmp_fibonachi 
#     tmp_fibonachi = first_fibonachi + second_fibonachi 
#     index += 1
# if tmp_fibonachi == input_number: print(index + 1)
# else: print(-1)




# Задача №13. Уставшие от необычно теплой зимы, жители решили узнать,
# действительно ли это самая длинная оттепель за всю историю
# наблюдений за погодой. Они обратились к синоптикам, а те, в
# свою очередь, занялись исследованиями статистики за
# прошлые годы. Их интересует, сколько дней длилась самая
# длинная оттепель. Оттепелью они называют период, в
# который среднесуточная температура ежедневно превышала
# 0 градусов Цельсия. Напишите программу, помогающую
# синоптикам в работе.
# Пользователь вводит число N – общее количество
# рассматриваемых дней (1 ≤ N ≤ 100). В следующих строках
# располагается N целых чисел.
# Каждое число – среднесуточная температура в
# соответствующий день. Температуры – целые числа и лежат в
# диапазоне от –50 до 50

# n = int(input("Кол-во дней"))
# max_snowbreak = 0
# current_snowbreak = 0
# for _ in range(n): 
#     current_T = int(input("введите темперетуру: ")) 
#     if current_T > 0: 
#         current_snowbreak += 1 
#     elif current_snowbreak > max_snowbreak: 
#         max_snowbreak = current_snowbreak 
#         current_snowbreak = 0
# if current_snowbreak > max_snowbreak: 
#     max_snowbreak = current_snowbreak
# print(max_snowbreak)



# 15. Иван Васильевич пришел на рынок и решил купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество арбузов. Вторая строка содержит N чисел, 
# записанных на новой строчке каждое. Здесь каждое число – это масса соответствующего арбуза

# quantity = int(input("Количество арбузов: "))
# max_weight = 0
# min_weight = 0
# for i in range(quantity):
# current_weight = int(input("Вес арбуза: "))
# while current_weight <= 0 or current_weight > 30000:
# print("Такой арбуз не унести")
# current_weight = int(input("Вес арбуза: "))
# if i == 0:
# min_weight = current_weight
# max_weight = current_weight
# if i != 0:
# if current_weight > max_weight and current_weight < 30000:
# max_weight = current_weight
# if current_weight < min_weight and current_weight > 0:
# min_weight = current_weight

# print(f"Арбуз для себя {max_weight}")
# print(f"Арбуз для тещи {min_weight}")