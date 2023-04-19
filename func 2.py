### Нахождение факториала
# def factorial(n):
#     if n!=0:
#         return n*factorial(n-1)
#     else:
#         return 1
# print(factorial(5))


# def func(x): return x
#
#
# a1 = func
# a2 = a1
#
# print(a2(10))
#
# print(id(func), id(a1), id(a2))

### Функция лямбда
# a = lambda x, y: x * y
# print(a(2, 3), type(a))

# a = lambda x=1, y=1: x * y
# print(a(), type(a))
# print(a(2, 2), type(a))
# print(a(2, 3), type(a))


# print((lambda x, y: x * y)(2, 3))
# print((lambda x=1, y=1: x * y)())
# print((lambda x=1, y=1: x * y)(2, 3))


# def func1(a):
#     def func2(b):
#         return a * b
#
#     return func2
#
#
# print(func1(2)(4))  # a = 2 b = 4



#Функция которая умножает все на 3
# def func1(a):
#     def func2(b):
#         return a * b
#
#     return func2
#
# three_mul = func1(3)
# print(three_mul(5))
# print(three_mul(10))



###  Вызов декаратора .вариант 1
# def first():
#     print('Test function 1')
# def second():
#     print('Test function 2')
#
# def simple_decor(fn):
#     def wrapper():
#         print('Start function')
#         fn()  # fn - first - first()
#         print('Stop function')
#     return wrapper
# f1 = simple_decor(first)
# f1()
# f2 = simple_decor(second)
# f2()


# ###  Вызов декаратора .вариант 2
#
# def simple_decor(fn):
#     def wrapper():
#         print('Start function')
#         fn()  # fn - first - first()
#         print('Stop function')
#
#     return wrapper
# @simple_decor
# def first():
#     print('Test function 1')
# @simple_decor
# def second():
#     print('Test function 2')
# first()
# second()




# def simple_decor(fn):
#     def wrapper(arg):
#         print(f"Start function: {fn.name}, with arg {arg}")
#         fn(arg)
#
#     return wrapper
#
#
# @simple_decor
# def func1(x):
#     print(x ** 2)
#
#
# func1(2)  # 2 = x = arg

####ZADACHA1
# a = int(input("введите число от 1 до 1000: "))
#
# if 0 < a < 10:
#     print('разряд 1')
# elif 10 <= a <= 99:
#     print('разряд 2')
# elif 99 < a < 999:
#     print('разряд 3')
# else:
#     print("разряд 4")



# def digits(n):
#     return len(str(abs(n)))
#
# print('Количество разрядов: ', digits(123))



# def razr2(x2):
#     return len(x2)
#
#
# print(razr2(x2=input('Put a number: ')))


# def tipes(n, r):
#     if n / 1 >= 1:
#         r += 1
#     if n / 10 > 1:
#         r += 1
#     if n / 100 > 1:
#         r += 1
#     if n / 1000 > 1:
#         r += 1
#     return r
#
#
# print(tipes(15099, 0))



# def razr(x):
#     razr_no = 0
#     for i in x:
#         if i.isdigit():
#             razr_no += 1
#         else:
#             pass
#     return razr_no
#
#
# print(razr(x=input('Put a number: ')))



####!!!! препод
# def digits(n):
#     i = 0
#     while n > 0:
#         n = n//10
#         i += 1
#     return i
#
# num = abs(int(input('Введите число: ')))
# print('Количество разрядов:', digits(num))



#### Задание 2

# def funcX(*args, **kwargs):
#     iargs = 1
#     print('Every odd position:')
#     for i in args:
#         if iargs % 2:
#             print(i)
#         iargs += 1
#     print("Every value which is str")
#     for i2 in kwargs.values():
#         if type(i2) is str:
#             print(i2)
#
#
# funcX(4,12,5,7,354,a='das', bn='g1', sa=12, adw='312')


# def func(*args, **kwargs):
#     print('Позиционные параметры с нечетными индексами', args[1::2])
#     for key, value in kwargs.items():
#         if value == type(str):
#             print('Именованные параметры, в которых значения я вляются строками: ', kwargs.values())


#### Задание №3

# import random
#
#
# def randlist(x, y):
#     [random.randint(x, y) for i in range(10)]
#
#
# print(randlist(x=int(input('Start range at: ')),
#                y=int(input('Finish range at: '))))



# import random
#
#
# def func(a, b):
#     l = [random.randint(a, b) for i in range(10)]
#     print(l)
#
#
# a1 = int(input('введите число '))
# b1 = int(input('введите число '))
# func(a1, b1)



#### Задание 4

# def f1():
#     param = 'some parametr'
#     return param
#
# def f2(param):
#     param2 = 'some parametr 2'
#     return param, param2
#
# print(f2(f1()))


# def f1():
#     a = 12
#     return a
#
#
# def f2(x):
#     return 3 * x
#
#
# print(f2(f1()))