from fastapi import FastAPI
import pandas as pd

app = FastAPI(title='PROYECTO INDIVIDUAL Nº1',
            description='Jhoeliel Palma  - Data Engineering',
            version='1.0.1')


@app.get("/")
async def root():
    return "PI Data Engineering: Jhoeliel Palma Salazar"

@app.get("/about")
async def about():
    return 'PI Data Engineering: Jhoeliel Palma Salazar'

# API 1
@app.get('/1-get_word_count()')
async def get_word_count(plataforma:str,keyword:str): # 2 parametros de entrada: 2 strings
    #df_completo = pd.read_csv('https://raw.githubusercontent.com/Jhoeliel/PI-DataEngineering/main/completo.csv')
    df_completo = pd.read_csv('Datasets/completo.csv')
    df_filtrado = df_completo[df_completo['id'].str.contains(plataforma[0])]
    count = int(df_filtrado['title'].str.contains(keyword).sum())
    return plataforma,count # 2 valores de salida 1 string y 1 entero

# API 2
@app.get('/2-get_score_count()')
async def get_score_count(plataforma:str,score:int,year:int): # 3 parametros de entrada: 1 string y 2 enteros
    #df_completo = pd.read_csv('https://raw.githubusercontent.com/Jhoeliel/PI-DataEngineering/main/completo.csv')
    df_completo = pd.read_csv('Datasets/completo.csv')
    df_filtrado = df_completo[df_completo['id'].str.contains(plataforma[0])]
    df_filtrado = df_filtrado[df_filtrado['release_year'] == year]
    df_filtrado = df_filtrado[df_filtrado['type'] == 'movie']
    count=int(df_filtrado[df_filtrado['score'] > score].shape[0])
    return plataforma,count # 2 valores de salida 1 string y 1 entero

# API 3
@app.get('/3-get_second_score()')
async def get_second_score(plataforma:str): # 1 parametro de entrada: 1 string
    #df_completo = pd.read_csv('https://raw.githubusercontent.com/Jhoeliel/PI-DataEngineering/main/completo.csv')
    df_completo = pd.read_csv('Datasets/completo.csv')
    df_filtrado=df_completo[df_completo['id'].str.contains(plataforma[0])]
    df_filtrado = df_filtrado[df_filtrado['type'] == 'movie']
    df_filtrado = df_filtrado.sort_values(by=['score','title'], ascending=[False, True])
    df_filtrado= df_filtrado.reset_index(drop=True)
    title=df_filtrado['title'][1]
    score=int(df_filtrado['score'][1])
    return title,score # 2 valores de salida 1 string y 1 entero

# API 4
@app.get('/4-get_longest()') 
async def get_longest(plataforma:str,duracion:str,year:int): # 3 parametros de entrada: 2 strings y 1 entero
    #df_completo = pd.read_csv('https://raw.githubusercontent.com/Jhoeliel/PI-DataEngineering/main/completo.csv')
    df_completo = pd.read_csv('Datasets/completo.csv')
    df_filtrado=df_completo[df_completo['id'].str.contains(plataforma[0])]
    df_filtrado = df_filtrado[df_filtrado['release_year'] == year]
    df_filtrado = df_filtrado[df_filtrado['duration_type'].str.contains(duracion)]
    df_filtrado = df_filtrado.sort_values(by=['duration_int'], ascending=[False])
    df_filtrado= df_filtrado.reset_index(drop=True)
    title=df_filtrado['title'][0]
    duracion_int=int(df_filtrado['duration_int'][0])
    duracion_type=df_filtrado['duration_type'][0]
    return title,duracion_int,duracion_type # 3 valores de salida 1 string, 1 entero y 1 string

# API 5
@app.get('/5-get_rating_count()')
async def get_rating_count(rating:str): # 1 parametro de entrada: 1 string
    #df_completo = pd.read_csv('https://raw.githubusercontent.com/Jhoeliel/PI-DataEngineering/main/completo.csv')
    df_completo = pd.read_csv('Datasets/completo.csv')
    df_filtrado = df_completo[df_completo['rating']==rating]
    cantidad=int(df_filtrado.shape[0])
    return rating,cantidad # 2 valores de salida 1 string y 1 entero