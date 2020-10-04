# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 09:54:28 2020

@author: Mehmet Eyüpoğlu
"""

# def f( x ):
#     x = x + 1
#     print('in f(x): x =', x)
#     return x
# x = 3
# z = f( x )

# def f(y):
#     x = 1
#     x += 1
#     print(y)
# x = 5
# f(x)
# print(x)

# def g(y):
#     print(x)
#     print(x + 1)
# x = 5
# g(x)
# print(x)
# def h(y):
#     x += 1
# x = 5
# h(x)
# print(x)

# def quotient_and_remainder(x, y):
#     q = x // y
#     r = x % y
#     return (q, r)
# (quot, rem) = quotient_and_remainder(4,5)
# print((quot, rem))

# (x, y) = (4, rem)
# print((x, y))

# def get_data(aTuple):
#     nums = ()
#     words = ()
#     for t in aTuple:
#         nums = nums + (t[0],)
#         if t[1] not in words:
#             words = words + (t[1],)
#     min_n = min(nums)
#     max_n = max(nums)
#     unique_words = len(words)
#     return (min_n, max_n, unique_words)

# print(get_data(((3,4),(5,6),(7,8))))

# Computing the sum of elements

l = [1,2,3,4,5]

# def sum_list(a_list): 
#     sum_list = 0
#     for i in a_list: 
#         sum_list += i
#     return sum_list

# a = sum_list(l)
# print(a)

L = []

l.extend([0,6])

print(l)

l.remove(3)
print(l)
