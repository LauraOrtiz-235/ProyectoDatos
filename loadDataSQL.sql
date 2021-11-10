alter table pais
alter column nombre type varchar(50);

alter table municipio
alter column nombre type varchar(50);

alter table municipio
alter column codigo type integer;

copy departamento(codigo, nombre)
from '/home/laura/Desktop/univ/univ2021-2/Datos/proyecto/data/departamentos.csv'
delimiter ','
csv header;

copy pais(codigo, nombre)
from '/home/laura/Desktop/univ/univ2021-2/Datos/proyecto/data/pais.csv'
delimiter ','
csv header;

copy municipio(codigo, nombre, codigo_departamento)
from '/home/laura/Desktop/univ/univ2021-2/Datos/proyecto/data/municipio.csv'
delimiter ','
csv header;

copy casos(id_caso, fecha_reporte_web, fecha_notificacion, edad, sexo, tipo_contagio, ubicacion_caso, recuperado, 
               fecha_inicio_sintomas, fecha_muerte, fecha_diagnostico, fecha_recuperacion, tipo_recuperacion, 
              codigo_pais, codigo_municipio)
from '/home/laura/Desktop/univ/univ2021-2/Datos/proyecto/data/casos.csv'
delimiter ','
csv header;

alter table casos
alter column codigo_municipio type integer;

ALTER TABLE casos
ALTER COLUMN fecha_diagnostico type date;

ALTER TABLE casos
ALTER COLUMN fecha_inicio_sintomas type date;
