import streamlit as st
import random
from datetime import date, datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64

st.set_page_config(page_title="Rincón de Recuerdos", page_icon="🎉")

st.markdown("""
<style>
    .stApp {
        background-color: #1E1A1A;
    }
    .romantic-card {
        background-color: #2C2626;
        border-radius: 20px;
        padding: 1rem;
        margin-bottom: 1rem;
        box-shadow: 0 4px 12px rgba(0,0,0,0.3);
        border-left: 5px solid #B54A4A;
    }
    .timeline-item {
        background-color: #3A2C2C;
        border-radius: 15px;
        padding: 0.8rem;
        margin: 0.5rem 0;
        transition: transform 0.2s;
    }
    .timeline-item:hover {
        transform: scale(1.02);
        background-color: #4A3A3A;
    }
    .polaroid {
        background-color: #FDF8F0;
        padding: 0.8rem;
        border-radius: 10px;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        text-align: center;
        color: #3E2A2A;
    }
    .stButton button {
        width: 100%;
    }
    .stProgress > div > div {
        background-color: #B54A4A !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎉 Nuestro rincón mágico del primer año")
st.markdown("*Cada recuerdo, un tesoro. Explora, juega y planea nuestro futuro juntos.*")

# Cuenta regresiva
proximo_aniversario = date(2027, 2, 14)
hoy = date.today()
dias_restantes = (proximo_aniversario - hoy).days
if dias_restantes > 0:
    st.metric("⏳ Días para nuestro segundo aniversario", dias_restantes)
    st.progress(1 - dias_restantes/365, text="Año en curso")
else:
    st.success("¡Hoy es nuestro aniversario! 🎂")

st.divider()

# Mapa de aventuras
st.subheader("🗺️ Lugares que atesoramos")
st.markdown("*Cada lugar guarda una historia. Haz clic en cada tarjeta para leerla.*")

lugares = {
    "🍔 Migas (Caracas)": {"historia": "Aquí comenzó todo con unas hamburguesas crispy. Esa primera cita fue mágica, llena de nervios y sonrisas. ¡Nunca olvidaré cómo te mordiste el labio mientras pedías!", "icono": "🍔", "foto": "images/primeracita.jpeg"},
    "🌳 Parque del Este": {"historia": "Nuestro primer picnic. Tú trajiste frutas y yo olvidé el abrelatas. Terminamos comprando helados y paseando hasta el atardecer.", "icono": "🌳", "foto": None},
    "🎬 Cine Plaza": {"historia": "Vimos una película de terror y te escondiste detrás de mí. Luego me confesaste que no te gustaba el terror, pero querías sentir mi brazo alrededor de ti.", "icono": "🎬", "foto": "images/cinebillie.jpeg"},
    "🏠 Nuestra casa": {"historia": "Nuestro refugio, donde cocinamos mal pero reímos bien, donde vimos series hasta las 3 am y donde cada rincón guarda un abrazo.", "icono": "🏠", "foto": "images/micasa.jpeg"}
}

cols_map = st.columns(2)
for i, (lugar, info) in enumerate(lugares.items()):
    with cols_map[i % 2]:
        with st.expander(f"{info['icono']} {lugar}"):
            if info["foto"]:
                try:
                    st.image(info["foto"], use_container_width=True)
                except:
                    pass
            st.write(info["historia"])
            if st.button(f"Recordar {lugar.split()[0]}", key=f"btn_{i}"):
                st.balloons()
                st.success("✨ ¡Ese día fue increíble! Gracias por ese recuerdo.")

st.divider()

# Línea de tiempo
st.subheader("📅 Línea de tiempo de nuestros momentos épicos")
timeline = [
    ("14 Feb 2025", "⭐ Nos conocimos en Migas", "Hamburguesas, risas y electricidad en el aire."),
    ("20 Mar 2025", "📸 Primera foto juntos", "Selfie en el Parque del Este con un atardecer de fondo."),
    ("10 Jun 2025", "🍦 Primera pelea graciosa", "Discutimos quién se comió el último helado (fuiste tú)."),
    ("14 Ago 2025", "🎂 Mi cumpleaños sorpresa", "Me llevaste a comer hamburguesas otra vez. ¡Eres perfecta!"),
    ("14 Feb 2026", "💖 Primer aniversario", "Hoy celebramos este año increíble. ¡Te amo más que nunca!")
]

for fecha, titulo, desc in timeline:
    st.markdown(f"""
    <div class="timeline-item">
        <strong>{fecha}</strong> – <em>{titulo}</em><br>
        <span style="font-size:0.9rem;">{desc}</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# Medidor de chispitas
st.subheader("✨ Medidor de chispitas de amor")
if "chispas" not in st.session_state:
    st.session_state.chispas = random.randint(20, 50)

col1, col2 = st.columns([1, 2])
with col1:
    if st.button("❤️ ¡Dar like! (chispa extra)", use_container_width=True):
        st.session_state.chispas += 1
        st.balloons()
        st.success("¡Chispa añadida! 💥")
with col2:
    st.metric("Chispitas acumuladas", st.session_state.chispas)

nivel_chispas = min(100, st.session_state.chispas * 2)
st.progress(nivel_chispas / 100, text=f"Intensidad del amor: {nivel_chispas}%")

st.divider()

# Rincón de planes locos
st.subheader("📝 Rincón de planes locos")
if "planes" not in st.session_state:
    st.session_state.planes = [
        "🍦 Comer 100 helados juntos",
        "💃 Bailar bajo la lluvia",
        "🌋 Visitar el Ávila de noche",
        "🍔 Probar todas las hamburguesas de Migas",
        "✈️ Viajar a la playa"
    ]

nuevo_plan = st.text_input("✨ Nuevo plan loco:", placeholder="Ejemplo: Aprender a bailar salsa")
if st.button("➕ Agregar plan", use_container_width=True):
    if nuevo_plan.strip():
        st.session_state.planes.append(nuevo_plan.strip())
        st.rerun()

st.write("**📌 Lista de pendientes chéveres:**")
for i, plan in enumerate(st.session_state.planes):
    col_check, col_text = st.columns([0.1, 0.9])
    with col_check:
        st.checkbox("", key=f"check_{i}")
    with col_text:
        st.write(f"{i+1}. {plan}")

def generar_imagen_planes(lista_planes):
    fig, ax = plt.subplots(figsize=(8, 0.3 * len(lista_planes) + 2))
    ax.axis('off')
    fig.patch.set_facecolor('#FDF8F0')
    texto = "\n".join([f"{i+1}. {p}" for i, p in enumerate(lista_planes)])
    ax.text(0.05, 0.95, texto, transform=ax.transAxes, fontsize=12, verticalalignment='top', family='monospace', color='#3E2A2A')
    ax.set_title("Nuestros planes locos futuros", fontsize=14, fontweight='bold', color='#B54A4A')
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight')
    buf.seek(0)
    plt.close(fig)
    return buf

if st.button("📸 Descargar lista de planes como imagen", use_container_width=True):
    img_buf = generar_imagen_planes(st.session_state.planes)
    b64 = base64.b64encode(img_buf.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{b64}" download="planes_locos.png">Haz clic aquí para guardar la imagen</a>'
    st.markdown(href, unsafe_allow_html=True)

st.divider()

# Muro de recuerdos Polaroid con fotos reales
st.subheader("🖼️ Muro de recuerdos (Polaroids)")
st.markdown("*Nuestros momentos favoritos en formato vintage.*")

recuerdos_fotos = [
    {"titulo": "Primera cita en Migas", "desc": "Hamburguesas crispy", "fecha": "Feb 2025", "foto": "images/primeracita.jpeg", "emoji": "🍔"},
    {"titulo": "Primera foto juntos", "desc": "Nuestro primer selfie", "fecha": "Mar 2025", "foto": "images/primerafotojuntos.jpeg", "emoji": "📷"},
    {"titulo": "Noche de sushi", "desc": "Compartiendo comida", "fecha": "Abr 2025", "foto": "images/sushi.jpeg", "emoji": "🍣"},
    {"titulo": "En nuestra casa", "desc": "Nuestro refugio", "fecha": "May 2025", "foto": "images/micasa.jpeg", "emoji": "🏠"},
    {"titulo": "Nocturneando", "desc": "Aventuras de noche", "fecha": "Jun 2025", "foto": "images/nocturneando.jpeg", "emoji": "🌙"},
    {"titulo": "Navidad juntos", "desc": "Celebrando en familia", "fecha": "Dic 2025", "foto": "images/24diciembre.jpeg", "emoji": "🎄"},
    {"titulo": "San Valentín", "desc": "Nuestro primer 14F", "fecha": "Feb 2026", "foto": "images/14febrero.jpeg", "emoji": "💖"},
    {"titulo": "Enamorados", "desc": "Así nos sentimos", "fecha": "Siempre", "foto": "images/enamorados.jpeg", "emoji": "💕"},
    {"titulo": "Gaitas venezolanas", "desc": "Tradición y amor", "fecha": "Dic 2025", "foto": "images/gaitas.jpeg", "emoji": "🎶"}
]

cols_polaroid = st.columns(3)
for i, rec in enumerate(recuerdos_fotos):
    with cols_polaroid[i % 3]:
        st.markdown(f"""
        <div class="polaroid">
        """, unsafe_allow_html=True)
        
        try:
            from PIL import Image
            img = Image.open(rec["foto"])
            st.image(img, use_container_width=True)
        except:
            st.markdown(f"<div style='font-size: 3rem; text-align:center;'>{rec['emoji']}</div>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <strong>{rec['titulo']}</strong><br>
            <span style="font-size:0.8rem;">{rec['desc']}</span><br>
            <span style="font-size:0.7rem; color:#7A5A5A;">{rec['fecha']}</span>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# Horóscopo
st.subheader("🔮 Horóscopo de la relación (versión chévere)")

frases = [
    "💫 Hoy el universo conspira para que coman helado juntos. ¡Aprovecha!",
    "🌙 Las estrellas predicen una tarde de abrazos y risas. No la dejes escapar.",
    "🍔 Cuidado con los antojos compartidos: podrían terminar en una segunda cena.",
    "🎵 Es un buen día para recordar por qué te elegí: ¡porque eres la mejor loca que conozco!",
    "🌌 La luna está en cuarto creciente, ideal para hacer planes locos (como pedir hamburguesas a las 11 pm).",
    "💖 Venus alinea tu mirada con la mía. Prepárate para un 'te quiero' espontáneo."
]

if st.button("✨ Ver predicción del día", use_container_width=True):
    prediccion = random.choice(frases)
    st.info(prediccion)
    if "te quiero" in prediccion.lower():
        st.balloons()
        st.success("¡Esa predicción ya se cumplió! ❤️")
else:
    st.info("Presiona el botón para recibir tu horóscopo diario.")

st.divider()

# Botón sorpresa final
st.subheader("🎁 ¿Un último detalle?")
if st.button("🕯️ Encender la llama eterna", use_container_width=True):
    st.balloons()
    st.snow()
    st.markdown("""
    <div style="background-color:#2C2626; padding:1rem; border-radius:15px; text-align:center;">
        <h3 style="color:#B54A4A;">✨ Eres la luz de mi vida ✨</h3>
        <p>Gracias por este año increíble. Te amo más allá de las estrellas.</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("*Hecho con todo el amor del mundo, utilizando estadísticas, biología y mucha programación. 💻💖*")