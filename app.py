import streamlit as st
from datetime import date

st.set_page_config(page_title="Primer Aniversario", page_icon="💖")

st.title("💖 ¡Feliz Primer Aniversario, Victoria! 💖")
st.markdown("*Hoy celebramos 365 días de amor, risas y aprendizaje juntos.*")
st.markdown("**¡Entre perros calientes, helados, y mucho amor!**")

# Fecha de inicio (cámbiala si es otra)
fecha_inicio = date(2025, 2, 14)  # 14 de febrero de 2025
dias_juntos = (date.today() - fecha_inicio).days
st.metric("Días desde que nos conocimos en Migas", dias_juntos)

# Imagen de portada (si ya tienes una foto en images/portada.jpg)
try:
    from PIL import Image
    img = Image.open("images/portada.jpg")
    st.image(img, use_column_width=True)
except:
    st.info("📸 Pronto pondré aquí nuestra foto favorita.")

if st.button("🎁 Haz clic para una sorpresa"):
    st.balloons()
    st.success("¡Te amo más que ayer y menos que mañana churra! 💕")

st.sidebar.title("📅 Nuestro primer año")
st.sidebar.info("Usa el menú de arriba para ver el dashboard, jugar o recibir una carta especial.")