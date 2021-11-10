#Consultas de todos los datos de cada tabla

def departamento():
    return """select *
           from departamento"""

def municipio():
    return """select *
           from municipio"""

def pais():
    return """select *
           from pais"""

def cases():
    return """select * 
           from casos
           where id_caso between 1 and 100""" 
#Los datos de los primeros 100 casos
