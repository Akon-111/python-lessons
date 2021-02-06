# -*- coding: utf-8 -*-
"""
Created on Sat Feb  6 09:38:40 2021

@author: VOVO-BRAT
"""

#WHILE YORDAMIDA RO'YXATNI TO'LDIRISH

# ismlar = []

# print ("Yaqin do'stingiz ro'yxatini tuzamiz.")
# n=1
# while True:
#     savol = f"{n} - do'stingiz simini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi? (ha/yo'q)")
#     if javob =='ha':
#         n+=1
#         continue
#     else:
#         break
# print("Dostlaringiz ro'yhati")
# for ism in ismlar:
#     print(ism.title())


# WHILE YORDAMIDA LUG'ATNI TO'LDIRISH

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting:")
#     yosh = input(f"{ism.title()} ning yoshini kiriting:")
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana malumot kiritasizmi (ha/yo'q)")
#     if javob =="yo'q":
#       ishora = False
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()}ning yoshi {yosh} da")


# RO'YXAT ELEMENTLARINI O'CHIRISH

# cars = ['lasseti','nexi','tayota','nexi','aodi','malibu','nexi']
# car = 'aodi'
# while car in cars:
#     cars.remove(car)
# print(cars)


#RO'YXATDAN RO'YXATGA ELEMENT KO'CHIRISH

# talabalar = ['husan','hasan','olim','botir']
# boholangan_talabalar ={}
# while talabalar:
#     talaba = talabalar.pop()
#     baho = input(f"{talaba.title()}ning bahosini kiriting:")
#     print(f"{talaba.title()} baholandi")
#     boholangan_talabalar[talaba] = int(baho)



#AMALIYOT

# print("Mahsulotlar savatchasi:")

# mahsulotlar = []
# n=1
# while True:
#     savol = input(f"{n} - mashulotlaringizni kiriting: ")
#     mahsulotlar.append(savol)
    
#     javob = input("Yana mahsulot kiritasizmi (ha/yo'q)")
#     if javob == 'ha':
#         n+=1
#         continue
       
#     else:
#       break
# print("Sizning savatchadagi mahsulotlaringiz:")
# for savol in mahsulotlar:
#     print (savol.title())



# print("Mahsulotlar savatchasi")

# mahsulotlar = {}
# ishora = True
# while ishora:
#     mahsulot = input("Mahsulotingizni kiriting: ")
#     narh = input(f"{mahsulot.title()} ning narhini kiriting ")
#     mahsulotlar[mahsulot] = int(narh)
    
#     javob = input("Yana boshqa mahsulot tanlaysizmi? (ha/yo'q)")
#     if javob =="yoq":
#        ishora =False
    
# for mahsulot, narh in mahsulotlar.items():
#     print(f"{mahsulot.title()} ning narhi {narh} ga teng")


# buyurtmalar = ['olma','non','nok','cola','qovun']
# mahsulotlar = {
#     'olma':20000,
#     'non':3000,
#     'nok':6000,
#     'cola':10000
#     }

# while buyurtmalar:
#     buyurtma =buyurtmalar.pop()
#     if buyurtma in mahsulotlar.keys():
#         narh = mahsulotlar[buyurtma]
#         print(f"{buyurtma.title()}ning narhi {narh} ga teng")
#     else:
#         print(f"Bizda {buyurtma} mahsuloti yoq")





































