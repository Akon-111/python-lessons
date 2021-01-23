# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 09:59:19 2021

@author: VOVO-BRAT
"""

# SyntaxError - SINTEKS XATOLIK
# print ("Hello world!")

# EOL va EOF xatolik
# EOL (End of Line - qator yakuni) xatoligi sintaks xatolikning bir turi bo'lib, odatda qator oxirida qo'shtirnoq (birtirnoq) ni yopish esdan chiqqanda yuzaga keladi.
# print("Hello Worl!

# EOF (End of function - funktsiya yakuni) xatoligi esa funktsiya oxirida qavsni yopish esdan chiqqanda yuzaga keladi.  
#print ("Hello world!"

#IndentationError - unexpected indent -JOY TASHLASHDA XATOLIK
 #print ("Hello world!")
 
 #IndentationError: expected an indented block
# print("O'ngacha sanaymiz")
# for n in range(10):
# print(n+1)

#RUN TIME ERROR - DASTURNI BAJARISHDA XATOLIK
#TypeError
# son = input("Istalgan son kiriting:")
# print(f"{son} ning kvadrati {son **2} ga teng")

#NameError
# prit("Hello World")

# mevalar = ["olma","uzum","nok","anor","anjir"]
# for meva in mealar:
#     print(meva)

#ValueError invalid literal for int() with base 10: '45.5'
# son = int(input("Istalgan son kiriting:"))
# if son >=0:
#     print("Musbat son")
# else:
#     print("Manfiy son")

#IndexError
# mevalar = ["olma","anor","uzum"]
# print(mevalar[3])

#ZeroDivisionError division by zero
# x , y = 50, 50
# z = 250/(x-y)
# print(z)

#MANTIQIY XATOLAR

# radius = 5
# pi = 4.14
# aylana_yuzi = pi*radius**2
# print(aylana_yuzi)

# son =float(input("Istalgan son kiriting: "))
# ildiz = son ** 1/2
# print(F"{son} ning ildizi {ildiz} ga teng")

# mevalar = ["olma","uzum","nok","anor","anjir"]
# for meva in mevalar:
#     print(meva)
#     print("Dastur tugadi! Etiboringiz uchun rahmad")




#AMALIYOT

# son = float(input("Juft son kiriting>>>:"))
# if son %2 == 1:
#     print("Bu son juft emas.")
# else:
#     print("Rahmad!")





# yosh = int(input("Yoshingiz nechida? "))
# if yosh <=4 or yosh >=60:
#     narh =0
# elif yosh < 18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so\'m")


# x = float(input("Birinchi sonni kiriting: "))
# y = float(input("Ikkinchi sonni kiriting:  "))

# if x == y:
#     print(f"{x} = {y}")
# elif x < y:
#     print(f"{x} < {y}")
# else:
#     print(f"{x} > {y}")

# mahsulotlar = ["un","yog","sovun","tuxum","piyoz","kartoshka","olma","banan","uzum","qovun"]
# savat = []
# for n in range(5):
#     savat.append(input(f"SAvatga {n+1} -mahsulotni qoshing: "))
    
# if savat:
#     for mahsulot in savat:
#         if mahsulot in mahsulotlar:
#             print(f"Dokonimizda {mahsulot} bor")
#         else:
#             print(f"Dokonimizda {mahsulot} yo\'q")
# else:
#     print("Savatingiz bo'sh")


# mahsulotlar = ["un","yog","sovun","tuxum","piyoz","kartoshka","olma","banan","uzum","qovun"]
# savat = []

# for n in range(5):
#     savat.append(input(f'savatga {n + 1} - mahsulotni qo\'shing:'))
# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)
# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
# for mahsulot in mavjud_emas:
#     print(mahsulot)
# else:
#     print("Siz so'ragan barcha mahsulotlar do'konimizda bor")


# users = ["alisher","aziz","yasina", "umar"]
# login = input("Yangi login tanlang:")
# if login in users:
#     print('Login band, yangi login talang!')
# else :
#     print("Xush kelibsiz!")






























