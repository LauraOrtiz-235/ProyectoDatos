import dash
from dash import dcc
import dash_core_components as dcc
from dash import html
import dash_html_components as html
import plotly.express as px
import pandas as pd
from connectionDB import Connection
import queries as sql
import plotly.graph_objects as go


external_stylesheets = ["https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css"]

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)



#Casos por departamento

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_casos_departamento(), con.connection)
con.closeConnection()

dfCasosDep = pd.DataFrame(query, columns=["nombre", "total"])
figBarCasosDep = px.bar(dfCasosDep.head(20), x="nombre", y="total",
                        color='total',
                        color_continuous_scale=["#C70039", "#900C3F"])

figTableDep = go.Figure(data=[go.Table(
    header=dict(values=list(dfCasosDep.columns),
        fill_color='#F0B1CA',
        align='left'),
    cells=dict(values=[dfCasosDep.nombre, dfCasosDep.total],
        fill_color='#FAE9F0',
        align='left'))
    ])


#Casos por municipio

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_casos_municipio(), con.connection)
con.closeConnection()

dfCasosMun = pd.DataFrame(query, columns=["nombre", "total"])
figBarCasosMun = px.bar(dfCasosMun.head(20), x="nombre", y="total",
                        color='total',
                        color_continuous_scale=["#C70039", "#900C3F"])


figTableMun = go.Figure(data=[go.Table(
    header=dict(values=list(dfCasosMun.columns),
        fill_color='#F0B1CA',
        align='left'),
    cells=dict(values=[dfCasosMun.nombre, dfCasosMun.total],
        fill_color='#FAE9F0',
        align='left'))
    ])


#Casos por país

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_casos_pais2(), con.connection)
con.closeConnection()

dfCasosP2 = pd.DataFrame(query, columns=["total", "nombre"])
figPieCasosP2 = px.pie(dfCasosP2, values= "total", names = "nombre")


con.openConnection()
query = pd.read_sql_query(sql.total_casos_pais(), con.connection)
con.closeConnection()

dfCasosP = pd.DataFrame(query, columns=["total", "nombre"])
figMapCasosP = px.choropleth(dfCasosP, locations="nombre",
                            locationmode="country names",
                            color="total",
                            hover_name="nombre",
                            color_continuous_scale=["#64C7FF", "#3355FF"])


con.openConnection()
query = pd.read_sql_query(sql.total_casos_pais(), con.connection)
con.closeConnection()

dfCasosP= pd.DataFrame(query, columns = ["nombre", "total"])
figTablePais = go.Figure(data=[go.Table(
    header=dict(values=list(dfCasosP.columns),
        fill_color='lightblue',
        align='left'),
    cells=dict(values=[dfCasosP.nombre, dfCasosP.total],
        fill_color='lavender',
        align='left'))
    ])



#Edad con + contagios

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.edad_con_mas_contagio(), con.connection)
con.closeConnection()

dfEdadCont = pd.DataFrame(query, columns=["total", "edad"])
figLineEdadCont = px.line(dfEdadCont, x="edad", y="total")


#Edad con + muertes

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.edad_con_mas_muertes(), con.connection)
con.closeConnection()

dfEdadMuertes = pd.DataFrame(query, columns=["total", "edad"])
figLineEdadMuertes = px.line(dfEdadMuertes, x="edad", y="total")


#Edad con + muertes

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.edad_con_mas_recuperacion(), con.connection)
con.closeConnection()

dfEdadRecu = pd.DataFrame(query, columns=["total", "edad"])
figLineEdadRecu = px.line(dfEdadRecu, x="edad", y="total")


#Total casos tipo contagio

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_por_tipo_contagio(), con.connection)
con.closeConnection()

dfCasosTipo = pd.DataFrame(query, columns=["total", "nombre", "tipo_contagio"])
figBarCasosTipo = px.bar(dfCasosTipo.head(20), x="tipo_contagio", y="total")


#Total casos tipo recuperacion

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_por_tipo_recuperacion(), con.connection)
con.closeConnection()

dfCasosRecu = pd.DataFrame(query, columns=["total", "tipo_recuperacion"])
figBarCasosRecu = px.bar(dfCasosRecu.head(20), x="tipo_recuperacion", y="total")


#Casos por genero

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_casos_por_genero(), con.connection)
con.closeConnection()

dfCasosGenero = pd.DataFrame(query, columns=["total", "sexo"])
figPieCasosGenero = px.pie(dfCasosGenero, values= "total", names = "sexo")


#Fecha Inicio sintomas

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_casos_fecha_inicio_sintomas(), con.connection)
con.closeConnection()

dfInicioFecha = pd.DataFrame(query, columns=["total", "fecha"])
figLineFecha = px.line(dfInicioFecha, x="fecha", y="total")





#Layout

app.layout = html.Div(children=[
    html.H1(children='Covid 19 Dashboard', className="text-center"), 
    html.H2(children='Casos contagios por Países (primeros 10 sin Colombia)'),
    dcc.Graph(
        id='PieCasosPais',
        figure=figPieCasosP2
    ),
    dcc.Graph(
        id='mapCasosPais',
        figure=figMapCasosP
    ),
    dcc.Graph(
        id='tableCasosPais',
        figure=figTablePais
    ),
    
    html.H2(children='Edad con mas Contagios'),
    dcc.Graph(
        id='LineEdadContagios',
        figure=figLineEdadCont
    ),

    html.H2(children='Edad con mas Muertes'),
    dcc.Graph(
        id='LineEdadMuertes',
        figure=figLineEdadMuertes
    ),

    html.H2(children='Edad con mas Recuperaciones'),
    dcc.Graph(
        id='LineEdadRecu',
        figure=figLineEdadRecu
    ),

    html.H2(children='Casos por Departamento'),
    dcc.Graph(
        id='BarCasosDep',
        figure=figBarCasosDep
    ),
    dcc.Graph(
        id='tableCasosDep',
        figure=figTableDep
    ),

    html.H2(children='Casos por Municipio'),
    dcc.Graph(
        id='BarCasosMun',
        figure=figBarCasosMun
    ),
    dcc.Graph(
        id='tableCasosMun',
        figure=figTableMun
    ),

    html.H2(children='Casos por Tipo de Contagio'),
    dcc.Graph(
        id='BarCasosTipo',
        figure=figBarCasosTipo
    ),

    html.H2(children='Casos por Tipo de Recuperación'),
    dcc.Graph(
        id='BarCasosRecu',
        figure=figBarCasosRecu
    ),

    html.H2(children='Casos por Género'),
    dcc.Graph(
        id='PieCasosGenero',
        figure=figPieCasosGenero
    ),

    html.H2(children='Casos por la fecha de inicio de los Síntomas'),
    dcc.Graph(
        id='LineFechaInicio',
        figure=figLineFecha
    ),

])

if __name__== '__main__' :
    app.run_server(debug = True)
