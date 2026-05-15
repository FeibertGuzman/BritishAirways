# 📘 Tutorial de Aprendizaje: Análisis de Elegibilidad de Salas VIP

¡Hola! Si estás revisando este documento, es porque estás interesado en aprender no solo **qué** se hizo, sino **por qué** y **cómo** se programó cada parte de la solución para la simulación de Data Science de British Airways (Forage). 

Este tutorial está diseñado paso a paso para estudiantes.

---

## 🧠 1. Comprendiendo el Problema de Negocio

### El Reto
British Airways (BA) necesita proyectar cuántas personas entrarán a sus Salas VIP (Lounges) en la Terminal 3 de Heathrow. Los niveles de salas son:
- **Nivel 1 (Concorde):** Muy exclusivos, pasajeros VIP o de First Class.
- **Nivel 2 (First):** Pasajeros de primera clase o con estatus muy alto.
- **Nivel 3 (Club):** Pasajeros de Business Class o viajeros frecuentes regulares.

### El Problema
Si calculamos la demanda basándonos en números de vuelo específicos (Ej. "Vuelo BA123 tendrá 10 pasajeros"), nuestro modelo **no será escalable**. Si mañana BA cambia los números de vuelo o agrega nuevas rutas, el modelo se rompe. 

### La Decisión (El "Por Qué")
Decidimos que la mejor forma de predecir la demanda es usando **agrupaciones a alto nivel**. Elegimos dos variables presentes en el dataset:
1. **`HAUL` (Tipo de Ruta):** Diferencia si el vuelo es de corto alcance (Europa) o de largo alcance (Intercontinental). *Razón:* Los vuelos intercontinentales suelen llevar aeronaves más grandes y vender más asientos Premium.
2. **`TIME_OF_DAY` (Hora del Día):** Mañana, Tarde, Noche. *Razón:* Los viajeros de negocios (que suelen tener acceso a salas VIP) viajan en horarios pico muy marcados.

---

## ⚙️ 2. Lógica de Procesamiento de Datos (Pandas)

Para diligenciar el archivo Excel que Forage nos pedía, tuvimos que transformar la base de datos original. 

### ¿Cómo lo hicimos en código?
Aunque el script original lo integramos y ejecutamos para ti, la lógica matemática detrás fue la siguiente, utilizando la librería `pandas` de Python:

```python
import pandas as pd

# 1. Leer el archivo Excel original
df = pd.read_excel('British Airways Summer Schedule Dataset.xlsx')

# 2. Calcular el total real de pasajeros
# Sumamos las sillas de las 3 clases para saber la capacidad total del avión
df['TOTAL_PAX'] = df['FIRST_CLASS_SEATS'] + df['BUSINESS_CLASS_SEATS'] + df['ECONOMY_SEATS']

# 3. Agrupación Matemática (El corazón del algoritmo)
# Usamos .groupby() para juntar todos los vuelos que comparten el mismo HAUL y TIME_OF_DAY.
# .agg() nos permite sumar cuántos pasajeros en total de Nivel 1, 2 y 3 hubo en ese grupo.
grouped = df.groupby(['HAUL', 'TIME_OF_DAY']).agg({
    'TOTAL_PAX': 'sum',
    'TIER1_ELIGIBLE_PAX': 'sum',
    'TIER2_ELIGIBLE_PAX': 'sum',
    'TIER3_ELIGIBLE_PAX': 'sum'
}).reset_index()

# 4. Cálculo de Porcentajes
# Si de 1000 pasajeros totales en "Largo Alcance - Mañana", 50 entran al Nivel 1,
# la probabilidad/porcentaje es 50 / 1000 = 0.05 (5%).
grouped['Nivel 1 %'] = grouped['TIER1_ELIGIBLE_PAX'] / grouped['TOTAL_PAX']
grouped['Nivel 2 %'] = grouped['TIER2_ELIGIBLE_PAX'] / grouped['TOTAL_PAX']
grouped['Nivel 3 %'] = grouped['TIER3_ELIGIBLE_PAX'] / grouped['TOTAL_PAX']
```

> **Lección Clave:** Al agrupar, redujimos miles de filas de vuelos individuales a unas pocas filas genéricas. Si en el futuro BA suma 10 vuelos nuevos en la mañana de largo alcance, simplemente multiplicamos los pasajeros de esos vuelos por estos porcentajes descubiertos. ¡Eso es escalabilidad!

