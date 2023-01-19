from fastapi import FastAPI, File, UploadFile
import pandas as pd
from flask import Flask

app = Flask(__name__)



app = FastAPI(title='PROYECTO INDIVIDUAL Nº1',
            description='Data Engineering',
            version='1.0.1')

@app.post("/")
def upload():
    return "hello"

"""@app.route('/', methods=["GET"])
def hello_world():
    return "Hello World ooo" """

"""# Carga la base de datos al iniciar
@app.on_event('startup')
def startup():
    global df_completo
    df_completo = pd.read_csv('Datasets/completo.csv')


@app.get("/")
async def root():
    return 'PI Data Engineering: Jhoeliel Palma Salazar'

@app.get("/about")
async def about():
    return 'PI Data Engineering: Jhoeliel Palma Salazar'

# Consulta 1
@app.get('/get_word_count({plataforma},{keyword})')
async def get_word_count(plataforma,keyword):
    df_filtrado = df_completo[df_completo['id'].str.contains(plataforma[0])]
    count = df_filtrado['title'].str.contains(keyword).sum()
    return count

# Consulta 2
@app.get('/get_score_count({plataforma},{score},{year})')
async def get_score_count(plataforma,score,year):
    df_filtrado = df_completo[df_completo['id'].str.contains(plataforma[0])]
    df_filtrado = df_filtrado[df_filtrado['release_year'] == year]
    df_filtrado = df_filtrado[df_filtrado['type'] == 'movie']
    count=df_filtrado[df_filtrado['score'] > score].shape[0]
    return count

# Consulta 3
@app.get('/get_second_score({plataforma})')
def get_second_score(plataforma):
    df_filtrado=df_completo[df_completo['id'].str.contains(plataforma[0])]
    df_filtrado = df_filtrado[df_filtrado['type'] == 'movie']
    df_filtrado = df_filtrado.sort_values(by=['score','title'], ascending=[False, True])
    df_filtrado= df_filtrado.reset_index(drop=True)
    title=df_filtrado['title'][1]
    return title

# Consulta 4
@app.get('/get_longest({plataforma},{duracio},{year})')
def get_longest(plataforma,duracion,year):
    df_filtrado=df_completo[df_completo['id'].str.contains(plataforma[0])]
    df_filtrado = df_filtrado[df_filtrado['release_year'] == year]
    df_filtrado = df_filtrado[df_filtrado['duration_type'].str.contains(duracion)]
    df_filtrado = df_filtrado.sort_values(by=['duration_int'], ascending=[False])
    df_filtrado= df_filtrado.reset_index(drop=True)
    title=df_filtrado['title'][0]
    return title

# Consulta 5
@app.get('/get_rating_count({rating})')
def get_rating_count(rating):
    df_filtrado = df_completo[df_completo['rating']==rating]
    cantidad=df_filtrado.shape[0]
    return cantidad"""