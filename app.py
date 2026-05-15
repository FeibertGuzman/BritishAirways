import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Lounge Eligibility Dashboard", page_icon="✈️", layout="wide")

# Custom CSS for a better look
st.markdown("""
    <style>
    .main {
        background-color: #f8f9fa;
    }
    h1 {
        color: #0b2545;
    }
    h2, h3 {
        color: #134074;
    }
    .stDataFrame {
        border-radius: 10px;
        overflow: hidden;
    }
    </style>
""", unsafe_allow_html=True)

# -----------------
# DATA LOADING
# -----------------
@st.cache_data
def load_data():
    df = pd.read_csv('data/processed_lounge_data.csv')
    return df

@st.cache_data
def load_excel_report():
    df_excel = pd.read_excel('data/Filled_Lounge_Eligibility_Lookup.xlsx')
    return df_excel

df = load_data()
df_excel = load_excel_report()

# -----------------
# SIDEBAR / FILTERS
# -----------------
st.sidebar.image("https://upload.wikimedia.org/wikipedia/en/thumb/9/98/British_Airways_Logo.svg/1200px-British_Airways_Logo.svg.png", width=200)
st.sidebar.title("Filtros y Navegación")

# Filters
haul_options = ['Todos'] + list(df['HAUL'].unique())
selected_haul = st.sidebar.selectbox("Filtro por Alcance (HAUL)", haul_options)

time_options = ['Todos'] + list(df['TIME_OF_DAY'].unique())
selected_time = st.sidebar.selectbox("Filtro por Momento del Día", time_options)

st.sidebar.markdown("---")
st.sidebar.markdown("**Realizado por:** Feibert Guzmán")

# Filter logic
filtered_df = df.copy()
if selected_haul != 'Todos':
    filtered_df = filtered_df[filtered_df['HAUL'] == selected_haul]
if selected_time != 'Todos':
    filtered_df = filtered_df[filtered_df['TIME_OF_DAY'] == selected_time]

# -----------------
# MAIN CONTENT / TABS
# -----------------
st.title("✈️ British Airways - Lounge Eligibility Dashboard")
st.markdown("### Forage Data Science Task 1")

tab1, tab2 = st.tabs(["Dashboard Principal", "Reporte Excel Generado"])

with tab1:
    st.write("Este dashboard presenta el resumen de los pasajeros elegibles para las salas VIP (Lounges) de Nivel 1, Nivel 2 y Nivel 3, agrupados por Tipo de Vuelo (HAUL) y Momento del Día.")
    
    # KPI Cards
    col1, col2, col3, col4 = st.columns(4)
    total_pax = filtered_df['TOTAL_PAX'].sum() if not filtered_df.empty else 0
    t1_pax = filtered_df['TIER1_ELIGIBLE_PAX'].sum() if not filtered_df.empty else 0
    t2_pax = filtered_df['TIER2_ELIGIBLE_PAX'].sum() if not filtered_df.empty else 0
    t3_pax = filtered_df['TIER3_ELIGIBLE_PAX'].sum() if not filtered_df.empty else 0

    col1.metric("Total Pasajeros", f"{total_pax:,.0f}")
    col2.metric("Total Nivel 1 (Concorde)", f"{t1_pax:,.0f}")
    col3.metric("Total Nivel 2 (First)", f"{t2_pax:,.0f}")
    col4.metric("Total Nivel 3 (Club)", f"{t3_pax:,.0f}")

    st.divider()

    # Charts
    st.subheader("📊 Distribución de Demanda de Salas VIP por Tipo de Vuelo y Hora")
    if not filtered_df.empty:
        colA, colB = st.columns(2)

        with colA:
            # Bar chart for passenger counts
            melted_df = filtered_df.melt(id_vars=['HAUL', 'TIME_OF_DAY'], value_vars=['TIER1_ELIGIBLE_PAX', 'TIER2_ELIGIBLE_PAX', 'TIER3_ELIGIBLE_PAX'], var_name='Tier', value_name='Passengers')
            # Handle facet_col dynamically if filtered down to 1 value to avoid plotly errors
            if len(filtered_df['TIME_OF_DAY'].unique()) > 1:
                fig_bar = px.bar(melted_df, x='HAUL', y='Passengers', color='Tier', barmode='group', facet_col='TIME_OF_DAY', title='Pasajeros Elegibles por Nivel')
            else:
                fig_bar = px.bar(melted_df, x='HAUL', y='Passengers', color='Tier', barmode='group', title=f"Pasajeros Elegibles por Nivel ({filtered_df['TIME_OF_DAY'].iloc[0]})")
            st.plotly_chart(fig_bar, use_container_width=True)

        with colB:
            # Pie chart for total eligible passengers
            total_tiers = pd.DataFrame({
                'Tier': ['Nivel 1', 'Nivel 2', 'Nivel 3'],
                'Passengers': [t1_pax, t2_pax, t3_pax]
            })
            if total_tiers['Passengers'].sum() > 0:
                fig_pie = px.pie(total_tiers, names='Tier', values='Passengers', title='Proporción Total de Demanda', hole=0.4, color_discrete_sequence=['#134074', '#8da9c4', '#eef4ed'])
                st.plotly_chart(fig_pie, use_container_width=True)
            else:
                st.info("No hay suficientes datos para generar el gráfico circular.")

        st.divider()

        # Data Table
        st.subheader("📋 Tabla de Consulta de Elegibilidad")
        st.write("La siguiente tabla muestra el porcentaje estimado de elegibilidad por Nivel respecto al total de pasajeros para cada grupo.")

        display_df = filtered_df[['HAUL', 'TIME_OF_DAY', 'Nivel 1 %', 'Nivel 2 %', 'Nivel 3 %']].copy()
        # Format percentages
        display_df['Nivel 1 %'] = (display_df['Nivel 1 %'] * 100).map("{:.2f}%".format)
        display_df['Nivel 2 %'] = (display_df['Nivel 2 %'] * 100).map("{:.2f}%".format)
        display_df['Nivel 3 %'] = (display_df['Nivel 3 %'] * 100).map("{:.2f}%".format)

        st.dataframe(display_df, use_container_width=True)
    else:
        st.warning("No hay datos disponibles para los filtros seleccionados.")

with tab2:
    st.subheader("📄 Reporte Excel: Lounge Eligibility Lookup")
    st.write("Visualización del archivo base que se llenó automáticamente con el modelo: `Filled_Lounge_Eligibility_Lookup.xlsx`")
    st.dataframe(df_excel, use_container_width=True)

st.caption("Desarrollado para British Airways Forage Job Simulation.")
