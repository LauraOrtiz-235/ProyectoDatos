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
                        color_continuous_scale=["#44C3BF", "#B0F7F5"])

figTableDep = go.Figure(data=[go.Table(
    header=dict(values=list(dfCasosDep.columns),
        fill_color='#80D8DE',
        align='left'),
    cells=dict(values=[dfCasosDep.nombre, dfCasosDep.total],
        fill_color='#DEF9FB',
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
                        color_continuous_scale=["#DAF7A6", "#83E9B6"])

figMapCasosMun = px.scatter_geo(dfCasosMun, locations="nombre", 
                            color="nombre",
                            hover_name="nombre", 
                            projection="natural earth")

figTableMun = go.Figure(data=[go.Table(
    header=dict(values=list(dfCasosMun.columns),
        fill_color='#9EEDC8',
        align='left'),
    cells=dict(values=[dfCasosMun.nombre, dfCasosMun.total],
        fill_color='#E0FFF6',
        align='left'))
    ])


#Casos por país

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_casos_pais2(), con.connection)
con.closeConnection()

dfCasosP2 = pd.DataFrame(query, columns=["total", "nombre"])
figPieCasosP2 = px.pie(dfCasosP2, values= "total", names = "nombre", color_discrete_sequence=px.colors.sequential.Emrld)

con.openConnection()
query = pd.read_sql_query(sql.total_casos_pais(), con.connection)
con.closeConnection()

dfCasosP = pd.DataFrame(query, columns=["total", "nombre", "codigo"])
figMapCasosP = px.choropleth(dfCasosP, locations="nombre",
                            locationmode="country names",
                            color="total",
                            hover_name="nombre",
                            color_continuous_scale=["#B0F7F5", "#44C3BF"])

con.openConnection()
query = pd.read_sql_query(sql.total_casos_pais(), con.connection)
con.closeConnection()

dfCasosP= pd.DataFrame(query, columns = ["nombre", "total"])
figTablePais = go.Figure(data=[go.Table(
    header=dict(values=list(dfCasosP.columns),
        fill_color='#80D8DE',
        align='left'),
    cells=dict(values=[dfCasosP.nombre, dfCasosP.total],
        fill_color='#DEF9FB',
        align='left'))
    ])


#Muertes por pais

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.muertes_por_pais(), con.connection)
con.closeConnection()

dfMuertesP = pd.DataFrame(query, columns=["total", "nombre"])
figBarMuertesP = px.bar(dfMuertesP.head(20), x="nombre", y="total",
                        color='total',
                        color_continuous_scale=["#DAF7A6", "#83E9B6"])

con.openConnection()
query = pd.read_sql_query(sql.muertes_por_pais2(), con.connection)
con.closeConnection()

dfMuertesPais = pd.DataFrame(query, columns=["nombre", "total"])
figTablePaisM = go.Figure(data=[go.Table(
    header=dict(values=list(dfMuertesPais.columns),
        fill_color='#9EEDC8',
        align='left'),
    cells=dict(values=[dfMuertesPais.nombre, dfMuertesPais.total],
        fill_color='#E0FFF6',
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
figBarCasosTipo = px.bar(dfCasosTipo.head(20), x="tipo_contagio", y="total", color_discrete_sequence=px.colors.diverging.Tropic)


#Total casos tipo recuperacion

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_por_tipo_recuperacion(), con.connection)
con.closeConnection()

dfCasosRecu = pd.DataFrame(query, columns=["total", "tipo_recuperacion"])
figBarCasosRecu = px.bar(dfCasosRecu.head(20), x="tipo_recuperacion", y="total", color_discrete_sequence=px.colors.sequential.Tealgrn)


#Casos por genero

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_casos_por_genero(), con.connection)
con.closeConnection()

dfCasosGenero = pd.DataFrame(query, columns=["total", "sexo"])
figPieCasosGenero = px.pie(dfCasosGenero, values= "total", names = "sexo", color_discrete_sequence=px.colors.sequential.Darkmint)


#Fecha Inicio sintomas

con = Connection()
con.openConnection()
query = pd.read_sql_query(sql.total_casos_fecha_inicio_sintomas(), con.connection)
con.closeConnection()

dfInicioFecha = pd.DataFrame(query, columns=["total", "fecha"])
figLineFecha = px.line(dfInicioFecha, x="fecha", y="total")





#Layout

app.layout = html.Div(style={'backgroundColor': "#35C5E5"}, children=[
    html.H1(children='Casos COVID-19 en Colombia', className="text-center", style={'color': "#E7FEFF"}), 
    html.Div(className="container-fluid", children=[
        html.Div(className="row", children=[
            html.Div(className="col", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header bg-info text-#D4F2FB", children=[
                        html.H2(children='Casos contagios por Países (primeros 10 sin Colombia)', style={'color': "#E7FEFF"}),
                    ]),
                    dcc.Graph(
                        id='PieCasosPais',
                        figure=figPieCasosP2
                    ),
                ]),
            ]),
        ]),
    ]),
    html.Div(className="container-fluid", children=[
        html.Div(className="row", children=[
            html.Div(className="col", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header bg-info text-#D4F2FB", children=[
                        html.H2(children='Casos contagios por Países', style={'color': "#E7FEFF"}),
                            html.Div(className="card-body", children=[
                                html.Div(className="row", children=[
                                    html.Div(className="col-lg-12 col-xl-6", children=[
                                        dcc.Graph(
                                            id='mapCasosPais',
                                            figure=figMapCasosP
                                        ),
                                    ]),
                                    html.Div(className="col-lg-12 col-xl-6", children=[
                                        dcc.Graph(
                                            id='tableCasosPais',
                                            figure=figTablePais
                                        ),
                                    ]),
                                ]),
                            ]),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.Div(className="container-fluid", children=[
        html.Div(className="row", children=[
            html.Div(className="col", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header bg-info text-#D4F2FB", children=[
                        html.H2(children='Muertes por país', style={'color': "#E7FEFF"}),
                    ]),
                    html.Div(className="card-body", children=[
                        html.Div(className="row", children=[
                            html.Div(className="col-lg-12 col-xl-6", children=[
                                dcc.Graph(
                                    id='TableMuertesPais2',
                                    figure=figTablePaisM
                                ),
                            ]),
                            html.Div(className="col-lg-12 col-xl-6", children=[
                                dcc.Graph(
                                    id='BarMuertesPais',
                                    figure=figBarMuertesP
                                ),
                            ]),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ]),
    
    html.H2(children='Edad con mas Contagios', style={'color': "#E7FEFF"}),
    dcc.Graph(
        id='LineEdadContagios',
        figure=figLineEdadCont
    ),

    html.H2(children='Edad con mas Muertes', style={'color': "#E7FEFF"}),
    dcc.Graph(
        id='LineEdadMuertes',
        figure=figLineEdadMuertes
    ),

    html.H2(children='Edad con mas Recuperaciones', style={'color': "#E7FEFF"}),
    dcc.Graph(
        id='LineEdadRecu',
        figure=figLineEdadRecu
    ),

    html.Div(className="container-fluid", children=[
        html.Div(className="row", children=[
            html.Div(className="col", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header bg-info text-#D4F2FB", children=[
                        html.H2(children='Casos por Departamento', style={'color': "#E7FEFF"}),
                            html.Div(className="card-body", children=[
                                html.Div(className="row", children=[
                                    html.Div(className="col-lg-12 col-xl-6", children=[
                                        dcc.Graph(
                                            id='BarCasosDep',
                                            figure=figBarCasosDep
                                        ),
                                    ]),
                                    html.Div(className="col-lg-12 col-xl-6", children=[
                                        dcc.Graph(
                                            id='tableCasosDep',
                                            figure=figTableDep
                                        ),
                                    ]),
                                ]),
                            ]),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.Div(className="container-fluid", children=[
        html.Div(className="row", children=[
            html.Div(className="col", children=[
                html.Div(className="card", children=[
                    html.Div(className="card-header bg-info text-#D4F2FB", children=[
                        html.H2(children='Casos por Municipio', style={'color': "#E7FEFF"}),
                    ]),
                    html.Div(className="card-body", children=[
                        html.Div(className="row", children=[
                            html.Div(className="col-lg-12 col-xl-6", children=[
                                dcc.Graph(
                                    id='BarCasosMun',
                                    figure=figBarCasosMun
                                ),
                            ]),
                            html.Div(className="col-lg-12 col-xl-6", children=[
                                dcc.Graph(
                                    id='tableCasosMun',
                                    figure=figTableMun
                                ),
                            ]),
                            dcc.Graph(
                                id='MapCasosMun',
                                figure=figMapCasosMun
                            ),
                        ]),
                    ]),
                ]),
            ]),
        ]),
    ]),

    html.H2(children='Casos por Tipo de Contagio', style={'color': "#E7FEFF"}),
    dcc.Graph(
        id='BarCasosTipo',
        figure=figBarCasosTipo
    ),

    html.H2(children='Casos por Tipo de Recuperación', style={'color': "#E7FEFF"}),
    dcc.Graph(
        id='BarCasosRecu',
        figure=figBarCasosRecu
    ),

    html.H2(children='Casos por Género', style={'color': "#E7FEFF"}),
    dcc.Graph(
        id='PieCasosGenero',
        figure=figPieCasosGenero
    ),

    html.H2(children='Casos por la fecha de inicio de los Síntomas', style={'color': "#E7FEFF"}),
    dcc.Graph(
        id='LineFechaInicio',
        figure=figLineFecha
    ),

])

if __name__== '__main__' :
    app.run_server(debug = True)
