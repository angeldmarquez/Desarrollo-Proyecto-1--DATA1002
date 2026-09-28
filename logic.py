import pandas as pd
from tabulate import tabulate
df = pd.read_csv("Características y composición del hogar.csv", sep= ";")

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

def cada_variable(df):
    new_frame = limpieza_datos(df)
    
    nulos_satisfaccion = new_frame["P1895"].isnull().sum()
    nulos_ingreso = new_frame["P1896"].isnull().sum()
    nulos_seguridad = new_frame["P1898"].isnull().sum()
    nulos_freetime = new_frame["P3175"].isnull().sum()
    nulos_trabajo = new_frame["P1899"].isnull().sum()
    nulos_salud = new_frame["P1897"].isnull().sum()
    
    porcentajes = [
        (nulos_satisfaccion*100)/len(new_frame["P1895"]),
        (nulos_ingreso*100)/len(new_frame["P1896"]),
        (nulos_seguridad*100)/len(new_frame["P1898"]),
        (nulos_freetime*100)/len(new_frame["P3175"]),
        (nulos_trabajo*100)/len(new_frame["P1899"]),
        (nulos_salud*100)/len(new_frame["P1897"]),
    ]
    
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
    filas = datos.items()

    return tabulate(filas, headers=["Métrica", "Valor"], tablefmt="simple")

print(cada_variable(df))