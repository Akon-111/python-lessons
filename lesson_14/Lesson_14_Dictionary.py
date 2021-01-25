# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 12:47:59 2021

@author: VOVO-BRAT
"""

# car_0 = {"modeli":"ferrari" ,"rangi":"qizil"}
# print(car_0['rangi'])

#talaba_0 = {"ism":"murod olimov","yosh":20,"t_yil":2000}
# print(f"{talaba_0['ism'].title()},\
#       {talaba_0['t_yil']}- yilda tug'ilgan,\
#           {talaba_0['yosh']} yoshda")
# talaba_0["kurs"] = 4
# talaba_0['fakultet'] = "infarmatika"
# print(talaba_0)

# talaba_1 ={}
# talaba_1["ism"] = 'qobil rasulov'
# talaba_1["kurs"] = 3
# talaba_1["yosh"] = 20
# del talaba_1['yosh']
# talaba_1["kurs"] = 4
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")



# telefonlar = {
#     "ali":"iphone X",
#     "vali":"galaxy s9",
#     "olim":"mi 10 pro",
#     "orif":"nokia 3310"
#     }
# #print(telefonlar)

# #get() METODI

# # phone = telefonlar['hasan']
# # print(f"Alining telefoni {phone}")

# # phone = telefonlar.get("hasan","Bundayn ism mavjud emas")
# # print(phone)

# phone = telefonlar.get("hasan")
# print(phone)

#AMALIYOT

# otam = {"ism":"Bahrom","t_yil":1972,"city":"Toshkent"}
# print(f"Otamning ismi {otam['ism']},\
#        {otam['t_yil']}- yilda,\
#            {otam['city']} da tug'ilgan")

# onam = {"ism":"Xilola","t_yil":1976,"city":"Toshkent"}
# print(f"Onamning ismi {onam['ism']},\
#       {onam['t_yil']} -yilda,\
#           {onam['city']} da tug'ulgan")
         

# family = {
#     "ukam":"Ali","taom1":"osh",
#     "dostim":"Sarik","taom":"manti"}
# print(f"{family['ukam']},ning sevimli taommi {family['taom1']},\
#       {family['dostim']}, ning sevimli taomi {family['taom']}")

dictionari = {
    "integer":"butun son",
    "flaot":"o'nlik son",
    "string":"matin",
    "if":"agar",
    "else":"aks xolda"
    }

#lugat = dictionari.get("tuple","Bunday soz mavjud emas")
# soz = input("birorta soz kiriting>>>").lower()
# print(dictionari.get(soz,"bunday son mavjud emas"))

kalit = input("kalit soz kiriting>>>").lower()
tarjima = dictionari.get(kalit)
if tarjima == None:
    print("bunday son mavjud emas")
else:
    print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    

































