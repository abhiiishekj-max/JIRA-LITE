# class Abhishek:
#     def __init__(self,n , d):
#         self.num = n
#         self.den = d

#     def __str__(self):
#        return"{}/{}".format(self.num, self.den)
    
#     def __add__(self,others):
#         tempo_num = self.num * others.den + others.num * self.den
#         tempo_den = self.den * others.den
#         return"{}/{}".format(tempo_num,tempo_den)

#     def __sub__(self,others):
#             tempo_num = self.num * others.den - others.num * self.den
#             tempo_den = self.den * others.den
#             return"{}/{}".format(tempo_num,tempo_den)
#     def __mul__(self,others):
#              tempo_num = self.num *  others.num 
#              tempo_den = self.den * others.den
#              return"{}/{}".format(tempo_num,tempo_den)
#     def __truediv__(self,others):
#                  tempo_num = self.num *  others.den
#                  tempo_den = self.den * others.num
#                  return"{}/{}".format(tempo_num,tempo_den)





# def mera_khud_ka_loop(iterable):

#     iterator = iter(iterable)

#     while True:

#         try:
#             print(next(iterator))
#         except StopIteration:
#             break



# a  =[ 1, 2,]
# b = range(1,20)
# c = (1,2,3)
# d = {1, 2,3}
# e = {1:2,3:4}

# mera_khud_ka_loop(b)



# class mera_range:

#     def __inti__(self,start,end):
#         self.start = start
#         self.end = end

#     def __iter__(self):
#         return mera_range()

# class mera_range:
#     pass
#     def __init__(self,):
#         self.iterable = iterable_obj
#     def __init__(self)
#         return self
#     def __next__(self):
#         pass