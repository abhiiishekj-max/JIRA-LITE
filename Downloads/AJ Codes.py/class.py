# a= ([[[(10, 20, 'hai'),'hello' ,'python'],(2,3),6], {3,40, 56,'hai'}, ['language' , 'is'],'good'],30,40,200)


# print(a[0:3:2])

# import random
# random.randint(100,300)
# jacpot = random.randint(100,300)
# guess =int(input('guess the number'))
# while guess != jacpot:
#     if guess<jacpot:
#         print('too low')
#     else:
#         print('too high')
#     guess = int(input('guess the number'))
#     print('sahi jawb')



# def return_sum(func, L):

#     result= 0

#     for i in L:

#         if func(i):
#             result = result + i
#     return result

# L=[111, 14, 21, 23,56,78,45, 29, 28]

# x = lambda x:x%2 == 0
# y = lambda x:x%2 != 0
# z = lambda x :x%3 ==0

# print(return_sum(x, L))
# print(return_sum(y,L))
# print(return_sum(z,L))






# class Atm:
#     def __init__(self):
#         self.pin = ""
#         self.balance = 0

#         self.menu()

#     def menu(self):
#          user_input =  input("""
#         hello welcome how would u like to proceed ?
#         1. enter 1 to create pin
#         2. enter 2 to deposit
#         3. enter 3 to withdraw
#         4. enter 4 to check balance 
#         5 . enter to exit
#         """)
#     if user_input == '1':
#         print("create pin")
#     elif user_input == '2':
#         print("deposit")
#     elif user_input == '3':
#         print("withdraw")
#     elif user_input == '4':
#         print("check balance")
#     else:
#         print ("exit")
   



# import random
# random.randint(100,200)


# jackpot= random.randint(100,200)
# guess = int(input("guess a number"))
# counter = 1

# while guess!= jackpot:
#     if guess<jackpot:
#         print("too low")

# else:
#     print("sahi jawab")
#     print= int(input("guess a number"))
#     counter+=1
#     print("sahi jawab")
#     print("you took", counter , "guess")
        



# import random
# random.randint(100,500)

# jackpot = random.randint(100,500)
# counter  = 1

# guess = int(input("number guess kar"))
# while guess!= jackpot:
#     if guess<jackpot:
#         print("too low")
#     else:
#         print("too high")
#     guess = int(input("number guess kar"))
    
#     counter = counter + 1
#     print("sahi jawab")
#     print("you took", counter,"guesses")




# from fraction import Fraction
# x = Fraction(4,5)
# print(x)


# from abhishek import Abhishek
# x = Abhishek(4,5)
# y = Abhishek(5,6)
# print(type(x)) 
# print(x+y)
# print(x-y)
# print(x/y)
# print(x*y)




# def change(L):
#     print(id(L))
#     L.append(5)
#     print(id(L))

# L1 = [1,2,3,4,]
# print(id(L1))
# print(L1)

# change(L1)

# print(L1)


# class costumer:

#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# c1 = costumer("abhishek",23)
# c2 = costumer("abhi",34)
# c3 = costumer("hero",45)

# L = [c1,c2,c3]

# for i in L:
#     print(i.name,i.age)

# abhishek import abhishek





# a = 1 
# b = True + False
# print(a is b)

# a = {1,3,5}

# b = {1,3,5}

# print(a is b)

# a,b = (1,),(1,)
# print(a is b)

# print('abhi' is 'abhi')



# print( 0 is False )

# print(0 is 0)



# a = 1000
# b = 1000

# print( id(a) , id (b))
# print(a is b)



# class customer:
#     def __init__(self, name, gender, address):
#         self.name = name
#         self.gender = gender
#         self.address = address

#     def edit_profile(self, new_name=None, new_city=None, new_pin=None, new_state=None):
#         if new_name is not None:
#             self.name = new_name
#         if new_city is not None and new_pin is not None and new_state is not None:
#             self.address.change_address(new_city, new_pin, new_state)


# class address:
#     def __init__(self, city, pincode, state):
#         self.city = city
#         self.pincode = pincode
#         self.state = state

#     def change_address(self, new_city, new_pin, new_state):
#         self.city = new_city
#         self.pincode = new_pin
#         self.state = new_state


# add = address("mumbai", 401101, "mah")
# cust = customer("abhishek", "male", add)

# cust.edit_profile("abhishek", "pune", 411001, "mh")
# print(cust.address.pincode)




# class user:

#     def login(self):
#         print("login")

#     def register(self):
#         print("register")

# class student(user):

#     def enroll(self):
#         print("enroll")

#     def review(self):
#         print("review")


# stu1 = student()
# stu1.enroll()
# stu1.review()
# stu1.login()
# stu1.register()




# class phone:
#     def __init__(self,price,brand,camera):

#         print("inside phone constructor")
#         self.__price = price
#         self.brand = brand
#         self.camera = camera

#     def buy(self):
#         print("buying a phone")
# #method overriding

# class smartphone(phone):
#     print("buying a smartphone")

# s= smartphone(20000, 'apple', 13)

# s.buy()



# a = 3000
# b = 3000

# print(a is b)
# print(id (a), id (b))



# class Geometry:
#     def area(self, radius):
#         return 3.14* radius * radius

#     def area(self,I ,b):
#         return I*b

