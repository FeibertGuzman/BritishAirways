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

st.title("✈️ British Airways - Lounge Eligibility Dashboard")
st.markdown("### Forage Data Science Task 1")
st.write("Este dashboard presenta el resumen de los pasajeros elegibles para las salas VIP (Lounges) de Nivel 1, Nivel 2 y Nivel 3, agrupados por Tipo de Vuelo (HAUL) y Momento del Día.")

@st.cache_data
def load_data():
    df = pd.read_csv('data/processed_lounge_data.csv')
    return df

df = load_data()

# KPI Cards
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Pasajeros", f"{df['TOTAL_PAX'].sum():,.0f}")
col2.metric("Total Nivel 1 (Concorde)", f"{df['TIER1_ELIGIBLE_PAX'].sum():,.0f}")
col3.metric("Total Nivel 2 (First)", f"{df['TIER2_ELIGIBLE_PAX'].sum():,.0f}")
col4.metric("Total Nivel 3 (Club)", f"{df['TIER3_ELIGIBLE_PAX'].sum():,.0f}")

st.divider()

# Charts
st.subheader("📊 Distribución de Demanda de Salas VIP por Tipo de Vuelo y Hora")
colA, colB = st.columns(2)

with colA:
    # Bar chart for passenger counts
    melted_df = df.melt(id_vars=['HAUL', 'TIME_OF_DAY'], value_vars=['TIER1_ELIGIBLE_PAX', 'TIER2_ELIGIBLE_PAX', 'TIER3_ELIGIBLE_PAX'], var_name='Tier', value_name='Passengers')
    fig_bar = px.bar(melted_df, x='HAUL', y='Passengers', color='Tier', barmode='group', facet_col='TIME_OF_DAY', title='Pasajeros Elegibles por Nivel')
    st.plotly_chart(fig_bar, use_container_width=True)

with colB:
    # Pie chart for total eligible passengers
    total_tiers = pd.DataFrame({
        'Tier': ['Nivel 1', 'Nivel 2', 'Nivel 3'],
        'Passengers': [df['TIER1_ELIGIBLE_PAX'].sum(), df['TIER2_ELIGIBLE_PAX'].sum(), df['TIER3_ELIGIBLE_PAX'].sum()]
    })
    fig_pie = px.pie(total_tiers, names='Tier', values='Passengers', title='Proporción Total de Demanda', hole=0.4, color_discrete_sequence=['#134074', '#8da9c4', '#eef4ed'])
    st.plotly_chart(fig_pie, use_container_width=True)

st.divider()

# Data Table
st.subheader("📋 Tabla de Consulta de Elegibilidad")
st.write("La siguiente tabla muestra el porcentaje estimado de elegibilidad por Nivel respecto al total de pasajeros para cada grupo.")

display_df = df[['HAUL', 'TIME_OF_DAY', 'Nivel 1 %', 'Nivel 2 %', 'Nivel 3 %']].copy()
# Format percentages
display_df['Nivel 1 %'] = (display_df['Nivel 1 %'] * 100).map("{:.2f}%".format)
display_df['Nivel 2 %'] = (display_df['Nivel 2 %'] * 100).map("{:.2f}%".format)
display_df['Nivel 3 %'] = (display_df['Nivel 3 %'] * 100).map("{:.2f}%".format)

st.dataframe(display_df, use_container_width=True)

st.caption("Desarrollado para British Airways Forage Job Simulation.")
