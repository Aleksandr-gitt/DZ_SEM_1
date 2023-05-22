# Задача 6: Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером. Счастливым
# билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех. Т.е. билет с номером
# 385916 – счастливый, т.к. 3+8+5=9+1+6. Вам требуется написать программу, которая проверяет счастливость билета
 
# 385916 -> yes
# 123456 -> no
 
num = input("Введите номер билета: ")
if len(num) != 6:
    print('Вы ввели что-то не то')
else:
    if int(num)%10+int(num)//10%10+int(num)//100%10 == int(num)//1000%10+int(num)//10000%10+int(num)//100000%10:
        print("yes")
    else: 
        print("no")