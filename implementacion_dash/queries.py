#Consultas de todos los datos de cada tabla

def leer_tabla_dept():
    return """select *
              from departamento"""

def leer_tabla_municipio():
    return """select *
              from municipio"""

def leer_tabla_pais():
    return """select *
              from pais"""

def leer_tabla_casos(): #Los datos de los primeros 100 casos
    return """select * 
              from casos
              where id_caso between 1 and 100""" 

def edad_con_mas_contagio():
    return """select count(c.id_caso), c.edad
              from casos c
              group by edad
              order by count desc"""

def edad_con_mas_muertes():
    return """select count(c.fecha_muerte), c.edad
              from casos c
              group by edad
              order by count desc"""

def edad_con_mas_recuperacion():
    return """select count(c.fecha_recuperacion), c.edad
              from casos c
              group by edad
              order by count desc"""

def total_casos_colombia():
    return """select count(c.id_caso) as total_casos, p.nombre
              from pais p join casos c on (p.codigo = c.codigo_pais)
              where p.nombre = 'COLOMBIA'
              group by nombre"""

def total_por_tipo_contagio(): #En Colombia
    return """select count(c.id_caso) as total_casos, p.nombre, c.tipo_contagio
              from pais p join casos c on (p.codigo = c.codigo_pais)
              where p.nombre = 'COLOMBIA'
              group by nombre, tipo_contagio"""

def total_casos_departamento():
    return """select count(s.id_caso), d.nombre
              from (casos c join municipio m on (c.codigo_municipio = m.codigo)) s
                            join departamento d on (s.codigo_departamento = d.codigo)
              group by d.nombre
              order by count desc"""

def total_casos_municipio():
    return """select count(c.id_caso), m.nombre
              from (casos c join municipio m on (c.codigo_municipio = m.codigo))
              group by m.nombre
              order by count desc"""

def total_por_tipo_recuperacion():
    return """select count(c.id_caso), c.tipo_recuperacion
              from casos c
              group by tipo_recuperacion
              order by count desc
              limit 2"""

def total_casos_por_genero():
    return """select count(c.id_caso), c.sexo
              from casos c
              group by sexo"""

def total_casos_fecha_inicio_sintomas():
    return """select count(c.id_caso), fecha_inicio_sintomas
              from casos c
              group by fecha_inicio_sintomas
              order by count desc"""
