import random
# 1
# def tpl_sort(a):
#     for i in a:
#         if not type(i) == int and not i % 1 == 0:
#             return a
#     return tuple(sorted(a))
# print(tpl_sort((2,5,6,1.2)))

#2
# list1 = [10, 9, 1, 5, 2, 6, 8, 1, 2, 5, 7]
# def sieve(lst):
#     lst = set(lst)
#     print(lst)
#     return tuple(reversed(list(lst)))
# print(sieve(list1))

#3
# def foo(tpl,a):
#     if not a in tpl:
#         return tpl
#     else:
#         k=tpl.index(a)
#         return tuple(list(tpl)[0:k]+list(tpl[k+1:]))
 
 
# print(foo((1,2,3,4,2),2))

#4
# import re
# def checkemail(email):
#     pattern = r"^[a-zA-Z0-9.+-]+@[a-zA-Z0-9-]+.[a-zA-Z0-9-.]+$"
#     print(re.match(pattern, email))
#     return re.match(pattern, email) is not None
# mail = input("введите почту:")


# if checkemail(mail):
#     print("Это почта")
# else:
#     print("Не подходит")


#5
# s = 'ab aa aac aab'
# print(sorted((s.split())))

#6
# def sort_list(lst):
#     for i in lst:
#         number = lst.count(i)
#         if number >3:
#             while i in lst:
#                 lst.remove(i)
#     return(lst)
# print(sort_list([3,2,3,3,2,2,2]))

#7
lst = [4,2,7,1,6,3,5,2,5,25,3,5,6,7,1,2]
def mix_list(lst):
    return random.sample(lst, 5)
print(mix_list(lst))