# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 11:56:44 2021

@author: VOVO-BRAT
"""

# RO'YXATNI TARTIBLASH

#Aksar holatlarda ro'yxat ichidagi elementlarni alifbo ketma-ketligida tartiblash talab qilinishi mumkin. Buning uchun list uchun maxsus .sort() metodidan foydalanamiz.

# cars = ["bmw","mercedes benz","general motors","tesla","audi"]
# cars.sort()
# print(cars)

#Ro'yxatni teskari tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritamiz. 
# cars = ["bmw","mercedes benz","general motors","tesla","audi"]
# cars.sort(reverse=True)
# print(cars)

# Ba'zida asl ro'yxat ichidagi elementlarning ketma-ketligini buzmagan holda ro'yxatni tartiblash talab qilinishi mumkin. Buning uchun sorted() funktsiyasidan foydalanamiz:
#mehmonlar = ['Odil',"Hamid","Temur","Avazbek","Farruh","Shamsiddin"]
# print("sorted() qaytargan ro'yxat :",sorted(mehmonlar))
# print("Asl ro'yxat o'zgarmas qoldi:",mehmonlar)

#sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz:
#print(sorted(mehmonlar,reverse=True))

#Yuoqridagi ikki usul bilan sonli ro'yxatlarni ham tartiblashimiz mumkin:

# ages = [12,13,19,45,226,-36,-7]
# ages.sort()
# print(ages)
# print(sorted(ages,reverse= True))

#RO'YXATNI AYLANTIRISH

# fruits = ["pear","banana","apple","watermelon","lemon"]
# fruits.reverse()
# print(fruits)

# fruits = ["pear","banana","apple","watermelon","lemon"]
# print("ELementlar soni:",len(fruits))

# range() FUNKTSIYASI
# sonlar = list(range(0,10))
# print(sonlar)

# juft_sonlar = list(range(0,20,2)) # 0 dan 20 gacha 2 qadam bilan
# toq_sonlar = list(range(1,20,2))# 1 dan 20 gacha 2 qadam bilan
# print("Juft sonlar:",juft_sonlar)
# print("TOq_sonlar",toq_sonlar)

# SONLI RO'YXAT USTIDA SODDA AMALLAR
# narxlar = [1200,1300,2000,1000,700]
# arzon = min(narxlar)
# qimmat = max(narxlar)
# jami = sum(narxlar)
# print("Eng arzon narh",arzon, " Eng qimmati",qimmat , " Jami",jami)


#cars = ["bmw","mercedes benz","volvo","general motors","tesla","audi"]
#my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
#print(my_cars)

#print(cars[2:5])  # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
# print(cars[:4])
# print(cars[2:])


# sonlar = [1,2,3,4,5]
# sonlar2 = sonlar
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ro'yxati:", sonlar)
# print("BU sonlar2 ro'yxati:", sonlar2)

#RO'YXATDAN NUSXA OLISH

# sonlar = [1,2,3,4,5,6]# sonlar degan ro'yxat yaratamiz
# sonlar2 = sonlar [:] # [:] ro'yxatni to'liq ko'chirib oladi
# sonlar2.append(6)
# sonlar2.append(7)
# print("Bu sonlar ro'yxati:",sonlar)
# print("Bu sonlar2 ro'yxati:",sonlar2)

# TUPLES - O'ZGARMAS RO'YXAT

# tomonlar = (20,30,55.2)
# print(tomonlar)

# toys = ("bus","car","bear","dino","snake","lizard")
# print(toys[0])
# print(toys[-1])
# print(toys[2:5])

# Keling Tuple ichidagi biror elementning qiymatini o'zgartirib ko'ramiz:
    
# toys = ("bus","car","bear","dino","snake","lizard") # o'zgarmas ro'yxat
# toys = list(toys)# o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
# # Ro'yxatga o'zgartirishlar kiritamiz
# toys.append("cat")
# toys.append("watch")
# toys[1] = "mcqueen"
# toys = tuple(toys)# Ro'yxatni qaytadan o'zgarmas ro'yxatga (Tuple) aylantiramiz
# print(toys)


#davlatlar_nomi = ["USA","Brazilya","Italya","Rim","Rassiya","Angilya"]
#print(len(davlatlar_nomi)) #Ro'yxatning uzunligini konsolga chiqaring
#print(sorted(davlatlar_nomi)) #sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
#print(sorted(davlatlar_nomi, reverse=True))#sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
#davlatlar_nomi.reverse() #everse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
#davlatlar_nomi.sort(reverse=True) #sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
#print(davlatlar_nomi)

#juft_sonlar = list(range(120,1200,2))# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing

#print(sum(juft_sonlar)) #Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
#print(max(juft_sonlar) - min(juft_sonlar)) #Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
#print(len(juft_sonlar)) #Ro'yxatdagi elementlar sonini hisoblang
#print("Boshidagi 20 ta sonlar:", juft_sonlar[:20],"O'rtasidagi 20 ta sonlar:",juft_sonlar[220:240],"Oxiridagi 20 ta sonlar:",juft_sonlar[520:]) #Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring

# taomlar = ["manti","shorva","osh","shashlik","Baliq"]
# nonushta = taomlar[:]
# nonushta.append("tuxum")
# nonushta.append("Pishloq")
# nonushta = tuple(nonushta)
# nonushta[1] = "lagmon"
# print(taomlar)
# print(nonushta)






















































































