# Arithmetic Operators:
# Addition:         3 + 2
# Subtraction:      3 - 2
# Multiplication:   3 * 2
# Division:         3 / 2
# Floor Division    3 // 2
# Exponent:         3 ** 3
# Modulus:          3 % 2

num = 3
print(type(num))

print ('3 + 2 = ', 3 + 2)
print ('3 - 2 = ', 3 - 2)
print ('3 * 2 = ', 3 * 2)
print ('3 / 2 = ', 3 / 2)
print ('3 // 2 = ', 3 // 2)
print ('3 // 2 = ', 3 ** 2)
print ('3 % 2 = ', 3 % 2)
print ('3 * (2 + 1) = ', 3 * (2 + 1))

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Grater or Equal:  3 >= 2
# Less or Equal:    3 <= 2

num1 = 3
num2 = 2

print(num1, '==', num2, ', Equal =', num1 == num2 )
print(num1, '!=', num2, ', Not Equal =', num1 != num2 )
print(num1, '>', num2, ', Greater Than =', num1 > num2 )
print(num1, '<', num2, ', Less Than =', num1 < num2 )
print(num1, '>=', num2, ', Greater or Equal =', num1 >= num2 )
print(num1, '<=', num2, ', Less or Equal =', num1 <= num2 )

# Casting
num3 = '300'
num4 = '400'

num5 = int(num3)
num6 = int(num4)

print('String Addition =', num3 + num4)
print('String --> Integer =', num5 + num6)