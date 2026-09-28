import pandas as pd

def cargar_datos (filepath):
    """ Paso 1: Leer el archivo CSV. """
    print("Cargando datos...")
    df = pd.read_csv(filepath, sep= ";")
    return df

def limpieza_datos(df):
    """ Paso 2: En esta funcion limpiaremos los datos del dataframe, ya que nuestro trabajo 
    esta orientado a personas de 18 o mas y que hayan vivido en Bogota en los ultimos 12 meses.
    Args:
        df (Dataframe) -> El archivo csv original
    Return 
        df (Dataframe) -> El Dataframe ya limpio con las variables a trabajar.
    """
    total_original = len(df)
    
    # 3. Filtrar por personas de 18 años o más, la variable p6040 se refiere a los años cumplidos de cada individuo
    df_mayores18 = df[df["P6040"] >= 18]
    total_mayores18 = len(df_mayores18)

    # 4. Filtrar por personas que vivieron en Bogotá en los últimos 12 meses
    # La variable P753S1 indica en que departamento vivio en los ultimos 12 meses, el codigo 11 del "divipola" indica a bogota
    df_bogota = df_mayores18[df_mayores18["P753S1"] == 11]
    total_bogota18 = len(df_bogota)
    
    print("Reporte de los filtros")
    print(f"Total registros originales: {total_original}")
    print(f"Total de registros Mayores de 18 (P6040): {total_mayores18}")
    print(f"Total de registros mayores de 18 en Bogotá (P753S1): {total_bogota18}")

    return df_bogota

def evaluar_valores_nulos (df):
    
    # Obtenemos el DataFrame limpio llamando a la función anterior
    
    new_frame = limpieza_datos(df)
    
    # Conteo de valores nulos (.isnull().sum()) para cada variable de bienestar
    
    nulos_satisfaccion = new_frame["P1895"].isnull().sum()
    nulos_ingreso = new_frame["P1896"].isnull().sum()
    nulos_seguridad = new_frame["P1898"].isnull().sum()
    nulos_freetime = new_frame["P3175"].isnull().sum()
    nulos_trabajo = new_frame["P1899"].isnull().sum()
    nulos_salud = new_frame["P1897"].isnull().sum()
    
    # Cálculo de los porcentajes de valores vacíos respecto al total de registros limpios
    
    porcentajes = [
        (nulos_satisfaccion*100)/len(new_frame["P1895"]),
        (nulos_ingreso*100)/len(new_frame["P1896"]),
        (nulos_seguridad*100)/len(new_frame["P1898"]),
        (nulos_freetime*100)/len(new_frame["P3175"]),
        (nulos_trabajo*100)/len(new_frame["P1899"]),
        (nulos_salud*100)/len(new_frame["P1897"]),
    ]
    
    # Diccionario estructurado que almacena de forma organizada los conteos y proporciones
    datos = {
        "Datos Vacíos de Satisfacción General.": str(int(nulos_satisfaccion)),
        "Datos Vacíos de Ingreso.": str(int(nulos_ingreso)),
        "Datos Vacíos de Seguridad.": str(int(nulos_seguridad)),
        "Datos Vacíos del Tiempo Libre.": str(int(nulos_freetime)),
        "Datos Vacíos del Trabajo.": str(int(nulos_trabajo)),
        "Datos Vacíos de la Salud." : str(int(nulos_salud)),
        "Proporción de Vacíos en la Satisfacción General": str(float(porcentajes[0])),
        "Proporción de Vacíos en el Ingreso.": str(float(porcentajes[1])),
        "Proporción de Vacíos en la Seguridad.": str(float(porcentajes[2])),
        "Proporción de Vacíos en el Tiempo Libre.": str(float(porcentajes[3])),
        "Proporción de Vacíos en el Trabajo.": str(float(porcentajes[4])),
        "Proporción de Vacíos en la Salud.": str(float(porcentajes[5]))
    }
    
    return datos

import matplotlib.pyplot as plt
import seaborn as sns

def analisis_descriptivo(df):
    """
    Calcula estadísticos descriptivos y genera visualizaciones para las variables 
    de bienestar y demográficas de la población mayor de 18 años en Bogotá.
    """
    df_limpio = limpieza_datos(df)
    
    # Definimos directamente las variables existentes
    variables_existentes = ["P6040", "P1895", "P1896", "P1897", "P1898", "P1899", "P3175"]
    
    print("\n--- RESUMEN ESTADÍSTICO (Media, Mediana, Mín, Máx, Desviación) ---")
    resumen = df_limpio[variables_existentes].describe()
    print(resumen)
    
    # Generación y guardado de histogramas con KDE para análisis visual
    for var in variables_existentes:
        plt.figure(figsize=(8, 5))
        sns.histplot(df_limpio[var].dropna(), kde=True, bins=20, color="teal")
        plt.title(f"Distribución de la variable {var}")
        plt.xlabel(var)
        plt.ylabel("Frecuencia")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.savefig(f"histograma_{var}.png", bbox_inches='tight')
        plt.close()
        
    print("Gráficos de distribución generados.")
    return resumen


def analisis_exploratorio (df):
    df_limpio = limpieza_datos(df)
    variables_interes = ["P6040", "P1895", "P1896", "P1897", "P1898"]
    
    print("VALORES MÍNIMOS Y MÁXIMOS (Para detectar que valores atípicos tenemos o codigos de error")
    print(df_limpio[variables_interes].agg(['min', 'max']))
    
    print("MATRIZ DE CORRELACIÓN (Para ver posibles asociaciones de bienestar)")
    print(df_limpio[["P1895", "P1896", "P1897", "P1898"]].corr())