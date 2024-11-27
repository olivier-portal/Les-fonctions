def is_pair(number):
    if number != int(number):
        return 'Le nombre doit être entier'
    elif number < 0:
        return 'Le nombre doit-être positif'
    elif number % 2 == 0:
        return f"{number} est pair"
    else:
        return f"{number} est impair"

print(is_pair(0.5))

print(is_pair(5))

print(is_pair(6))

print(is_pair(-6))