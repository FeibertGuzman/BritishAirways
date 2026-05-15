# ✈️ British Airways - Lounge Eligibility Model

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

Proyecto desarrollado para el **Programa de Data Science de Forage - British Airways**.

## 📖 Descripción
Este proyecto implementa una tabla de consulta para estimar los porcentajes de elegibilidad de pasajeros en las diferentes salas VIP (Lounges: Nivel 1, Nivel 2 y Nivel 3) de la Terminal 3 de Heathrow.

Dado que los calendarios de vuelos futuros son impredecibles, el modelo agrupa los vuelos a alto nivel basándose en el **Tipo de Ruta (HAUL)** y la **Hora del Día (TIME_OF_DAY)** en lugar de vuelo por vuelo. Esto hace que el modelo sea flexible y fácil de aplicar a nuevos itinerarios.

## 🗂 Estructura del Proyecto
- `data_processing.py`: Script de Python que lee los datos originales, los agrupa, calcula los porcentajes de elegibilidad y llena automáticamente el archivo de Excel requerido por Forage.
- `Filled_Lounge_Eligibility_Lookup.xlsx`: Excel resultante con los datos agrupados y las justificaciones del modelo.
- `app.py`: Dashboard interactivo desarrollado en **Streamlit** para explorar los resultados del modelo.
- `index.html`: Landing page moderna y responsive lista para ser desplegada en **GitHub Pages**.
- `tutorial.md`: Documento paso a paso que explica toda la lógica y la metodología aplicada.

## 🚀 Instalación y Despliegue

### Requisitos previos
Instalar las dependencias de Python:
```bash
pip install -r requirements.txt
```

### 1. Ejecutar Procesamiento de Datos
Genera el dataset consolidado (`processed_lounge_data.csv`) y el Excel final:
```bash
python data_processing.py
```

### 2. Despliegue del Dashboard Local
Inicia la aplicación en Streamlit para visualizar gráficos y KPIs:
```bash
streamlit run app.py
```

### 3. GitHub Pages (Landing Page)
Simplemente sube el archivo `index.html` a un repositorio público en GitHub, ve a **Settings > Pages** y despliega desde la rama `main` en el directorio root (`/`).

---
**Autor:** Desarrollado como parte de la simulación de empleo +EDU para Feibert Guzmán.
