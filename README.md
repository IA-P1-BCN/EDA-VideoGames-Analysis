# 🎮 Proyecto EDA: Análisis del Mercado Global de Videojuegos

[![Python Version](https://img.shields.io/badge/python-3.8%2B-blue.svg)](https://www.python.org/)
[![Framework](https://img.shields.io/badge/framework-Streamlit-FF4B4B.svg)](https://streamlit.io/)
[![Testing](https://img.shields.io/badge/testing-Pytest-yellow.svg)](https://docs.pytest.org/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](#)

Proyecto de **Análisis Exploratorio de Datos (EDA)** y arquitectura modular en Python enfocado en el dataset histórico de ventas globales de videojuegos de Kaggle. El proyecto abarca desde la exploración estadística y tratamiento de anomalías hasta la implementación de pruebas unitarias (`pytest`), un pipeline automatizado reproducible y un tablero interactivo ejecutivo (`Streamlit`).

📄 **[Informe ejecutivo (PDF, 2 páginas) →](INFORME_INVESTIGACION_EDA.pdf)** · 📝 **[Informe completo de investigación (Markdown) →](INFORME_INVESTIGACION_EDA.md)**

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
| `Other_Sales` | Ventas acumuladas en el resto del mundo (en millones de unidades) | Numérico (`float32`) |
| `Global_Sales` | Ventas globales acumuladas (en millones de unidades) | Numérico (`float32`) |

> Las cifras del proyecto expresan **unidades físicas vendidas**, no facturación económica.

---

## 🎯 2. Hallazgos Principales del EDA

* **Mercado occidental concentrado:** Norteamérica (`NA_Sales`) y Europa (`EU_Sales`) suman de forma agregada el **81.2%** del volumen global de unidades; la correlación entre ambos mercados es fuerte (`r = 0.8382`).
* **Comportamiento asimétrico de Japón:** Mientras que el mercado occidental consume predominantemente géneros de **Acción, Deportes y Shooters**, el mercado japonés (`JP_Sales`) muestra preferencia líder por el género **Role-Playing (RPG)**, con correlaciones moderadas con occidente (r ≈ 0.47–0.52).
* **Mercado concentrado en pocos títulos:** El 9.9% del catálogo supera el límite IQR (≈ 1.71 M de unidades) y acumula el **54.5% del volumen total**; la mediana por título (0.29 M) queda muy por debajo de la media (0.77 M).
* **Segmentación de plataformas:** Los cuatro sistemas líderes (PS2, X360, PS3, Wii) concentran el **60.7%** del volumen histórico acumulado.

---

## 🏗️ 3. Estructura del Repositorio

```text
EDA-VideoGames-Analysis/
│
├── dato.csv                        # Dataset original sin procesar
├── dato_cleaned.csv                # Dataset limpio y optimizado generado por pipeline.py
├── 01_eda_videojuegos.ipynb        # Notebook con la exploración completa y las visualizaciones
├── pipeline.py                     # Pipeline ejecutable de limpieza y optimización de datos
├── test_pipeline.py                # Batería de pruebas unitarias desarrolladas con pytest
├── app.py                          # Dashboard ejecutivo interactivo maquetado en Streamlit
├── INFORME_INVESTIGACION_EDA.pdf   # Informe ejecutivo (PDF editorial, 2 páginas)
├── INFORME_INVESTIGACION_EDA.md    # Informe de investigación completo (fuente editable)
├── assets/
│   └── figures/                    # Figuras exportadas del notebook (citadas en el informe)
├── requirements.txt                # Dependencias del proyecto
└── README.md                       # Documentación principal del repositorio
```

---

## 🛠️ 4. Requisitos e Instalación

### Requisitos Previos
* Python 3.8+
* Visual Studio Code o Google Colab

### 1. Clonar el Repositorio

Abre tu terminal e ingresa el siguiente comando para clonar el repositorio de la organización:

```bash
git clone https://github.com/IA-P1-BCN/EDA-VideoGames-Analysis.git
cd EDA-VideoGames-Analysis
```

### 2. Creación de Entorno Virtual (Opcional pero recomendado)

```powershell
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual en Windows (PowerShell)
.\venv\Scripts\Activate.ps1

# Activar en macOS / Linux
source venv/bin/activate
```

### 3. Instalar Dependencias

Instala todas las librerías necesarias invocando directamente a Python para evitar errores de PATH en Windows:

```powershell
python -m pip install -r requirements.txt
```

---

## 🚀 5. Guía de Ejecución

### A. Exploración del Cuaderno Jupyter (`01_eda_videojuegos.ipynb`)

Para revisar todo el análisis interactivo, gráficos e interpretaciones estadísticas:

1. Abre Visual Studio Code.
2. Abre el archivo `01_eda_videojuegos.ipynb`.
3. Selecciona tu Kernel de Python y presiona **Run All** (o ejecútalo directamente en Google Colab).

### B. Ejecución de Pruebas Unitarias (`pytest`)

Para validar los criterios de calidad y limpieza del pipeline de datos bajo metodología TDD (3 pruebas unitarias):

```powershell
python -m pytest test_pipeline.py -v
```

### C. Ejecución del Pipeline Reproducible (`pipeline.py`)

Para procesar el archivo original y generar el dataset optimizado `dato_cleaned.csv`:

```powershell
python pipeline.py
```

### D. Lanzamiento del Dashboard Interactivo (`app.py`)

Para abrir el cuadro de mando ejecutivo en el navegador web local:

```powershell
python -m streamlit run app.py
```

Se desplegará automáticamente la interfaz web interactiva en `http://localhost:8501`.

---

## 📋 6. Informe de Calidad de Datos (Data Quality Report)

* **Tratamiento de Nulos:** El filtrado de registros sin editor (`Publisher`) se mantiene como salvaguarda preventiva del pipeline; el dataset actual **no contiene valores nulos** en esta columna.
* **Eliminación de Duplicados:** Se eliminan los registros duplicados exactos (**24 en el dataset actual**), reduciendo el catálogo de 7,112 a 7,088 títulos.
* **Corrección de Formato:** Conversión de coma decimal a punto en columnas numéricas y ajuste a flotantes de 32 bits (`float32`).
* **Optimización de Memoria:** Reducción del consumo de memoria en ejecución de **0.87 MB a 0.42 MB (≈ 52%)** mediante conversión categórica de variables de texto repetitivas y downcasting de flotantes.

---

## 📄 7. Documentación Ampliada

* **[Informe ejecutivo en PDF](INFORME_INVESTIGACION_EDA.pdf)** — versión editorial de 2 páginas, pensada para público no técnico.
* **[Informe de investigación en Markdown](INFORME_INVESTIGACION_EDA.md)** — fuente editable con el desarrollo metodológico completo: verificación de cifras, limitaciones del dataset, análisis regional detallado y conclusiones con sus interpretaciones.
