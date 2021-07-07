# x=input('enter any number')
# if x == '7':
#     print('7 is lucky number! Tiday is your lucky day!')
# else:
#     print('Thank you. Yave a nice day.')

# height=int(input("введите рост (см)"))
# weight=int(input('введите вес' ))
# bmi=(weight/((height/100)**2))
#
#
# if bmi <=18.4:
#     print("дистрофия")
# elif bmi <=25:
#     print("норма")
# elif bmi <=30:
#     print("предожирение")
# elif bmi <=35:
#     print("ожирение 1 степени")
# elif bmi <=40:
#     print("ожирение 2 степени")
# elif bmi <=40.1:
#     print("ожирение 3 степени")

#Напишите код, который выводит сообщение: 'Enter an integer number'.
# Если было введено чётное число, должно выводиться сообщение: 'The number is even',
# если было введено нечётное число, должно выводиться сообщение 'The number is odd'

x=int(input('Enter an integer number'))
if x%2==0:
    print('the number is четное')
else:
    print('The number is нечетное')
