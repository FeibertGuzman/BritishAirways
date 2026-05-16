# 📊 Curso SCORM: Visualización de Datos con Python + Streamlit

![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)

Bienvenido al módulo interactivo de **Visualización de Datos**. Este proyecto es un curso empaquetado compatible con el estándar SCORM 1.2, diseñado para enseñar desde los fundamentos de la visualización en Python hasta la creación de dashboards interactivos y profesionales usando Streamlit.

## 📖 Contenido del Curso
El curso interactivo está estructurado en módulos, una evaluación final y certificación:

### Módulo 1: Fundamentos
- **Introducción a la Visualización**: Conceptos clave, y los diferentes tipos de gráficos según su propósito.
- **Python para Visualización**: Exploración del ecosistema con bibliotecas base.
- **Matplotlib**: Estructura de la biblioteca base de gráficos estáticos y personalización.
- **Seaborn**: Visualización estadística atractiva e identificación de patrones y correlaciones.
- **Plotly**: Creación de gráficos dinámicos con interactividad nativa (zoom, animaciones, etc).

### Módulo 2: Streamlit
- **Introducción a Streamlit**: Construcción de interfaces web de datos únicamente con Python.
- **Componentes**: Uso de widgets interactivos (sliders, inputs) y organización de layouts (columnas, tabs).
- **Gráficos en Streamlit**: Integración perfecta con Matplotlib, Plotly y bibliotecas interactivas nativas.
- **Dashboard Completo**: Proyecto integrador con estructura modular y filtrado dinámico.

### Evaluación y Certificación
- **Quiz Final**: 10 preguntas interactivas para evaluar los conocimientos adquiridos. (Puntaje mínimo aprobatorio: 70%).
- **Certificado de Finalización**: Generación de certificado personalizado tras superar la evaluación.

## 🚀 Ejecución y Uso

Dado que este curso es un paquete interactivo front-end (con API SCORM 1.2 integrada para progreso de lecciones y quiz), todo funciona localmente sin dependencias de servidor. Solo necesitas abrir el archivo `index.html`.

### Despliegue Local
1. Navega a la carpeta del módulo:
```bash
cd "Visualizacion de datos"
```
2. Abre el archivo en tu navegador web de preferencia. Si estás en Windows puedes usar:
```bash
start index.html
```

## 🛠️ Tecnologías y Diseño de la Plataforma
- **Diseño UI/UX:** Interfaz gráfica elegante con animaciones suaves, barras laterales responsivas y paletas de colores corporativas. 
- **Lógica Frontend:** Manipulación dinámica del DOM con JavaScript puro para las transiciones de diapositivas, validación de quizzes, estado de avance (barra de progreso) y recolección de puntajes SCORM.
- **Integración SCORM:** Incluye las funciones `LMSInitialize`, `LMSSetValue`, `LMSCommit` y `LMSFinish` para llevar persistencia del estado en un LMS o usando *localStorage*.

---
**Realizado por:** Feibert Guzmán  
