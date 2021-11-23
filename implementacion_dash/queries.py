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


#Consultas para análisis en dash 

def edad_con_mas_contagio():
    return """select count(c.id_caso) as total, c.edad
              from casos c
              group by edad
              order by edad asc"""

def edad_con_mas_muertes():
    return """select count(c.fecha_muerte) as total, c.edad
              from casos c
              group by edad
              order by edad asc"""

def edad_con_mas_recuperacion():
    return """select count(c.fecha_recuperacion) as total, c.edad
              from casos c
              group by edad
              order by edad asc"""

def total_casos_pais():
    return """select p.nombre as nombre, count(c.id_caso) as total
                from pais p join casos c on (c.codigo_pais = p.codigo)
                group by nombre
                order by total desc"""

def total_casos_pais2(): #sin Colombia
    return """select p.nombre as nombre, count(c.id_caso) as total
                from pais p join casos c on (c.codigo_pais = p.codigo)
                where p.nombre != 'COLOMBIA'
                group by nombre
                having count(c.id_caso) > 20
                order by total desc"""

def total_casos_colombia():
    return """select count(c.id_caso) as total_casos, p.nombre
              from pais p join casos c on (p.codigo = c.codigo_pais)
              where p.nombre = 'COLOMBIA'
              group by nombre"""

def total_por_tipo_contagio(): #En Colombia
    return """select count(c.id_caso) as total, p.nombre, c.tipo_contagio
              from pais p join casos c on (p.codigo = c.codigo_pais)
              where p.nombre = 'COLOMBIA'
              group by nombre, tipo_contagio"""

def total_casos_departamento():
    return """select count(s.id_caso) as total, d.nombre as nombre
              from (casos c join municipio m on (c.codigo_municipio = m.codigo)) s
                            join departamento d on (s.codigo_departamento = d.codigo)
              group by d.nombre
              order by total desc"""

def total_casos_municipio():
    return """select count(c.id_caso) as total, m.nombre
              from (casos c join municipio m on (c.codigo_municipio = m.codigo))
              group by m.nombre
              order by total desc"""

def total_por_tipo_recuperacion():
    return """select count(c.id_caso) as total, c.tipo_recuperacion
              from casos c
              group by tipo_recuperacion
              order by total desc
              limit 2"""

def total_casos_por_genero():
    return """select count(c.id_caso) as total, c.sexo
              from casos c
              group by sexo"""

def total_casos_fecha_inicio_sintomas():
    return """select count(c.id_caso) as total, fecha_inicio_sintomas as fecha
              from casos c
              group by fecha_inicio_sintomas
              order by fecha asc"""

def muertes_por_pais(): #Sin Colombia
    return """select count(c.id_caso) as total, p.nombre
              from pais p join casos c on (p.codigo = c.codigo_pais)
              where p.nombre != 'COLOMBIA' and c.recuperado = 'F'
              group by nombre
              order by total desc"""

def muertes_por_pais2():
    return """select count(c.id_caso) as total, p.nombre
              from pais p join casos c on (p.codigo = c.codigo_pais)
              where c.recuperado = 'F'
              group by nombre
              order by total desc"""


