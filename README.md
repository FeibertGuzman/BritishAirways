# ✈️ British Airways - Lounge Eligibility Model

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)

Proyecto desarrollado para el **Programa de Simulación de Data Science de Forage - British Airways**.

## 📖 Resumen Ejecutivo
Este proyecto proporciona una solución analítica escalable para estimar la demanda en las salas VIP (Lounges: Nivel 1 Concorde, Nivel 2 First y Nivel 3 Club) de la Terminal 3 de Heathrow.

A través de un enfoque de agrupamiento estratégico basado en el **Alcance de Ruta (HAUL)** y el **Momento del Día (TIME_OF_DAY)**, el modelo puede proyectar métricas precisas para la demanda de pasajeros, superando las limitaciones de depender de calendarios de vuelo estáticos e impredecibles.

## 🗂 Estructura del Repositorio
* `data_processing.py`: Pipeline automatizado para la limpieza de datos, la agrupación y la inferencia del modelo que diligencia automáticamente las plantillas.
* `Filled_Lounge_Eligibility_Lookup.xlsx`: El reporte analítico generado automáticamente para el departamento de planificación.
* `app.py`: Un dashboard moderno e interactivo construido en **Streamlit** que expone el resumen métrico, incorpora filtrado dinámico de datos y previsualiza los reportes generados.
* `index.html`: Landing page corporativa que presenta el modelo de forma elegante y está diseñada para **GitHub Pages**.
* `tutorial.md`: Documentación exhaustiva que desglosa el marco metodológico y lógico del proyecto.

## 🚀 Guía de Instalación y Despliegue

### 1. Clonar el Repositorio
Para obtener una copia local de este proyecto, ejecuta el siguiente comando en tu terminal:

```bash
git clone https://github.com/FeibertGuzman/BritishAirways.git
cd BritishAirways
```

### 2. Configurar Entorno
Se recomienda el uso de un entorno virtual. Luego, instala las dependencias necesarias:

```bash
pip install -r requirements.txt
```

### 3. Ejecutar Procesamiento (ETL)
Genera el reporte consolidado y procesa la data para su uso en la aplicación:

```bash
python data_processing.py
```

### 4. Lanzar el Dashboard (Streamlit)
Inicia la herramienta de inteligencia de negocios para explorar los datos interactivos:

```bash
streamlit run app.py
```

### 5. Despliegue Web Estático
La página `index.html` sirve como portal público del proyecto y puede alojarse directamente en **GitHub Pages** seleccionando la rama `main` desde el menú de *Settings*.

---
**Desarrollador:** Feibert Guzmán  
*Proyecto implementado como evidencia para la plataforma +EDU.*
