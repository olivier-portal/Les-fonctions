def calcule(num1, operator, num2):
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    elif operator == '*':
        return num1 * num2
    elif operator == '/':
        return num1 / num2
    elif operator == '%':
        return num1 % num2
    else:
        return 'num1 & num2 doivent être des nombres et operator un caractère (+, -, *, / ou %)'
    
print(calcule(4, '*', 5))

print(calcule(6, '/', 2))

print(calcule(17, '+', 5))

print(calcule(24, '%', 6))

print(calcule(4, '-', 5))
    