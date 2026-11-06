Markdown

# 🎮 Proyecto EDA: Análisis del Mercado Global de Videojuegos

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Testing](https://img.shields.io/badge/testing-Pytest-yellow.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#)

Proyecto de **Análisis Exploratorio de Datos (EDA)** y arquitectura modular en Python enfocado en el dataset histórico de ventas globales de videojuegos de Kaggle. El proyecto abarca desde la exploración estadística y tratamiento de anomalías hasta la implementación de pruebas unitarias (`pytest`), un pipeline automatizado reproducible y un tablero interactivo ejecutivo (`Streamlit`).

---

## 📌 1. Origen y Estructura de los Datos

Los datos analizados proceden del repositorio público de **Kaggle**:
* **Fuente original:** [Video Game Sales Dataset (Kaggle)](https://www.kaggle.com/datasets/gregorut/videogamesales)
* **Archivo fuente local:** `dato.csv`
* **Archivo optimizado en producción:** `dato_cleaned.csv`

### Diccionario de Datos Principal
| Variable | Descripción | Tipo de Dato |
| :--- | :--- | :--- |
| `Platform` | Consola o plataforma de lanzamiento (ej. PS2, X360, Wii) | Categórico |
| `Genre` | Género del videojuego (ej. Action, Sports, RPG) | Categórico |
| `Publisher` | Empresa editora / distribuidora | Categórico |
| `NA_Sales` | Ventas acumuladas en Norteamérica (en millones de unidades) | Numérico (`float32`) |
| `EU_Sales` | Ventas acumuladas en Europa (en millones de unidades) | Numérico (`float32`) |
| `JP_Sales` | Ventas acumuladas en Japón (en millones de unidades) | Numérico (`float32`) |
| `Other_Sales` | Ventas acumuladas en el resto del mundo (en millones) | Numérico (`float32`) |
| `Global_Sales` | Facturación global total acumulada (en millones de unidades) | Numérico (`float32`) |

---

## 🎯 2. Hallazgos Principales del EDA

* **Dominio Occidental:** Los mercados de Norteamérica (`NA_Sales`) y Europa (`EU_Sales`) representan de forma conjunta más del **65% al 70%** del volumen global de facturación en títulos de alto rendimiento (*Blockbusters*).
* **Comportamiento Asimétrico de Japón:** Mientras que el mercado occidental consume predominantemente géneros de **Acción, Deportes y Shooters**, el mercado japonés (`JP_Sales`) muestra preferencia líder por el género **Role-Playing (RPG)**, operando de forma independiente al resto de regiones.
* **Segmentación de Mercado (Plataformas):** Se identificaron 3 niveles estratégicos de plataformas (*Tiers*) basados en volumen histórico acumulado, destacando a consolas como PS2, X360, PS3 y Wii en el *Tier 1 (Leaders)*.

---

## 🏗️ 3. Estructura del Repositorio

```text
EDA-VideoGames-Analysis/
│
├── dato.csv                    # Dataset original sin procesar
├── dato_cleaned.csv            # Dataset limpio y optimizado generado por pipeline.py
├── 01_eda_videojuegos.ipynb    # Cuaderno Jupyter/Colab con la exploración completa (Niveles Esencial-Experto)
├── pipeline.py                 # Pipeline ejecutable de limpieza y optimización de datos
├── test_pipeline.py            # Batería de pruebas unitarias desarrolladas con pytest
├── app.py                      # Dashboard ejecutivo interactivo maquetado en Streamlit
└── README.md                   # Documentación principal del repositorio

🛠️ 4. Requisitos e Instalación
Requisitos Previos

    Python 3.8+

    Visual Studio Code o Google Colab

1. Clonar el Repositorio

Abre tu terminal e ingresa el siguiente comando para clonar el repositorio de la organización:
Bash

git clone [https://github.com/IA-P1-BCN/EDA-VideoGames-Analysis.git](https://github.com/IA-P1-BCN/EDA-VideoGames-Analysis.git)
cd EDA-VideoGames-Analysis

2. Creación de Entorno Virtual (Opcional pero recomendado)
PowerShell

# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual en Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activar en macOS / Linux
source venv/bin/activate

3. Instalar Dependencias

Instala todas las librerías necesarias invocando directamente a Python para evitar errores de PATH en Windows:
PowerShell

python -m pip install pandas numpy matplotlib seaborn scikit-learn pytest streamlit

🚀 5. Guía de Ejecución
A. Exploración del Cuaderno Jupyter (01_eda_videojuegos.ipynb)

Para revisar todo el análisis interactivo, gráficos e interpretaciones estadísticas:

    Abre Visual Studio Code.

    Abre el archivo 01_eda_videojuegos.ipynb.

    Selecciona tu Kernel de Python y presiona Run All (o ejecútalo directamente subiéndolo a Google Colab).

B. Ejecución de Pruebas Unitarias (pytest)

Para validar los criterios de calidad y limpieza del pipeline de datos bajo metodología TDD:
PowerShell

python -m pytest test_pipeline.py

C. Ejecución del Pipeline Reproducible (pipeline.py)

Para procesar el archivo original y generar el dataset optimizado dato_cleaned.csv:
PowerShell

python pipeline.py

D. Lanzamiento del Dashboard Interactivo (app.py)

Para abrir el cuadro de mando ejecutivo en el navegador web local:
PowerShell

python -m streamlit run app.py

Se desplegará automáticamente la interfaz web interactiva en http://localhost:8501.
📋 6. Informe de Calidad de Datos (Data Quality Report)

    Tratamiento de Nulos: Remoción de registros sin editor (Publisher) identificado para evitar distorsiones estadísticas en análisis bivariados.

    Corrección de Formato: Conversión de coma decimal a punto en columnas numéricas y ajuste a flotantes de 32 bits (float32).

    Optimización de Memoria: Reducción del consumo de memoria RAM en más de un 40% mediante conversión categórica de variables de texto repetitivas y downcasting de enteros/flotantes.