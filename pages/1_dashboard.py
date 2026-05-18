import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

st.title("📸 Nuestro primer año en datos")

# DATOS PERSONALES (CÁMBIALOS por los tuyos)
meses = ["Mayo", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic", "Ene", "Feb", "Mar", "Abr"]
fotos_por_mes = [12, 25, 18, 30, 22, 35, 28, 45, 32, 27, 40, 50]  # reemplaza con números reales

df_fotos = pd.DataFrame({"Mes": meses, "Fotos juntos": fotos_por_mes})
fig1 = px.bar(df_fotos, x="Mes", y="Fotos juntos", title="📷 Cantidad de fotos que nos tomamos cada mes")
st.plotly_chart(fig1, use_container_width=True)

# MAPA DE LUGARES ESPECIALES (necesitas coordenadas reales)
# Ejemplo: Migas en Caracas (busca en Google Maps las coordenadas)
lugares = pd.DataFrame({
    "Lugar": ["Migas Caracas", "Nombre del otro lugar"],
    "lat": [10.4961, 10.5000],   # cámbialo por coordenadas reales
    "lon": [-66.8980, -66.9000]
})
st.subheader("🗺️ Lugares que marcaron nuestro año")
st.map(lugares)

# CONTADOR DE DÍAS DESDE LA PRIMERA CITA
fecha_primera_cita = date(2024, 5, 20)  # cámbiala por la fecha real
dias_juntos = (date.today() - fecha_primera_cita).days
st.metric("Días desde nuestra primera cita en Migas", dias_juntos)

st.info("💖 Cada foto, cada lugar y cada día contigo son únicos. ¡Feliz primer año!")
