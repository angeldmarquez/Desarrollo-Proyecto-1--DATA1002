# ==========================================
# VISTA PRINCIPAL (view.py)
# ==========================================

from logic import cargar_datos
from logic import limpieza_datos
from logic import evaluar_valores_nulos
from logic import analisis_descriptivo
from logic import analisis_exploratorio

print("==================================================")
print("PROYECTO 1: ANALISIS DE BIENESTAR EN BOGOTA")
print("==================================================")

# Ruta del archivo CSV
archivo = "Características y composición del hogar.csv"

# ----------------------------------------------------
# PASO 1: Carga de datos
# ----------------------------------------------------
print("")
print("PASO 1: Cargando la base de datos...")
df_original = cargar_datos(archivo)
print("Datos cargados correctamente.")

# ----------------------------------------------------
# PASO 2: Limpieza y Filtrado de Datos
# ----------------------------------------------------
print("")
print("PASO 2: Aplicando filtros de edad y ciudad...")
df_limpio = limpieza_datos(df_original)
print("Filtrado completado.")

# ----------------------------------------------------
# PASO 3: Evaluación de Valores Nulos
# ----------------------------------------------------
print("")
print("PASO 3: Evaluando valores nulos y vacios...")
diccionario_nulos = evaluar_valores_nulos(df_original)

# Imprimir el diccionario paso a paso de forma muy sencilla
for clave in diccionario_nulos:
    valor = diccionario_nulos[clave]
    print(clave, ":", valor)

# ----------------------------------------------------
# PASO 4: Análisis Descriptivo (Estadísticos y Gráficos)
# ----------------------------------------------------
print("")
print("PASO 4: Realizando analisis descriptivo y graficos...")
resumen_estadistico = analisis_descriptivo(df_original)
print(resumen_estadistico)

# ----------------------------------------------------
# PASO 5: Análisis Exploratorio (Atípicos y Correlaciones)
# ----------------------------------------------------
print("")
print("PASO 5: Analizando valores atipicos y correlaciones...")
analisis_exploratorio(df_original)

print("")
print("==================================================")
print("PROGRAMA FINALIZADO CON EXITO")
print("==================================================")