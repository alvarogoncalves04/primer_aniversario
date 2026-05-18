import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

st.title("📊 Nuestro primer año en estadísticas... ¡más locas!")
st.markdown("*Porque el amor también se mide en helados y abrazos.*")

# Gráfica 1: Competencia de snacks favoritos
snacks = pd.DataFrame({
    "Snack": ["Helados 🍦", "Galletas 🍪", "Hamburguesas 🍔", "Papitas 🥔", "Chocolate 🍫"],
    "Veces que comimos juntos": [24, 18, 12, 30, 15]
})
fig1 = px.bar(snacks, x="Snack", y="Veces que comimos juntos", title="¡Carrera de antojos compartidos!", color="Snack")
st.plotly_chart(fig1, use_container_width=True)

# Gráfica 2: Actividades favoritas
actividades = pd.DataFrame({
    "Actividad": ["Ver series 📺", "Caminar por el parque 🌳", "Cocinar juntos 👩‍🍳", "Tomar fotos 📸", "Abrazarnos 🤗"],
    "Cantidad": [45, 22, 18, 67, 200]
})
fig2 = px.bar(actividades, x="Actividad", y="Cantidad", title="¿Qué hemos hecho más veces?", color="Actividad")
st.plotly_chart(fig2, use_container_width=True)

# Gráfica 3: Lugares más visitados (con emojis)
lugares = pd.DataFrame({
    "Lugar": ["Migas 🍔", "Parque del Este 🌳", "Cine 🎬", "Nuestra casa 🏠"],
    "Visitas": [8, 5, 4, 150]
})
fig3 = px.bar(lugares, x="Lugar", y="Visitas", title="Nuestros rincones favoritos", color="Lugar")
st.plotly_chart(fig3, use_container_width=True)

# Contador de días desde la primera cita (14 feb 2025)
fecha_primera_cita = date(2025, 2, 14)
dias_juntos = (date.today() - fecha_primera_cita).days
st.metric("📅 Días desde que nos conocimos en Migas", dias_juntos)

# Un dato curioso gracioso
st.success("🎉 **Dato freak:** Nos hemos mandado aproximadamente 1,234 mensajes de 'te quiero' (contados mentalmente).")
st.info("💖 Próximo desafío: comer 100 helados juntos. ¡Vamos por la meta!")

# Galería de fotos
st.subheader("📸 Un vistazo a nuestro año")
col1, col2, col3 = st.columns(3)

with col1:
    try:
        st.image("images/portada.jpg", caption="Día que nos conocimos")
    except:
        st.image("https://placehold.co/300x200?text=Foto+1")

with col2:
    try:
        st.image("images/migas.jpg", caption="En Migas")
    except:
        st.image("https://placehold.co/300x200?text=Foto+2")

with col3:
    try:
        st.image("images/selfie.jpg", caption="Nuestro selfie")
    except:
        st.image("https://placehold.co/300x200?text=Foto+3")
        
st.info("💖 Cada foto, cada lugar y cada día contigo son únicos. ¡Feliz primer año!")