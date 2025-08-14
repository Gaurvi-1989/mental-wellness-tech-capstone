#question 1
# import math_operations 
# a=int(input('enter first number'))
# b=int(input('enter second number'))
# print(f'numbers are {a} and {b}')
# print('addition=', math_operations.add(a,b))
# print('subtraction=', math_operations.sub(a,b))
# print('multiplication=', math_operations.mul(a,b))
# print('division=', math_operations.div(a,b))

# def maxs_app(numbers) :
#     dict = {}
#     for num in numbers:
#         dict[num] = dict.get(num, 0) + 1
#     print(dict)
#     return max(dict, key=dict.get)

# l=[1,2,3,3,4,4,7,4,3,2,1,1,4,1,6,7,4]
# print(maxs_app(l))

#question 3
# import math
# a=int(input('enter number'))
# print("factorial=", math.factorial(a))
# print('square root=', math.sqrt(a))

# b=int(input('enter number to find gcd with'))
# print(f"gcd of {a} and {b} is {math.gcd(a,b)}")

#question 2
from geometry import circle
from geometry import rectangle
r=int(input("enter radius of circle"))
print('area=', circle.area_cir(r))
print('circumference=',circle.circum(r))

l=int(input('enter length of rectangle'))
b=int(input('enter breafth of rectangle'))
print('area=',rectangle.area_rect(l,b))
print('perimeter=',rectangle.peri(l,b))