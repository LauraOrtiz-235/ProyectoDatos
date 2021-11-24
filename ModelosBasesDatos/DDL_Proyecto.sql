-- object: public.casos | type: TABLE --
-- DROP TABLE IF EXISTS public.casos CASCADE;
CREATE TABLE public.casos (
	id_caso int2 NOT NULL,
	fecha_reporte_web date NOT NULL,
	fecha_notificacion date NOT NULL,
	edad smallint NOT NULL,
	sexo char(1) NOT NULL,
	recuperado char(1) NOT NULL,
	fecha_inicio_sintomas date,
	fecha_muerte date,
	fecha_diagnostico date,
	fecha_recuperacion date,
	codigo_pais smallint,
	codigo_municipio smallint,
	CONSTRAINT casos_pk PRIMARY KEY (id_caso)

);
-- ddl-end --
ALTER TABLE public.casos OWNER TO postgres;
-- ddl-end --

-- object: public.pais | type: TABLE --
-- DROP TABLE IF EXISTS public.pais CASCADE;
CREATE TABLE public.pais (
	codigo smallint NOT NULL,
	nombre varchar(10) NOT NULL,
	CONSTRAINT pais_pk PRIMARY KEY (codigo)

);
-- ddl-end --
ALTER TABLE public.pais OWNER TO postgres;
-- ddl-end --

-- object: public.municipio | type: TABLE --
-- DROP TABLE IF EXISTS public.municipio CASCADE;
CREATE TABLE public.municipio (
	codigo smallint NOT NULL,
	nombre varchar(20) NOT NULL,
	codigo_departamento smallint,
	CONSTRAINT municipio_pk PRIMARY KEY (codigo)

);
-- ddl-end --
ALTER TABLE public.municipio OWNER TO postgres;
-- ddl-end --

-- object: public.departamento | type: TABLE --
-- DROP TABLE IF EXISTS public.departamento CASCADE;
CREATE TABLE public.departamento (
	codigo smallint NOT NULL,
	nombre varchar(20) NOT NULL,
	CONSTRAINT departamento_pk PRIMARY KEY (codigo)

);
-- ddl-end --
ALTER TABLE public.departamento OWNER TO postgres;
-- ddl-end --

-- object: departamento_fk | type: CONSTRAINT --
-- ALTER TABLE public.municipio DROP CONSTRAINT IF EXISTS departamento_fk CASCADE;
ALTER TABLE public.municipio ADD CONSTRAINT departamento_fk FOREIGN KEY (codigo_departamento)
REFERENCES public.departamento (codigo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: pais_fk | type: CONSTRAINT --
-- ALTER TABLE public.casos DROP CONSTRAINT IF EXISTS pais_fk CASCADE;
ALTER TABLE public.casos ADD CONSTRAINT pais_fk FOREIGN KEY (codigo_pais)
REFERENCES public.pais (codigo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: municipio_fk | type: CONSTRAINT --
-- ALTER TABLE public.casos DROP CONSTRAINT IF EXISTS municipio_fk CASCADE;
ALTER TABLE public.casos ADD CONSTRAINT municipio_fk FOREIGN KEY (codigo_municipio)
REFERENCES public.municipio (codigo) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: public.tipo_contagio | type: TABLE --
-- DROP TABLE IF EXISTS public.tipo_contagio CASCADE;
CREATE TABLE public.tipo_contagio (
	nombre varchar(45),
	id_caso_casos int2
);
-- ddl-end --
ALTER TABLE public.tipo_contagio OWNER TO postgres;
-- ddl-end --

-- object: public.tipo_recuperacion | type: TABLE --
-- DROP TABLE IF EXISTS public.tipo_recuperacion CASCADE;
CREATE TABLE public.tipo_recuperacion (
	nombre varchar(45),
	id_caso_casos int2
);
-- ddl-end --
ALTER TABLE public.tipo_recuperacion OWNER TO postgres;
-- ddl-end --

-- object: public.ubicacion_caso | type: TABLE --
-- DROP TABLE IF EXISTS public.ubicacion_caso CASCADE;
CREATE TABLE public.ubicacion_caso (
	nombre varchar(45),
	id_caso_casos int2
);
-- ddl-end --
ALTER TABLE public.ubicacion_caso OWNER TO postgres;
-- ddl-end --

-- object: casos_fk | type: CONSTRAINT --
-- ALTER TABLE public.ubicacion_caso DROP CONSTRAINT IF EXISTS casos_fk CASCADE;
ALTER TABLE public.ubicacion_caso ADD CONSTRAINT casos_fk FOREIGN KEY (id_caso_casos)
REFERENCES public.casos (id_caso) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: casos_fk | type: CONSTRAINT --
-- ALTER TABLE public.tipo_recuperacion DROP CONSTRAINT IF EXISTS casos_fk CASCADE;
ALTER TABLE public.tipo_recuperacion ADD CONSTRAINT casos_fk FOREIGN KEY (id_caso_casos)
REFERENCES public.casos (id_caso) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

-- object: casos_fk | type: CONSTRAINT --
-- ALTER TABLE public.tipo_contagio DROP CONSTRAINT IF EXISTS casos_fk CASCADE;
ALTER TABLE public.tipo_contagio ADD CONSTRAINT casos_fk FOREIGN KEY (id_caso_casos)
REFERENCES public.casos (id_caso) MATCH FULL
ON DELETE SET NULL ON UPDATE CASCADE;
-- ddl-end --