---

## 📊 3. Explicación a Detalle de la Aplicación (`app.py`)

Para presentar los resultados a los directivos, construimos una aplicación interactiva usando la librería **Streamlit**. Streamlit permite crear interfaces web directamente desde Python sin necesidad de saber React o Angular.

Abramos `app.py` y veamos bloque por bloque:

### Bloque A: Configuración y Diseño
```python
import streamlit as st
import pandas as pd
import plotly.express as px

# Aquí le decimos a Streamlit cómo se llama la pestaña del navegador y que use todo el ancho de pantalla.
st.set_page_config(page_title="Lounge Eligibility Dashboard", page_icon="✈️", layout="wide")

# Usamos HTML y CSS inyectado para cambiar colores (como el color de fondo y textos) y hacerlo lucir corporativo.
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    h1 { color: #0b2545; }
    </style>
""", unsafe_allow_html=True)
```

### Bloque B: Carga Optimizada de Datos
```python
# @st.cache_data es un "decorador". Le dice a Streamlit: "Guarda estos datos en la memoria RAM".
# Así, si el usuario hace clic en un botón, la app no vuelve a leer el archivo CSV desde cero, haciéndola rapidísima.
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed_lounge_data.csv')
    return df

df = load_data()
```

### Bloque C: Creación de Tarjetas de Resumen (KPIs)
```python
# Dividimos la pantalla en 4 columnas invisibles
col1, col2, col3, col4 = st.columns(4)

# metric() crea una tarjeta de KPI grande. Aquí usamos .sum() para sumar la columna entera del Dataframe.
col1.metric("Total Pasajeros", f"{df['TOTAL_PAX'].sum():,.0f}")
```

### Bloque D: Gráficos con Plotly
Usamos `plotly.express` porque genera gráficos donde puedes pasar el ratón por encima (hover) e interactuar, a diferencia de gráficas estáticas.

```python
# 1. Transformación de datos (Melt)
# pd.melt() "aplasta" las columnas TIER1, TIER2 y TIER3 en una sola columna llamada 'Tier' y sus valores en 'Passengers'.
# Esto es obligatorio para que Plotly entienda cómo hacer un gráfico de barras apilado o agrupado por colores.
melted_df = df.melt(id_vars=['HAUL', 'TIME_OF_DAY'], value_vars=['TIER1_ELIGIBLE_PAX', 'TIER2_ELIGIBLE_PAX', 'TIER3_ELIGIBLE_PAX'], var_name='Tier', value_name='Passengers')

# 2. Creación del gráfico
# facet_col='TIME_OF_DAY' le dice a Plotly que haga un mini-gráfico separado para cada momento del día.
fig_bar = px.bar(melted_df, x='HAUL', y='Passengers', color='Tier', barmode='group', facet_col='TIME_OF_DAY')
st.plotly_chart(fig_bar, use_container_width=True)
```

---

## 🌐 4. La Landing Page (Frontend Puro)

Además del Dashboard en Python, creamos una **Landing Page** (`public/index.html`) usando HTML y CSS puros. 

¿Por qué HTML puro? 
Porque herramientas como **GitHub Pages** alojan archivos HTML estáticos de forma 100% gratuita y sin necesidad de configurar servidores de bases de datos. 

Si abres el archivo HTML, notarás un bloque de `<style>` muy grande. Allí usamos:
- `backdrop-filter: blur(15px)`: Esta propiedad de CSS es la responsable de crear el efecto "vidrio empañado" (*Glassmorphism*) tan popular en los diseños premium actuales de Apple o Microsoft.
- `display: grid`: Para organizar las 3 tarjetas de metas alcanzadas de manera responsiva (se adaptan si lo abres en un celular o en PC).

---

## 🎓 Conclusión para tu Aprendizaje

1. **Datos:** El secreto de un buen científico de datos no es aplicar algoritmos complejos, sino entender el problema del negocio (Agrupar > Predecir).
2. **Backend/Análisis:** Python y Pandas son herramientas poderosas para limpiar y matematizar grandes volúmenes de datos rápidamente.
3. **Frontend/Presentación:** Un análisis no sirve de nada si no se sabe vender. El uso de Streamlit (para gerencia interna) y de una Landing Page en HTML (para el público o portafolio) garantiza que tu trabajo destaque frente al de otros desarrolladores.
