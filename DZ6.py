# Задача: предложить улучшения кода для уже решённых задач (3-5 задача):
# С помощью использования **лямбд, filter, map, zip, enumerate, list comprehension

# from random import randint
# import math

# def Get_coordinates(num_plan, left, right):     
#     return tuple([randint(left, right) for i in range(num_plan)])

# def Find_dist(a, b):    
#     return round(math.sqrt(sum((x - y)**2 for x, y in zip(a, b))), 3)

# num_plan = 3    
# left = -10
# right = 10

# point_A = Get_coordinates(num_plan, left, right)
# point_B = Get_coordinates(num_plan,left, right)

# print(f'A {point_A}, B {point_B}')
# print (f'Расстояние между точками: {Find_dist(point_A, point_B)}')

# from random import randint
# import itertools

# k = 5

# ratios = [randint(0, 10) for i in range (k + 1)]
# while ratios[0] == 0:
#     ratios[0] = randint(1, 10) 

# ratios = [1, 8, 2, 0, 5]



# n = [n for n in range(k, -1, -1)] 
# pol = list(zip(ratios, n))

# print (n)
# print(pol)

# from functools import reduce

# d = [1, 2, 3, 4, 5]

# pr = reduce(lambda x, y: x*y, d)
# print (pr)
