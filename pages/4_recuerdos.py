import streamlit as st
import random
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
from io import BytesIO

st.set_page_config(page_title="Rincón de Recuerdos", page_icon="🎉")
st.title("🎉 Nuestro rincón mágico del primer año")
st.markdown("*Mapa, línea de tiempo, planes locos, muro Polaroid y horóscopo... ¡y más!*")

# ==================== 1. MAPA DE AVENTURAS ====================
st.subheader("🗺️ Mapa de nuestras aventuras")
st.markdown("Lugares que marcaron nuestro año (con anécdotas)")

lugares = {
    "Migas Caracas": {"lat": 10.4961, "lon": -66.8980, "historia": "Aquí comenzó todo con unas hamburguesas crispy inolvidables. 🍔"},
    "Parque del Este": {"lat": 10.4939, "lon": -66.8416, "historia": "Nuestro primer picnic y un atardecer mágico. 🌳"},
    "Cine Plaza": {"lat": 10.5000, "lon": -66.9064, "historia": "Vimos una película de terror y te escondiste detrás de mí. 🎬"},
}

df_map = pd.DataFrame([{"lat": v["lat"], "lon": v["lon"], "nombre": k} for k, v in lugares.items()])
st.map(df_map)

for nombre, info in lugares.items():
    with st.expander(f"📍 {nombre}"):
        st.write(info["historia"])
        st.caption("(Coordenadas aproximadas)")

# ==================== 2. LÍNEA DE TIEMPO ====================
st.subheader("📅 Línea de tiempo de nuestros momentos épicos")
timeline = [
    ("14 Feb 2025", "⭐ Nos conocimos en Migas", "Hamburguesas, risas y electricidad en el aire."),
    ("20 Mar 2025", "📸 Primera foto juntos", "Selfie en el Parque del Este con un atardecer de fondo."),
    ("10 Jun 2025", "🍦 Primera pelea graciosa", "Discutimos quién se comió el último helado (fuiste tú)."),
    ("14 Ago 2025", "🎂 Mi cumpleaños sorpresa", "Me llevaste a comer hamburguesas otra vez. ¡Eres perfecta!"),
    ("14 Feb 2026", "💖 Primer aniversario", "Hoy celebramos este año increíble. ¡Te amo!"),
]
for fecha, titulo, desc in timeline:
    with st.container():
        st.markdown(f"**{fecha}** – *{titulo}*")
        st.write(desc)
        st.divider()

# ==================== 3. RINCÓN DE PLANES LOCOS (con descarga en imagen) ====================
st.subheader("📝 Rincón de planes locos")
st.markdown("Escribe cosas que quieras hacer juntos en el futuro. ¡Las guardamos en tu sesión!")

if "planes" not in st.session_state:
    st.session_state.planes = ["Comer 100 helados juntos", "Bailar bajo la lluvia", "Visitar el Ávila de noche"]

nuevo_plan = st.text_input("Nuevo plan loco:")
if st.button("Agregar plan"):
    if nuevo_plan.strip():
        st.session_state.planes.append(nuevo_plan.strip())
        st.rerun()

st.write("**Lista de pendientes chéveres:**")
for i, plan in enumerate(st.session_state.planes):
    st.write(f"{i+1}. {plan}")

# Función para generar imagen PNG de la lista de planes
def generar_imagen_planes(lista_planes):
    fig, ax = plt.subplots(figsize=(6, 0.5 * len(lista_planes) + 1))
    ax.axis('off')
    texto = "\n".join([f"{i+1}. {p}" for i, p in enumerate(lista_planes)])
    ax.text(0.1, 0.9, texto, transform=ax.transAxes, fontsize=12, verticalalignment='top', family='monospace')
    ax.set_title("Nuestros planes locos futuros", fontsize=14, fontweight='bold')
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close(fig)
    return buf

if st.button("📸 Descargar lista de planes como imagen PNG"):
    img_buf = generar_imagen_planes(st.session_state.planes)
    st.download_button("Haz clic aquí para guardar la imagen", img_buf, file_name="planes_locos.png", mime="image/png")

# ==================== 4. MURO DE RECUERDOS TIPO POLAROID ====================
st.subheader("🖼️ Muro de recuerdos (Polaroids)")
st.markdown("*Aquí irán nuestras fotos. Por ahora, emojis y frases.*")
cols = st.columns(3)
recuerdos = [
    ("🍔", "Primera cita en Migas", "Hamburguesas crispy y miradas"),
    ("📷", "Selfie en el parque", "Ese atardecer naranja"),
    ("🎬", "Noche de cine", "Te escondiste en mi hombro")
]
for i, (emoji, titulo, desc) in enumerate(recuerdos):
    with cols[i % 3]:
        st.markdown(f"📸 **{titulo}**")
        st.write(f"{emoji} {desc}")
        st.caption("(Pronto una foto real)")

# ==================== 5. HORÓSCOPO DE LA RELACIÓN ====================
st.subheader("🔮 Horóscopo de la relación (versión chévere)")
frases = [
    "Hoy el universo conspira para que coman helado juntos. ¡Aprovecha!",
    "Las estrellas predicen una tarde de abrazos y risas. No la dejes escapar.",
    "Cuidado con los antojos compartidos: podrían terminar en una segunda cena.",
    "Es un buen día para recordar por qué te elegí: ¡porque eres la mejor loca que conozco!",
    "La luna está en cuarto creciente, ideal para hacer planes locos (como pedir hamburguesas a las 11 pm).",
    "Venus alinea tu mirada con la mía. Prepárate para un 'te quiero' espontáneo."
]
if st.button("✨ Ver predicción del día"):
    st.info(random.choice(frases))
else:
    st.info("Presiona el botón para recibir tu horóscopo diario.")