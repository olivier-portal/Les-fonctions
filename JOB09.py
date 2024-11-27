def moyenne(note1, note2, note3):
    moyenne_etudiant = round(((note1 + note2 + note3) / 3), 2)
    print(moyenne_etudiant)
    if moyenne_etudiant >= 15 <= 20:
        return 'Très bon élève'
    elif moyenne_etudiant >= 11 < 15 :
        return 'Bon élève'
    elif moyenne_etudiant >= 8 < 11 :
        return 'Élève moyen'
    elif moyenne_etudiant >= 0 < 8 :
        return 'Élève devant faire des efforts'
        
    
    
print(moyenne(11, 15.5, 8.5))

print(moyenne(2, 3.5, 4.5))

print(moyenne(18, 19.5, 18.5))

print(moyenne(11, 10.5, 8.5))