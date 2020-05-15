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

print ('3 + 2 = '.__str__(), 3 + 2)
print ('3 - 2 = '.__str__(), 3 - 2)
print ('3 * 2 = '.__str__(), 3 * 2)
print ('3 / 2 = '.__str__(), 3 / 2)
print ('3 // 2 = '.__str__(), 3 // 2)
print ('3 // 2 = '.__str__(), 3 ** 2)
print ('3 % 2 = '.__str__(), 3 % 2)
print ('3 * (2 + 1) = '.__str__(), 3 * (2 + 1))

# Comparisons:
# Equal:            3 == 2
# Not Equal:        3 != 2
# Greater Than:     3 > 2
# Less Than:        3 < 2
# Grater or Equal:  3 >= 2
# Less or Equal:    3 <= 2

num1 = 3
num2 = 2

print(num1, '=='.__str__(), num2, ', Equal ='.__str__(), num1 == num2 )
print(num1, '!='.__str__(), num2, ', Not Equal ='.__str__(), num1 != num2 )
print(num1, '>'.__str__(), num2, ', Greater Than ='.__str__(), num1 > num2 )
print(num1, '<'.__str__(), num2, ', Less Than ='.__str__(), num1 < num2 )
print(num1, '>='.__str__(), num2, ', Greater or Equal ='.__str__(), num1 >= num2 )
print(num1, '<='.__str__(), num2, ', Less or Equal ='.__str__(), num1 <= num2 )

# Casting
num3 = '300'
num4 = '400'

num5 = int(num3)
num6 = int(num4)

print('String Addition ='.__str__(), num3 + num4)
print('String --> Integer ='.__str__(), num5 + num6)