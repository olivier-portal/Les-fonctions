minutes = int(input('Entre le nombre de minutes : '))

def time_to_text(minutes):
    
    # if minutes n'est pas un int!!!! ou float
    # alors redemander l'input //return msg d'erreur qui dit que c'est le bon type de valeur attendu 
    
    minutes = int(minutes)
    heure = 0
    if minutes < 0:
        return 'Il faut rentrer un nombre positif'
    elif minutes == 1:
        return (f'{heure} heure et {minutes} minute')
    elif minutes < 60:
        return (f'{heure} heure et {minutes} minutes')
    elif minutes >= 90:
        while minutes >= 60 < 90:
            heure = minutes // 60
            minutes = minutes % 60
            return (f'{heure} heures et {minutes} minutes')
    elif minutes >= 60:
        while minutes >= 60 < 90:
            heure = minutes // 60
            minutes = minutes % 60
            return (f'{heure} heure et {minutes} minutes')
        

# print(time_to_text(1))

# print(time_to_text(59))

# print(time_to_text(75))

# print(time_to_text(479))

# print(time_to_text(-10))

print(time_to_text(minutes))