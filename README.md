# <h1 align=center> **PROYECTO INDIVIDUAL Nº1** </h1>
<p align=center><img src=https://www.feedingthemachine.ai/wp-content/uploads/2021/04/data-engineering-dl-2020-1024x401-1.png><p>

Bienvenidos al Proyecto Individual N°1 - Data Engineering, de la etapa de labs de [HENRY](https://www.soyhenry.com/)
<br/>
Elaborado por Jhoeliel Palma Salazar
<hr>

## **Descripcion**
Como parte del equipo de data de una empresa, el área de análisis de datos nos ha solicitado al área de Data Engineering ciertos requerimientos para el óptimo desarrollo de sus actividades. Para ello deberemos elaborar las *transformaciones* requeridas y disponibilizar los datos mediante la *elaboración y ejecución de una API*.

De acuerdo a los lineamientos del area solicitante decidimos usar el siguiente Stack tecnologico:
+ Python --> EDA, ETL, Coding
+ FastApi --> Framework para disponibilizar los datos
+ Deta --> Lightweight cloud compute runtime para el deployment

Los datasets proporcionados por el área de análisis de datos se encuentran en la carpeta Datasets de este repositorio, asi como tambien el dataset resultante del proceso de ETL. Asi mismo en el root del repositorio encontraremos el archivo main.py en donde se encuentra la codificacion de las API requeridas, el archivo ETL.py donde se encuentra la funcion que hizo el ETL de los datasets.

## **Requerimientos del área de análisis de datos**

**`Transformaciones`**:  El analista de datos requiere estas, ***y solo estas***, transformaciones para sus datos:


+ Generar campo **`id`**: Cada id se compondrá de la primera letra del nombre de la plataforma, seguido del show_id ya presente en los datasets (ejemplo para títulos de Amazon = **`as123`**)

+ Los valores nulos del campo rating deberán reemplazarse por el string “**`G`**” (corresponde al maturity rating: “general for all audiences”

+ De haber fechas, deberán tener el formato **`AAAA-mm-dd`**

+ Los campos de texto deberán estar en **minúsculas**, sin excepciones

+ El campo ***duration*** debe convertirse en dos campos: **`duration_int`** y **`duration_type`**. El primero será un integer y el segundo un string indicando la unidad de medición de duración: min (minutos) o season (temporadas)

<br/>

**`Desarrollo API`**:  Para disponibilizar los datos la empresa usa el framework ***FastAPI***. El analista de datos requiere consultar:

+ Cantidad de veces que aparece una keyword en el título de peliculas/series, por plataforma

+ Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año

+ La segunda película con mayor score para una plataforma determinada, según el orden alfabético de los títulos.

+ Película que más duró según año, plataforma y tipo de duración

+ Cantidad de series y películas por rating
<br/>


**`Deployment`**: La empresa suele usar [Deta](https://www.deta.sh/?ref=fastapi) (no necesita dockerizacion) para realizar el deploy de sus aplicaciones. Sin embargo, también puede usar [Railway](https://railway.app/) y [Render](https://render.com/docs/free#free-web-services) (necesitan dockerizacion).
<br/>

<br/>

**`Video`**: El Tech Lead que delegó esta tarea quiere dar un feedback sobre el trabajo realizado. Para esto, pide que sintetice en un video de ***5 minutos*** del trabajo realizado, resaltando cómo ayuda el mismo a los analistas de datos.
