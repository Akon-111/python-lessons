# -*- coding: utf-8 -*-
"""
Created on Fri Feb  5 09:00:32 2021

@author: VOVO-BRAT
"""

# ism = input("Ismingiz nima>>>")
# print(f"Salom, {ism.title()}")

# ism = input("Ismingiz nima>>>")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh)
# height = input("Boyingiz necha metr>>")
# height =float(height)

# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan.
#     print(son,end =' ')# son ni konsolga chiqaramiz,
#     son += 1 # songa 1 qo'shamiz.

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting"
# savol += "(dasturni to\'xtatish uchun 'exit' deb yozing):"
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat != 'exit':
#         print(float(qiymat)**2)
# print("Dastur tugadi")

# Ishora (flag)

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur")
# savol = "Istalgan son kiriting"
# savol += "(dasturni to\'xtatish uchun 'exit' deb yozing):"

# ishora =True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora =False
#     else:
#         print(float(qiymat)**2)
# print("Dastur tugadi")

#    BREAK OPERATORI
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol ="Istalgan son kiriting"
# savol +="(dasturni to\'xtatish uchun 'exit' deb yozing):"

# while True: #abadiy tsikl
#   qiymat = input(savol)
#   if qiymat == 'exit':
#       break #tsiklni to'xtatish
#   else:
#       print(float(qiymat)**2)
# print("Dastur tugadi")



# sonlar = list(range (1,11))
# for son in sonlar:
#     if son ==5:
#         break
#     print(f"{son} ning kvadrati {son**2} ga teng")


#CONTINUE OPERATORI

# sonlar = list(range(1,11))
# for son in sonlar:
#     if son ==5:
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
#     son +=1
#     if son % 2 != 0:
#         continue
#     else:
#         print(son)


#ABADIY TSIKL TUZOG'I
# son= 0
# while son< 10:
#     if son%2 !=0:
#         continue
#     else:
#         print(son)

# son = 0
# while son<10:
#     if son%2 != 0:
#         continue
#     else:
#         print(son)
#     son +=1


# son =1
# while son>0:
#     son +=1
#     if son%2 !=0:
#         continue
#     else:
#         print(son)


#AMALIYOT
# print("O'zingiz yoqtirgan kitoblarni kiriting>>>")
# kitob = 'Eng yaxshi korgan kitobingizni yozing'
# kitob +="(dasturni toxtatish uchun 'stop' deb yozing):"
# qiymat = ''
# while qiymat != 'stop':
#     qiymat= input(kitob)
#     if qiymat == 'stop':
#         print("dastur tugadi")
   
# print("O'zingiz yoqtirgan kitoblarni kiriting>>>")
# kitob = 'Eng yaxshi korgan kitobingizni yozing'
# kitob +="(dasturni toxtatish uchun 'stop' deb yozing):"

# qiymat = True
# while qiymat:
#     qiymat = input(kitob)
#     if qiymat == "stop":
#         qiymat= False
#     print("dastur tugadi")


# print("O'zingiz yoqtirgan kitoblarni kiriting>>>")
# kitob = 'Eng yaxshi korgan kitobingizni yozing'
# kitob +="(dasturni toxtatish uchun 'stop' deb yozing):"


# while True:
#     qiymat = input(kitob)
#     if qiymat == 'stop':
#         break
# print("Dastur tugadi")

# print("Muzeyga kirish uchun chiptalar narxi")
# yosh = 'Yoshingizni kiriting'
# yosh += "(dasturni toxtatish uchun 'exit' yoki 'quit' deb yozing):"

# while True:
#     qiymat =input(yosh)
  
#     if qiymat == 'exit' or qiymat=='quit':
#         break
#     age = int(qiymat)
    
#     if age <=7:
#          narh= 2000
#     elif age >7 and age <18:
#          narh = 10000
#     elif age >19 and age <65:
#          narh = 8000
#     else: narh=0
         
#     if narh ==0:
#         print("SIzga chipta bepul")
#     else:
#       print(f"sizning yoshingiz {qiymat} da sizga bilet narxi {narh} so'm")
# print("Dastur tugadi")


# savol ="Kiritilgan sonning ildisizni qaytaruvchi dastur.\n"
# savol+="Musbat son kiriting "
# savol+="(dastur toxtatish uchun 'exit' deb yozing):"

# while True:
#     qiymat =input(savol)
#     if qiymat == 'exit':
#         break
#     elif float(qiymat) <0:
#         continue
#     else:
#         ildiz = float(qiymat)**(1/2)
#         print(f"{qiymat} ningildizi {ildiz} ga teng")
# print("Dastur tugadi")

