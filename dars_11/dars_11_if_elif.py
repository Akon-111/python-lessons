# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 19:42:42 2021

@author: VOVO-BRAT
"""

# yosh = int(input("yoshingiz nechida? "))
# if yosh <=4:
#     print("Sizga kirish bepul.")
# elif yosh <=12:
#     print('Sizga kirish 5000 so\'m.')
# elif yosh <=18:
#     print('Sizga kirish 8000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

# yosh = int(input("Yoshingiz nechida?"))
# if yosh <=4:
#     narh =0
# elif yosh <=12:
#     narh = 5000
# elif yosh <=18:
#     narh = 8000
# else:
#     narh = 1000
# print(f"Sizga kirish {narh} so'm")

  #OR OPERATORI

# kun = input("Bugun nima kun?>>>")
# if kun.lower() =="shanba" or kun.lower() == "yakshanba":
#     print("Bugun dam olish kuni")
# else:
#     print(f"Bugun ish kuni , { kun.title()}")    


# AND OPERATORI

# kun  = input ("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower() == "yakshanba" or kun.lower() == "shanba") and harorat >= 30:
#     print("Cho'milgani ketik")
# elif (kun.lower() == 'yakshanba' or kun.lower() =="shanba") and harorat<30:
#     print("Bugun uyda qolamiz")
# else:
#     print(f"Bugun ish kuni {kun.title()}")    
    
 #BOOLEAN MA'LUMOTLAR TURI
 
# narh = 15000 # mijoz 15000 so'maga taom oladi.
# choy = True # mijoz choy ham oladi.
# salat = 0 # mijoz salat olmaydi.

# if choy and salat:
#     narh +=10000
# elif choy or salat:
#     narh += 5000
# print(f"Jami {narh} so\'m")

####################### SHARTLARNI KETMA-KET TEKSHIRISH ##########
# narh = 15000
# choy = 1
# salat = 0
# non = 1 
# cola = 1
# assorti = 1

# if choy:
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:
#     print("Mijoz non oldi")
#     narh += 2000
# if cola:
#     print ("Mijoz cola oldi.")
#     narh += 8000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narh += 15000
# print(f"Jami{narh} so\'m")
    
###################  RO'YXAT TARKIBINI TEKSHIRISH #########

################### in OPERATORI
# menu = ["osh","sho'rva","lagmon","shashlik","somsa"]
# 'manti' in menu

# menu = ["osh"," shashlik","norin","somsa","sho'rva"]
# ovqat = input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Afsuski bizda bunday ovqat yo\'q")


############################ not in OPERATORI

# menu = ["osh","shashlik","somsa","sho\'rva","norin"]
# "manti" not in menu

# menu = ["osh","shashlik","qozonkobob","norin","somsa"]
# ovqat = input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() not in menu:
#     print("Afususki bizda bunday ovqat yo\'q")
# else:
#     print("Buyurtma qabul qilindi")

#################### IKKI RO'YXATNI SOLISHTIRISH

# menu = ["osh","shashlik","qozonkabob","norin","somsa"]
# buyurtmalar = ["osh", "somsa","manti","shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kexhirasiz,menuda {taom} yo'q")



############################RO'YXAT BO'SH EMASLIGINI TEKSHIRISH

# menu = ["osh","shashlik","qozonkabob","norin","somsa"]
# buyurtmalar = ["osh", "somsa","manti","shashlik"]


# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#    for taom in buyurtmalar:
#        if taom in menu:
#            print(f"Menuda {taom} bor")
#        else:
#             print(f"Kechirasiz,menuda {taom} yo\'q")
# else:       
#     print("Savatchangiz bo\'sh")

############################ AMALIYOT ####################

# juft_son = float(input( "Juft son kiriting"))

# if juft_son%2:
#         print("Bu son juft emas!")
# else:
#         print("Rahmad!")


# yosh = int(input("Yoshingiz nechida?"))
# if yosh<=4 or yosh >60:
#     narh = 0
# elif yosh <=18:
#     narh = 10000
# elif yosh >18 and yosh <60:
#     narh = 20000
# print(f"Sizga muzeyga kirish {narh} so\'m")


# son = int(input("O\'zingiz yoqtirgan soni kiriting?>>>"))
# son1 = int(input("O\'zingiz yoqtirgan yana son kiriting?>>>"))
# if son < son1:
#     print(f"{son} < {son1}")
# if son > son1:
#     print(f"{son} > {son1}")
# if son == son1:
#     print(f"{son} = {son1}")
#     print("siz kiritkan son teng")


# mahsulotlar = ["uzum","anor","shaftoli","nok","olma","xurmo","banan","tarvuz","qovun","o\'rik"]
# savat = []
# # savat.append("olma")
# # savat.append("go\'sh")
# # savat.append("non")
# # savat.append("tarvuz")
# # savat.append("anor")
# for n in range(5):
#     savat.append(input(f"Savatga {n+1} mahsulotni qo'shing:"))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do\'konimizda {mahsulot} bor")
#     else:
#         print(f"Do\'konimizda{mahsulot} yo'q")


mahsulotlar = ["non","olma","tarvuz","nok","qurt","novot"]
savat = []
for n in range(5):
    savat.append(input(f"Savatga {n+1} mahsulotni qo'shing>>>"))
    
mavjud_emas = []
bor_mahsulotlar =[]
 
for mahsulot in savat:                  
    if mahsulot in mahsulotlar:
        bor_mahsulotlar.append(mahsulot)
    else :
      mavjud_emas.append(mahsulot)
if mavjud_emas:
    print(f"Dokonimizda quyidagi mahsulotlar yoq:")
    for mahsulot in mavjud_emas:
        print(mahsulot)
    else:
        print("Siz so'ragan barcha ahsulotlar bor")


# foydalanuvchilar = ["ali","Malik","anvar","umar","olim"]
# login = input ("Yangi login tanlang>>>:")

# if login in foydalanuvchilar:
#     print("Bu login band boshqa login kiritin!")
# else:
#     print("Xush kelibsiz!")

# son = int(input("Istalgan butun soni kiriting>>>:"))
# for k in range(2,11):
#     if not (son%k):
#         print(f"{son} soni {k} ga qoldiqsiz bo'linadi")














































    
    
    
    
    
    
    
    
    
    
    
    
    
    