# obj = Geometry()
# print(obj.area(4))






#project

# import json
# from urllib.error import URLError
# from urllib.request import urlopen


# class IRCTC:
#     def __init__(self):
#         user_input = input(
#             "How would you like to proceed?\n"
#             "1. Check live train status\n"
#             "2. Check PNR\n"
#             "3. Check train schedule\n"
#         ).strip()

#         if user_input == "1":
#             print("Live status lookup is not implemented yet.")
#         elif user_input == "2":
#             print("PNR lookup is not implemented yet.")
#         elif user_input == "3":
#             self.train_schedule()
#         else:
#             print("Invalid option.")

#     def train_schedule(self):
#         train_no = input("Enter the train number: ").strip()
#         if not train_no:
#             print("Train number cannot be empty.")
#             return
#         self.fetch_data(train_no)

#     def fetch_data(self, train_no):
#         url = "https://api.example.com/trains/{train_no}/schedule"
#         try:
#             with urlopen(url, timeout=10) as response:
#                 data = json.loads(response.read().decode("utf-8"))
#             print(data)
#         except (URLError, TimeoutError, ValueError) as error:
#             print("Unable to fetch train schedule: {error}")

# obj = IRCTC()



# temp = float (input("enter temperature in celcius"))
# fehrenheit = (temp * 1.8 +32)
# print(fehrenheit)


# alpha = str(input("enter a alpha"))
# alpha = ord(alpha)
# upper_case = ord(alpha) + 36
# print(upper_case)

# class upper_case:

#     def __str__(self):
#        return"chr(ord)".format("")

# from time import sleep, time
# import threading

# start_time = time()

# def something(id):

#     print("going to sleep . .{id} ")
#     sleep(1)
#     print(" woken up....{id}")

# t1 = threading.Thread(target = something,args=[0])
# t1.start()
# # for _ in range(10):
# #     something()
# t1.join()
# end_time = time()

# print("main thread ended in {end_time-start_time] seconds ")




# L = [ x for x in range(1,10000)]

# # for i in L:
# #     print( i*2)

# import sys
# print(sys.getsizeof(L)/1024)


# value1 = int(input("enter a value"))
# value2 = int(input("enter a value"))
# value3 = int(input("enter a value"))

# print("sum =",value1+value2+value3)


# num = int(input("enter a number"))
# reverse = num[::-1]

# print("reverse =", reverse)
# print("same as original",reverse == num)


# num = int(input("Enter a number: "))
# original = num
# reverse = 0

# while num > 0:
#     reverse = reverse * 10 + num % 10   # take last digit, add to reverse
    # num //= 10                          # remove last digit

# print("Reverse =", reverse)
# print("Same as original?", reverse == original)



# year = int(input("enter a year"))
# if year % 4 == 0:
#     print("it leap year")
# else:
#     print("its not")


# import math

# class point:
#     def __init__(self,x ,y):
#         self.x = x 
#         self.y = y
#     def distance_to(self,others):
#         return  math.sqrt((others.x - self.x)**2+(others.y - self.y)**2)

# a = point(2,5)
# b = point(4 ,6)
# print(a.distance_to(b))


# a= float(input("enter first angle"))
# b= float(input("enter second angle"))
# c= float(input("enter third angle"))

# if a >0 and b >0 and c>0 and a + b + c == 180:
#     print("this can form a triangle")
# else:
#     print("this cannot form a triangle")



# cost = int(input("enter a cost"))

# selling = int(input("enter a selling"))
# if cost> selling:
#     print("loss")
# else:
#     print("profit")

# P = float(input("enter principle amount"))
# R = float(input("enter rate of interest"))
# N = float(input("enter time period"))

# print( P * R * N /100 )



# import math

# r = float(input("enter a radius"))
# h = float(input("enter a height"))


# volume = math.pi * r**2 * h
# cost = volume / 1000
# litre = cost * 40

# # print("volume in" 'cm')
# # print("cost of milk")
# # print("litre of milk")

# print("Volume =", round(volume,2), "cm³")

# print("Cost of milk = Rs", round(cost,2))
# print("Volume in litres =", round(litre,2), "L")




# from abc import ABC,abstractmethod

# class bankapp(ABC):

#     def database(self):
#         print("connected to database")

#     @abstractmethod
#     def  security(self):
#         pass


# class mobileapp(bankapp):
#     def mobile_login(self):
#         print("login into mobile")

#     def security(self):
#         print("mobile security")


# mob = mobileapp()
# mob.database()




class pizza:
    def prepare(self):
        raise NotImplementedError("this method be overwritten by subclasses")


class cheesepizza(pizza):
    def prepare(self):
        return "preparing cheese pizza"

class pepperonipizza(pizza):
    def prepare(self):
        return "preparing pepperoni pizza"

class veggiepizza(pizza):
    def prepare(self):
        return "preparing veggie pizza"

#factory class
class pizzafactory:
    @staticmethod
    def create_pizza(pizza_type):
        if pizza_type == "cheese":
            return cheesepizza()
        elif pizza_type == "pepperoni":
            return pepperonipizza()
        elif pizza_type == "veggie":
            return veggiepizza()


def main():
    try:
        user_input = "pepperoni"
        pizza = pizzafactory.create_pizza(user_input)
        print(pizza.prepare())
    except ValueError as e:
        print(e)
    