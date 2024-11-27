def Are_U_A_Dev(language):
    if language == 'Javascript' or language == 'javascript':
        return 'tu es un développeur web'
    elif language == 'Python' or language == 'python':
        return 'tu es un développeur IA'
    elif language == 'Java' or language == 'java':
        return 'tu es un développeur logiciel'
    elif language == 'Reactjs' or language == 'reactjs':
        return 'tu es un développeur mobile'
    else:
        return 'un jour, je serai le meilleur développeur…'
    
print(Are_U_A_Dev('Python'))

print(Are_U_A_Dev('Javascript'))

print(Are_U_A_Dev('java'))

print(Are_U_A_Dev('reactjs'))

print(Are_U_A_Dev('C#'))

