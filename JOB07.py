def Are_U_A_Dev(language):
    if language == 'Javascript' or language == 'javascript':
        return 'tu es un développeur web'
    elif language == 'Python' or language == 'python':
        return 'tu es un développeur IA'
    else:
        return 'tu es un OVNI'
    
print(Are_U_A_Dev('Python'))

print(Are_U_A_Dev('Javascript'))

print(Are_U_A_Dev('C#'))

