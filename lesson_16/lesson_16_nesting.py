# -*- coding: utf-8 -*-
"""
Created on Sat Jan 30 09:36:54 2021

@author: VOVO-BRAT
"""

# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }

# car = car0
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()},\
#   {car['rang']} rang,\
#   {car['yil']}-yil, {car['narh']}$")

# cars = [car0,car1,car2]
# for car in cars:
#     print(f"{car['model'].title()}, "\
#           f"{car['rang']}, rang "
#           f"{car['yil']} - yil , narhi {car['narh']}$ ")
  
  
#malibus = [] # Malibu mashinalari uchun bo'sh ro'yxat yaratdik
# for n in range(10):
#     new_car={  # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None,
#         'yil':2020,
#         'narh':None,
#         'km':0,
#         'karobka':'avto'

#         }
  
#     malibus.append(new_car) # yangi lug'atni ro'yxatga qo'shamiz
  
# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'
    
# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'   

# for malibu in malibus[6:]:
#      malibu['rang'] = 'oq'
#      malibu['karobka'] = 'mehanika'
    
# for malibu in malibus:
#    if malibu['karobka'] =='avto':
#        malibu['narh'] = 40000
#    else:
#         malibu['narh'] = 35000
    
#    print(malibus)
  


#LUG'AT ICHIDA RO'YXAT

# devs = {
#         'ali':['Python','C++'],
#         'vali':['Html','css','js'],
#         'hasan':['php','sql'],
#         'husan':['Python','php'],
#         'maryam':['C++','C#']
        
#         }
# for ism,tillar in devs.items():
#     print(f"\n{ism.title()} quiyidagi dasturlash tilarini biladi:", end =' ')
#     for til in tillar:
#         print(f"{til.upper()}", end=' ')

# hamkasblar = {
#     'ali':{'familyasi':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
           
#            },
#      'vali':{'familyasi':'aliyev',
#             'tyil':2001,
#             'malumot':'o\'rta-maxsus',
#             'tillar':['html','css','js']
         
#          },
#      'hasan':{'familyasi':'husanov',
#               'tyil':1999,
#               'malumot':'maxsus',
#               'tillar':['python','php']
              
#          }
    
#     }

# for ism, info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familyasi'].title()},"
#           f"{info['tyil']} - yilda tugulgan."
#           f"Malumoti {info['malumot']}.\n "
#          "Quyidagi dasturlash tillarini biladi:")
#     for til in info['tillar']:
#         print(til.upper())
          

# history0 = {
#     'ism':'abu adulloh',
#     'familya':'ibn ismoil',
#     'tyil':810,
#     'vyil':870,
#     'city':'buhoro',
#     'asarlar':['al-jome as-sahih','al-adab al-mufrad','at-tarix al-kabir','at-tarix as-sagir']
#     } 
# history1 = {
#     'ism':'abdulla',
#     'familya':'qodiriy',
#     'tyil':1894,
#     'vyil':1930,
#     'city':'toshkent',
#     'asarlar':['otkan kunlar','Mehrobdan chayon','obid ketmon']
#     }
# history2 = {
#     'ism':'erkin',
#     'familya':'vohidov',
#     'tyil':1936,
#     'vyil':2016,
#     'city':"fargona",
#     'asarlar':['tongi nafas','qoshiqlarim sizga','ozbegim','qiziquvchan matmusa']
#     }
# history3 = {
#     'ism':'alisher',
#     'familya':'navoi',
#     'tyil':1441,
#     'vyil':1551,
#     'city':"xirota",
#     'asarlar':['xamsa','lison ut-Tayr','mahbub Al-Qulub']
#     }
# persons = [history0,history1,history2,history3]

# for person in persons:
#     ism = person['ism']
#     familya = person['familya']
#     tyil = person['tyil']
#     vyil = person['vyil']
#     city = person['city']
#     print(f"{ism.title()} {familya.title()} "
#           f"{tyil}-yilda , {city} da tavolud topgan"
#           f" {vyil - tyil} yil umr korgan")
    
# for person  in persons:
#     ism = person['ism']
#     familya = person['familya']
#     asarlar = person['asarlar']
#     print(f"\n{ism.title()} {familya.title()} ning mashxur asarlari:" )
#     for person in asarlar:
#      print(person)
    # for asar in persons['asarlar']:
    #     print(asar.title())


# ukam ={
#        'husan':['terminator','Rambo','titanic'],
#        'vali':['tenet','inception','interstellar'],
#        'hasan':['abdulajon','bomba','shaytanat'],
#        'ali':['zombi','king','muvi']
#        }

# for key, ukam in ukam.items():
    
#  print(f"{key.title()} ning sevimli kinolari:")
#  for matn in ukam:
#   print(matn)





# world = {'o\'zbekiston' :
#          {
#     "poytaxt":'toshkent',
#     'hududi':448978,
#     'aholisi':33000000,
#     'pul':"so'm"
#     },
#   'rassiya': 
#     { "poytaxt":"moskva",
#    'hududi':17098246,
#    'aholisi':144000000,
#    'pul':'rubl'
#  },
#   'aqsh':{ 
#       'poytaxt':'washington',
#       'hududi':9631418,
#       'aholisi':327000000,
#       'pul':'dollar'
#       },
#   'Malayziya':{
#       'poytaxt':'kuala-lumpur',
#       'hududi':329750,
#       'aholisi':25000000,
#       'pul':'rinngit'      
#       }  
# }
    
# for davlat , info in world.items():
#     if davlat.lower() == 'aqsh':
#       davlat = davlat.upper()
#     else :
#         davlat = davlat.capitalize()
      
#     print(f"{davlat}ning poytaxti {info['poytaxt'].title()}\n"
#           f"Hududi:{info['hududi']} kv.km\n"
#           f"Aholisi:{info['aholisi']}\n"
#           f"Pul birligi:{info['pul']}\n")
    




world = {'o\'zbekiston' :
          {
    "poytaxt":'toshkent',
    'hududi':448978,
    'aholisi':33000000,
    'pul':"so'm"
    },
  'rassiya': 
    { "poytaxt":"moskva",
    'hududi':17098246,
    'aholisi':144000000,
    'pul':'rubl'
  },
  'aqsh':{ 
      'poytaxt':'washington',
      'hududi':9631418,
      'aholisi':327000000,
      'pul':'dollar'
      },
  'Malayziya':{
      'poytaxt':'kuala-lumpur',
      'hududi':329750,
      'aholisi':25000000,
      'pul':'rinngit'      
      }  
}

davlat = input("Davlat nomini kiriting:>>>").lower()   
if davlat in world:
    info = world[davlat]
    print(f"\n{davlat.capitalize()}ning poytaxti {info['poytaxt'].title()}\n"
          f"Hududi:{info['hududi']} kv.km \n"
          f"Aholosi:{info['aholisi']} \n"
          f"Pul birligi:{info['pul']}\n")
else:
    print("Bunday davlat bizda yoq")

























