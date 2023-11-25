import random
# 1
# def tpl_sort(a):
#     for i in a:
#         if not type(i) == int and not i % 1 == 0:
#             return a
#             break
#     return tuple(sorted(a))
# print(tpl_sort((2,5,6,1.2.5)))

#2
# def sieve(lst):
#     return tuple(reversed(list(set(lst))))
# lst = list(input())
# print(sieve(lst))

#3
# def foo(tpl,a):
#     if not a in tpl:
#         return tpl
#     else:
#         k=tpl.index(a)
#         return tuple(list(tpl)[0:k]+list(tpl[k+1:]))
 
 
# print(foo((1,2,3,4,2),2))

#4


#5
# s = 'string integer list dictionary tuple'
# print(sorted(list(s.split())))

#6
# def sort_list(lst):
#     for i in lst:
#         number = lst.count(i)
#         if number >3:
#             while i in lst:
#                 lst.remove(i)
#     return(lst)
# print(sort_list([3,2,3,3,2,2]))

#7
# lst = [4,2,7,1,6,3,5,2,5,25,3,5,6,7,1,2]
# def mix_list(lst):
#     return random.sample(lst, len(lst))
# print(mix_list(lst))