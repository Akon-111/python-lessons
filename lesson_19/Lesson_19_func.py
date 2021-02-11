# -*- coding: utf-8 -*-
"""
Created on Wed Feb 10 19:03:59 2021

@author: VOVO-BRAT
"""

# def salom_ber():
#     """ Salom beruvchi funkisiya"""
#     print("Assalomu alaykum")
# salom_ber()

# def salom_ber(ism):
#     """Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('hasan')
# salom_ber('olim')



# DOCSTRING
# print(salom_ber.__doc__)


#ARGUMENT VA PARAMETER

# def toliq_ism(ism,familya):
#     """ Foydalanuvchi ism va familyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familyasi: {familya.title()}")
# toliq_ism('aziz','hakimov')

# def yosh_hisobla(ism,tugulgan_yil):
#     """Foydalanuvchidan yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2021 - tugulgan_yil} yoshda")
# yosh_hisobla('olim',1997)




#KALIT SO'Z BILAN UZATISH

# def yosh_hisobla(ism,tugilgan_yil):
#     """ Foydalanuvchi yoshini hisoblaydigan dastur"""
#     print(f"{ism.title()} {2021 - tugilgan_yil} yoshda")
# yosh_hisobla(tugilgan_yil=1997,ism='olim')



# STANDART QIYMAT

# def yosh_hisobla(tugilgan_yil,joriy_yil=2020):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz!")
# yosh_hisobla(1995)



#FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR

# def yosh_hisobla(tugilgan_yil,joriy_yil=2021):
#     """Foydalanuvchi tug'ulgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz!")
# tyil= int(input("Tug'ilgan yilingizni kiriting:>>>"))
# yosh_hisobla(tyil)



# def yosh_hisobla(tugilgan_yil,joriy_yil):
#     """Foydalanuvchi tugulgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil - tugilgan_yil} yoshdasiz!")
# yosh_hisobla(1993,2021)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")
# salom_ber()

# def toliq_ism(ism,familya):
#     """Foydalanuvchi ism va familyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuchi familyasi: {familya.title()}")
# toliq_ism('olim',' hajimov')

#AMALIYOT
#1.
# def yosh_hisobla(ism,yosh,joriy_yil=2021):
#     """Foydalanuvchidan ismi va yoshini jamlab chiqarish funksiyasi"""
#     print(f"Salom {ism.title()}\n"
#           f"{ism.title()} siz {joriy_yil - yosh } - yilsiz!")
# ismi = input("Ismingizni kiriting?>>")
# yoshi =int(input("Yoshingizni kiriting>>"))
# yosh_hisobla(ismi,yoshi)

#2.
# def kub_kv_hisobla(son):
#     """Faydalanuvchidan son olib soni kv va kub ni hisoblovchi funksiya"""
#     print(f"Siz kiritkan soni kv {son ** 2} ga teng\n"
#           f"Siz kiritkan soni kub { son**3} ga teng")
# soni=int(input("Yoqtirgan soningizni kiriting:>>>"))
# kub_kv_hisobla(soni)

#3.
# def juft_son_hisobla(son):
#     """Juft soni hisoblovchi funksiya"""
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
# juft_son_hisobla(24)

#4.
# def sonlari_kattasini_tob(x,y):
#     """Ikkta sonni katta kichikligini aniqlovchi funksiya"""
#     if x > y:
#         print (f"{x} katta {y} dan")
#     elif x < y:
#         print(f"{x} kichkina {y} dan")
#     else:
#         print(f"{x} va {y} teng qiymatka ega")        
# sonlari_kattasini_tob(10,1)

#5.
# def hisobla(x,y):
#     """ Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya """
#     print(f"{x**y} songa teng")
# hisobla(8,9)

#6.
# def hisobla (x,y=2):
#     """ Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya """
#     print(f"{x**y} ga teng")
# hisobla(25)

#7.
# def sonni_qoldiqsizligini_tekshir(son):
#     for n in range(2,11):
#         if not son%n :
#             print(f"{son} {n} ga qoldiqsiz bolinadi")
# sonni_qoldiqsizligini_tekshir(70)
        