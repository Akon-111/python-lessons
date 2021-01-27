# -*- coding: utf-8 -*-
"""
Created on Mon Jan 25 19:27:36 2021

@author: VOVO-BRAT
"""
#.items() METODI

# talaba_0 = {
#     'ism':'alijon',
#     'familya':'shamsiyev',
#     'yosh':22,
#     'fakultet':'matematika',
#     'kurs':4
#     }
# #print(talaba_0.items())

# for kalit, qiymat in talaba_0.items():
#     print(f"Kalit:{kalit}")
#     print(f"Qiymat:{qiymat} \n")




# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k,q in telefonlar.items():
#     print(f"{k.title()} ning telefoni {q}")


# mahsulotlar = {
#     'olma':10000,
#     'anor':20000,
#     'uzum':40000,
#     'anjir':23000,
#     'shaftoli':30000
    
#     }
# #print(mahsulotlar.keys())

# print("Do\'kondagi mahsulotlar")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())


# bozorlik = ['anor','uzum','non','baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#      print(f"{mahsulot.title()} {mahsulotlar[mahsulot]}")
     
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, dokonizga {buyum.upper()} ham olib keling")
#Yuqordagi kodga e'tibor bering. Biz avval borolik degan ro'yxat yaratdik (uyga bozor qilyapmiz), keyin esa mahsulotlar lug'atidagi har bir mahsulotni bizdagi bozorlik ro'yxati bilan solishtirdik. Agar mahsulot bizning bozorlik ro'yxatimizda bo'lsa, uning narhini konsolga chiqardik.

#LUG'AT ELEMENTLARINI TARTIB BILAN CHIQARISH
# print("Do'konimizdegi mahsulotlar")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())


#print(telefonlar.values())
# print(f"Foydalanuvchilar quyidagi telefonlarni ishlatishadi")
# for tel in telefonlar.values():
#     print(tel)




# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'noki 3310',
#     'hamid':'galaxy s9',
#     'mayram':'huawei p30',
#     'tohir':'iphone x',
#     'umar':'iphone x'
    
#     }
# print("Foydalanuvchilar quyidagi telefonlarni ishlatishadi")
# for tel in set(telefonlar.values()):
#     print(tel)


     #AMALIYOT
# python = {
#     'boolean':'mantiqi qiymat',
#     'float':"o'nlik son",
#     "for":'biror amlni qayta-qayta bajarish sikili',
#     'if':'shartlarni tekwirish operatori',
#     'integer': 'butun son',
#     'tuple':"o'zgarmas son",
#     'sorted':'malumotni tartiblash alibo boyicha',
#     'print':'malumotni ekranga chiqarish'
#     }


# for matn, text in sorted(python.items()):
#     print(f"{matn.title()} - {text}")


# world = {
#     'aqsh':'washington',
#     'italiya':'rim',
#     'malayziya':'kuala-lumpur',
#     'o\'zbekiston':'toshkent',
#     'qirgiziston':'bishkek',
#     'qozogiston':'nursulton',
#     'rossiya':'moskva',
#     'singapur':'singapur',
#     'tojikiston':'dushanbe'
#     }


# # print("Dunyo davlatlari:")
# # for dav in sorted(world.keys()):
# #     print(dav.upper())


# # print("davlatlar poytaxti:")
# # for poy in sorted(world.values()):
# #     print(poy)
    
# savol = input("Qaysi davlatning poytaxtini bilishi hohlaysiz>>>")
    
# #for salov,text in world.items():
# if savol in world.items():
#       print(f"{savol} ning poytaxti {text} shahri")    





# world = {
#     'aqsh':'washington',
#     'italiya':'rim',
#     'malayziya':'kuala-lumpur',
#     'o\'zbekistin':"toshkent",
#     'qirgiziston':'bishkek',
#     'qozogiston':'nursulton',
#     'rossiya':'maskva',
#     'singapur':'singapur',
#     'tojikiston':'dushanbe',
#     'brazilya':'brazilya'
#     }
# print("Dunyo davlatlari:")
# for davlat in sorted(world.keys()):
#     print (davlat.upper())
    
    
# print(" Davlatlar poytaxti:")
# for poytaxt in world.values():
#     print(poytaxt.title())

# davlat = input("Qaysi davlatning poytaxtini bilishni xoxlaysiz?>>>").lower()
# poytaxt = world.get(davlat)
# if poytaxt == None:
#     print("Kechirasiz bu boyicha bizda malumot yoq")
# else:
#     print(f"{davlat.upper()} ning poytaxti {poytaxt.title()} shahri")



# menu = {
        
#         'osh':15000,
#         'lagmon':18000,
#         'shashlik':20000,
#         'shorva':12000,
#         'manti':19000,
#         'lavash':21000,
#         'tuxum barak':12000,
#         'bishteks':25000,
#         'asarti':30000
        
#         }
# print("O'zingiz yoqtirgan 3 ta taom buyurtma bering")
# buyurtma =[]
# for n in range(3):
#   buyurtma.append(input(f" {n+1} - taom:"))
  
# for zakas in buyurtma:
#     if zakas in menu:
#         print(f"Siz buyurtirgan taom {zakas.title()} {menu[zakas]} so'm")
#     else:
#         print(f"Kechirasiz bizda bunday {zakas.upper()} taom yoq")




























