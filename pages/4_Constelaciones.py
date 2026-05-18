import streamlit as st
from datetime import datetime

st.set_page_config(page_title="El cielo de nuestro encuentro", page_icon="⭐")
st.title("⭐ El cielo la noche que nos conocimos")
st.markdown("*14 de febrero de 2025 – Caracas, Venezuela*")

st.subheader("🌌 ¿Cómo estaban las estrellas aquel día?")

# Imagen del cielo estrellado (puedes cambiarla por una captura real de Stellarium)
st.image("https://cdn.pixabay.com/photo/2016/01/08/11/57/stars-1127476_1280.jpg", 
         caption="Cielo estrellado (imagen referencial)", use_column_width=True)

st.markdown("""
Esa noche, a eso de las 8:00 pm en Caracas, el cielo nos regalaba un espectáculo único:

- **Orión** se alzaba imponente en el sureste, con sus tres Marias brillando como testigos.
- **Tauro** y la estrella **Aldebarán** acompañaban cerca, como queriendo decir "algo especial va a pasar".
- **Sirio**, la estrella más brillante, titilaba en el horizonte, iluminando nuestro encuentro.
- La **Luna** estaba en cuarto creciente, sonriendo desde lo alto.

Esa combinación de astros, sin saberlo, estaba alineando nuestros caminos. Cada estrella era un deseo que todavía no sabíamos pedir.

💖 *Esa noche nacieron millones de chispas en el cielo, pero la más bonita fue la que surgió entre nosotros.*
""")

# Opción de mostrar una imagen más precisa si el usuario la sube
st.info("📸 Si quieres, puedes subir una captura real del cielo de esa fecha (desde Stellarium o similar).")
imagen_subida = st.file_uploader("Sube tu imagen (opcional)", type=["jpg", "png"])
if imagen_subida is not None:
    st.image(imagen_subida, caption="Cielo real del 14/02/2025", use_column_width=True)