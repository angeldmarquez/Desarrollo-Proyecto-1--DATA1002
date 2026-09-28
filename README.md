# Desarrollo-Proyecto-1--DATA1002

# Proyecto 1: Análisis de Bienestar en la Población Adulta de Bogotá D.C.

**Asignatura:** Aplicaciones en Ciencia de Datos (DATA-1002)  
**Institución:** Universidad de los Andes

## Integrantes del Grupo
* Diego Alejandro Bayona Vergara (202416663)
* Juan Lesmes (202614029)
* Juan Sebastián Barragán Luque (202425898)
* Ángel Daniel Márquez Velasco (202616507)

---

## Descripción del Proyecto
Este proyecto de consultoría en Ciencia de Datos tiene como objetivo analizar las condiciones de vida y el bienestar subjetivo de la población adulta residente en Bogotá D.C., utilizando como fuente de datos la tabla de **"Características y composición del hogar"** de la **Encuesta Nacional de Calidad de Vida (ECV) 2025** realizada por el DANE. El desarrollo sigue las etapas iniciales de la metodología CRISP-DM para formular preguntas analíticas, preparar los datos (ETL), realizar análisis descriptivos y exploratorios, y extraer hallazgos clave para orientar posibles acciones de política pública.

---

## Pregunta Analítica
> *"En una escala de 0 a 10, ¿qué tan satisfechas se sienten las personas mayores de 18 años en Bogotá con respecto a su salud, ingreso, seguridad, trabajo y tiempo libre, y cuáles de estos aspectos tienen mayor peso sobre su satisfacción general con la vida?"*

---

## Estructura del Repositorio
El código fuente del proyecto se encuentra dividido en dos archivos principales:
1. **`App/logic.py`**: Contiene la lógica, funciones de carga, filtros de limpieza ETL, tratamiento de valores especiales, evaluación de nulos y generación de estadísticos y gráficos.
2. **`App/view.py`**: Interfaz de ejecución principal que coordina el flujo del programa e imprime los reportes en consola.
3. **`Data/Características y composición del hogar.csv`**: Archivo de datos fuente de la ECV 2025 del DANE.

---

## Requisitos e Instalación
Es importante tener instalado Python y las siguientes librerías requeridas para ejecutar el proyecto:
    1. pandas 
    2. tabulate 
    3. matplotlib