# -*- coding: utf-8 -*-
"""
Created on Thu Jan 14 14:40:51 2021

@author: VOVO-BRAT
"""
#List quyidagicha yaratiladi:
    
# mevalar = ['olma','anjir','shaftoli',"o'rik"] # mevalar ro'yxati (matnlar)
#narhlar = [1200,1800,1090,2200]#narhlar ro'yxati (sonlar)
# sonlar = ['bir','ikki',3,4,5] #sonlar va matnlar aralash ro'yxat
# ismlar = [] #bo'sh ro'yhat
# print(mevalar, narhlar, sonlar)

#LIST ELEMENTLARI

# mevalar = ['olma','anjir','shaftoli',"o'rik"]#mevalar ro'yxati (matnlar)
# print("Birinchi meva:",mevalar[0].title())
# print("Ikkinchi meva:",mevalar[1].upper())

#print(narhlar[2] + narhlar[3])

#Yangi element qo'shish

# mevalar = ['olma','anjir','shaftoli',"o'rik"]
# mevalar.append("tarvuz") # mevalar ga tarvuz qo'shamiz
# print(mevalar)

# cars = []
# cars.append('Lacetti')
# cars.append('Nexia 3')
# cars.append('Cobalt')
# print(cars)

#.insert() metodi

# cars = ['Lacetti','Nexia 3','Cobalt']
# cars.insert(0,'Malibu')
# cars.insert(2,'Damas')
# print(cars)

#Elementni o'chirish

# mevalar = ['olma','anjir','shaftoli',"o'rik",'anor']
# del mevalar[1]# 2-element (anjir) ni o'chirib tashlaymiz
# print(mevalar)

# mevalar = ['Olma','anjir','shaftoli',"o'rik",'anor']
# mevalar.remove('shaftoli')# Ro'yxatdan shaftolini o'chirdik
# print(mevalar)


#Elementni sug'urib olish
# Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.
# bozorlik= ["yog'",'un','piyoz','banan',"go'sht"]
# mahsulot = bozorlik.pop(3)# Ro'yxatdan banan ni sug'urib olamiz
# print("Men " + mahsulot + " sotib oldim")
# print("olinmagan mahsulotlar:",bozorlik)

# ismlar = ["Abror","Rustam","Zohid"]
# print("SAlom",ismlar[0],"bugun choyxona bormi?",ismlar[1],"choyxonaga boramizmi?","Bugun choyxona", ismlar[2])

# sonlar = [10,-20,31.6,200,300,12,-4,36.7]

# sonlar[0] = 300
# sonlar[4] = sonlar[2] + 120
# sonlar[3] = 10
# sonlar[6] = sonlar[1] - 15
# sonlar[7] = sonlar [2]*2
# print (sonlar)

# t_shaxslar = [ "Amir Temur","Alisher Navoi","Imom Buhoriy"]
# z_shaxslar = ["Stiv Jobs","Bill Gates","Ilon Mask"]
# print("Men tarixiy Shaxslardan ",t_shaxslar.pop(2),"zamonaviy shaxslardan esa ",z_shaxslar.pop(1), "bilan suhbat qilishni istar edim!")



# friend = []
# friend.append("Ali")
# friend.append("Johon")
# friend.append("Zokir")
# #friend.remove("Zokir")
# friend.insert(0,"Toyir")
# friend.insert(5,"Marat")
# print("Mexmonga kelganlar",friend.pop(0),"Kelmaganlar",friend)







