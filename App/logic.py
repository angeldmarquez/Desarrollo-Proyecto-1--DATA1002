import pandas as pd
from tabulate import tabulate
import matplotlib.pyplot as plt

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
    df_bogota = df_mayores18[df_mayores18["P753S1"] == 11].copy()
    total_bogota18 = len(df_bogota)
    
    print("Reporte de los filtros")
    print(f"Total registros originales: {total_original}")
    print(f"Total de registros Mayores de 18 (P6040): {total_mayores18}")
    print(f"Total de registros mayores de 18 en Bogotá (P753S1): {total_bogota18}")

    return df_bogota

def tratar_valores_especiales(df):
    """
    Tratamiento de valores atípicos / códigos de no respuesta (ej. 99, 98).
    Convierte los códigos de 'No sabe' o 'No responde' en NaN para las variables 
    de bienestar, manteniendo intacto el puntaje 9 de la escala de satisfacción.
    """
    df_limpio = limpieza_datos(df)
    variables_bienestar = ["P1895", "P1896", "P1897", "P1898", "P1899", "P3175"]
    
    for var in variables_bienestar:
        if var in df_limpio.columns:
            df_limpio[var] = df_limpio[var].mask(df_limpio[var].isin([99, 98]))
            
    return df_limpio

def evaluar_valores_nulos (df):
    
    new_frame = tratar_valores_especiales(df)
    
    nulos_satisfaccion = new_frame["P1895"].isnull().sum()
    nulos_ingreso = new_frame["P1896"].isnull().sum()
    nulos_salud = new_frame["P1897"].isnull().sum()
    nulos_seguridad = new_frame["P1898"].isnull().sum()
    nulos_trabajo = new_frame["P1899"].isnull().sum()
    nulos_freetime = new_frame["P3175"].isnull().sum()
    
    total_registros = len(new_frame)
    
    porcentajes = [
        (nulos_satisfaccion * 100) / total_registros if total_registros > 0 else 0,
        (nulos_ingreso * 100) / total_registros if total_registros > 0 else 0,
        (nulos_salud * 100) / total_registros if total_registros > 0 else 0,
        (nulos_seguridad * 100) / total_registros if total_registros > 0 else 0,
        (nulos_trabajo * 100) / total_registros if total_registros > 0 else 0,
        (nulos_freetime * 100) / total_registros if total_registros > 0 else 0,
    ]
    
    datos = {
        "Datos Vacíos de Satisfacción General.": str(int(nulos_satisfaccion)),
        "Datos Vacíos de Ingreso.": str(int(nulos_ingreso)),
        "Datos Vacíos de la Salud." : str(int(nulos_salud)),
        "Datos Vacíos de Seguridad.": str(int(nulos_seguridad)),
        "Datos Vacíos del Trabajo.": str(int(nulos_trabajo)),
        "Datos Vacíos del Tiempo Libre.": str(int(nulos_freetime)),
        "Proporción de Vacíos en la Satisfacción General": f"{porcentajes[0]:.2f}%",
        "Proporción de Vacíos en el Ingreso.": f"{porcentajes[1]:.2f}%",
        "Proporción de Vacíos en la Salud.": f"{porcentajes[2]:.2f}%",
        "Proporción de Vacíos en la Seguridad.": f"{porcentajes[3]:.2f}%",
        "Proporción de Vacíos en el Trabajo.": f"{porcentajes[4]:.2f}%",
        "Proporción de Vacíos en el Tiempo Libre.": f"{porcentajes[5]:.2f}%"
    }
    
    filas = list(datos.items())
    
    return tabulate(filas, headers=["Métrica", "Valor"], tablefmt="simple")


def analisis_descriptivo(df):
    """
    Calcula estadísticos descriptivos y genera visualizaciones para las variables 
    de bienestar y demográficas de la población mayor de 18 años en Bogotá.
    """
    df_limpio = tratar_valores_especiales(df)
    
    variables_existentes = ["P6040", "P1895", "P1896", "P1897", "P1898", "P1899", "P3175"]
    
    print("RESUMEN ESTADÍSTICO (Media, Mediana, Mín, Máx, Desviación)")
    resumen = df_limpio[variables_existentes].describe()
    print(resumen)
    
    for cada_variable in variables_existentes:
        plt.figure(figsize=(8, 5))
        plt.hist(df_limpio[cada_variable].dropna(), bins=20, color="teal")
        plt.title(f"Distribución de la variable {cada_variable}")
        plt.xlabel(cada_variable)
        plt.ylabel("Frecuencia")
        plt.grid(True, linestyle="--", alpha=0.5)
        plt.savefig(f"histograma_{cada_variable}.png", bbox_inches='tight')
        plt.close()
        
    print("Gráficos de distribución generados.")
    return resumen


def analisis_exploratorio (df):
    df_limpio = tratar_valores_especiales(df)
    # unificado a las mismas 7 variables para mantener consistencia en todo el análisis
    variables_interes = ["P6040", "P1895", "P1896", "P1897", "P1898", "P1899", "P3175"]
    
    print("VALORES MÍNIMOS Y MÁXIMOS (Para detectar que valores atípicos tenemos o codigos de error")
    print(df_limpio[variables_interes].agg(['min', 'max']))
    
    print("MATRIZ DE CORRELACIÓN (Para ver posibles asociaciones de bienestar)")
    print(df_limpio[["P1895", "P1896", "P1897", "P1898", "P1899", "P3175"]].corr())