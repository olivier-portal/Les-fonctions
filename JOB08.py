def Fruits_season(type, saison):
    if type == 'fruits' and saison == 'hiver':
        return 'orange, mandarine et kiwi'
    elif type == 'fruits' and saison == 'été':
        return 'Poire, fraise, cassis'
    elif type == 'légume' and saison == 'hiver':
        return 'carotte, topinambour, endive'
    elif type == 'légume' and saison == 'été':
        return 'artichaut, aubergine,navet'
    
print(Fruits_season('fruits', 'hiver'))

print(Fruits_season('fruits', 'été'))

print(Fruits_season('légume', 'hiver'))

print(Fruits_season('légume', 'été'))