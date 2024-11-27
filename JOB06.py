def is_positive(nombre):
    if nombre >= 0:
        return 'positif'
    else:
        return 'négatif'

print(is_positive(-5))

print(is_positive(5))