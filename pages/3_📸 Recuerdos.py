import streamlit as st
import random
from datetime import date, datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64

st.set_page_config(page_title="Rincón de Recuerdos", page_icon="🎉")

# CSS personalizado
st.markdown("""
<style>
    .stApp {
        background-color: #1E1A1A;
    }
    .romantic-card {
        background: linear-gradient(135deg, #2C2626, #3D2C2C);
        border-radius: 20px;
        padding: 1.2rem;
        margin-bottom: 1rem;
        box-shadow: 0 8px 20px rgba(0,0,0,0.3);
        border-left: 5px solid #B54A4A;
        transition: transform 0.3s, box-shadow 0.3s;
    }
    .romantic-card:hover {
        transform: translateY(-3px);
        box-shadow: 0 12px 25px rgba(0,0,0,0.4);
    }
    .timeline-item {
        background: linear-gradient(95deg, #3A2C2C, #2C2626);
        border-radius: 15px;
        padding: 0.8rem 1rem;
        margin: 0.7rem 0;
        transition: all 0.3s ease;
        border-right: 3px solid #B54A4A;
        cursor: pointer;
    }
    .timeline-item:hover {
        transform: translateX(8px);
        background: linear-gradient(95deg, #4A3A3A, #3A2C2C);
    }
    .polaroid {
        background: linear-gradient(145deg, #FDF8F0, #F5E6D3);
        padding: 0.8rem 0.8rem 1.2rem 0.8rem;
        border-radius: 12px;
        box-shadow: 0 8px 16px rgba(0,0,0,0.2);
        text-align: center;
        color: #3E2A2A;
        transition: transform 0.3s, box-shadow 0.3s;
        transform: rotate(0deg);
    }
    .polaroid:hover {
        transform: rotate(1deg) scale(1.02);
        box-shadow: 0 12px 24px rgba(0,0,0,0.3);
    }
    .stButton button {
        width: 100%;
        background: linear-gradient(135deg, #B54A4A, #8B3A3A) !important;
        border: none !important;
    }
    .stProgress > div > div {
        background: linear-gradient(90deg, #B54A4A, #FF6B6B) !important;
    }
    .horoscopo-card {
        background: linear-gradient(135deg, #2C2626, #1E1A1A);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        border: 2px solid #B54A4A;
        box-shadow: 0 0 20px rgba(181,74,74,0.2);
    }
    .piropo-card {
        background: linear-gradient(135deg, #2C2626, #3D2C2C);
        border-radius: 20px;
        padding: 1rem;
        margin: 0.5rem 0;
        text-align: center;
        font-style: italic;
        border-bottom: 2px solid #B54A4A;
        transition: all 0.3s;
    }
    .piropo-card:hover {
        transform: scale(1.02);
        background: linear-gradient(135deg, #3D2C2C, #4A3A3A);
    }
    .sintonia-card {
        background: linear-gradient(135deg, #2C2626, #1E1A1A);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        border: 2px solid #FFD700;
        box-shadow: 0 0 20px rgba(255,215,0,0.3);
    }
</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <h1>🎉 Nuestro rincón mágico del primer año</h1>
    <p style="font-size: 1.1rem;">✨ Cada recuerdo, un tesoro. Explora, juega y planea nuestro futuro juntos. ✨</p>
</div>
""", unsafe_allow_html=True)

# ========== 1. CUENTA REGRESIVA ==========
proximo_aniversario = date(2026, 5, 25)
hoy = date.today()
dias_restantes = (proximo_aniversario - hoy).days

col_timer1, col_timer2, col_timer3 = st.columns([1, 2, 1])
with col_timer2:
    if dias_restantes > 0:
        st.metric("⏳ Días para nuestro siguiente aniversario", dias_restantes, delta=None)
        progreso_anio = max(0, min(1, (365 - dias_restantes) / 365))
        st.progress(progreso_anio, text="📅 Progreso del año en curso")
    else:
        st.success("🎂 ¡HOY ES NUESTRO ANIVERSARIO! 🎂 (falta un día)")

st.divider()

# ========== 2. MURAL DE PIROPOS Y AGRADECIMIENTOS ==========
st.subheader("💬 Mural de piropos y cosas por las que estoy agradecido")
st.markdown("*Pequeñas razones que me hacen amarte cada día más...*")

piropos = [
    "💖 Gracias por enseñarme que el amor se demuestra con acciones, no solo con palabras.",
    "🌹 Gracias por aguantar mis chistes malos y reírte de ellos como si fueran buenos.",
    "✨ Gracias por ser tú, auténtica, real y amando con locura.",
    "💕 Gracias por cada 'te amo' y abrazos inesperados que me saca una sonrisa.",
    "🌸 Gracias por las tardes de helado.",
    "🎵 Gracias por ser la musa que inspira cada uno de mis días.",
    "💪 Gracias por estar a mi lado en los días grises y celebrar los brillantes.",
    "🍔 Gracias por esa primera cita que cambió mi vida para siempre.",
    "💖 Eres mi persona favorita en el universo entero.",
    "🌙 Contigo hasta la luna y nunca quiero volver.",
    "✨ Desde que te conocí, las estrellas han sido más brillantes.",
    "💕 Gracias por hacerme sentir el hombre más afortunado del mundo."
]

cols_piropos = st.columns(3)
for i, piropo in enumerate(piropos):
    with cols_piropos[i % 3]:
        st.markdown(f"""
        <div class="piropo-card">
            {piropo}
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ========== 3. LÍNEA DE TIEMPO ==========
st.subheader("📅 Línea de tiempo de nuestros momentos épicos")
st.markdown("*Desliza sobre cada evento para ver el detalle*")

timeline = [
    ("14 Feb 2025", "⭐ La primera vez que nos vimos", "besos, risas y electricidad en el aire."),
    ("3 Mar 2025", "📝 La primera cita", "Hamburguesas, risas y felicidad a montones."),
    ("6 ABR 2025", "📝 La fiesta de manzanares", "tu dormida en mi pecho, paz,  plenitud"),
    ("30 MAY 2025", "📝 Caminarte", "Primera salida como novios"),
    ("01 OCT 2025", "📝 Cuando regresaste a vzla", "muchos sentimientos, te extrañaba tanto"),
    ("25 OCT 2025", "📝 Tu cumpleaños", "gaitas, celebración en familia, de los mejores días juntos"),
    ("24 DIC 2025", "📝 Primera navidad juntos", "la magia de pasarla contigo"),
    ("04 FEB 2026", "📝 Mi cumpleaños", "Hiciste que por fin lo disfrustara"),
    ("14 FEB 2026", "📝 Nuestro primer 14 de febrero", "Una cita que anhelabamos tanto"),
    ("25 May 2026", "💖 Primer aniversario", "Hoy celebramos este año increíble. ¡Te amo más que nunca!")
]

for fecha, titulo, desc in timeline:
    st.markdown(f"""
    <div class="timeline-item">
        <strong>📌 {fecha}</strong> – <em>{titulo}</em><br>
        <span style="font-size:0.9rem;">{desc}</span>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ========== 4. RINCÓN DE PLANES LOCOS ==========
st.subheader("📝 Rincón de planes locos")
st.markdown("*Escribe cosas que quieras hacer juntos en el futuro. ¡Se quedan guardados mientras explores la página!*")

if "planes" not in st.session_state:
    st.session_state.planes = [
        "🍦 Comer 100 helados juntos",
        "💃 Bailar bajo la lluvia",
        "🌋 Visitar el Ávila de noche",
        "🍔 Probar todas las hamburguesas de Migas",
        "✈️ Viajar a la playa",
        "🎨 Hacer una noche de pintura loca",
        "🍿 Marathon de películas de terror"
    ]

col_plan1, col_plan2 = st.columns([3, 1])
with col_plan1:
    nuevo_plan = st.text_input("✨ Escribe tu nuevo plan loco:", placeholder="Ejemplo: Aprender a bailar salsa 💃")
with col_plan2:
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("➕ Agregar", use_container_width=True):
        if nuevo_plan.strip():
            st.session_state.planes.append(nuevo_plan.strip())
            st.rerun()

st.write("**📌 Lista de aventuras pendientes:**")
for i, plan in enumerate(st.session_state.planes):
    col_check, col_text, col_del = st.columns([0.1, 0.75, 0.15])
    with col_check:
        hecho = st.checkbox("", key=f"check_{i}")
    with col_text:
        if hecho:
            st.markdown(f"~~{i+1}. {plan}~~ ✅")
        else:
            st.markdown(f"{i+1}. {plan}")
    with col_del:
        if st.button("🗑️", key=f"del_{i}"):
            st.session_state.planes.pop(i)
            st.rerun()

def generar_imagen_planes(lista_planes):
    fig, ax = plt.subplots(figsize=(10, 0.4 * len(lista_planes) + 2))
    ax.axis('off')
    fig.patch.set_facecolor('#FDF8F0')
    texto = "\n".join([f"{i+1}. {p}" for i, p in enumerate(lista_planes)])
    ax.text(0.05, 0.95, texto, transform=ax.transAxes, fontsize=12, 
            verticalalignment='top', family='monospace', color='#3E2A2A')
    ax.set_title("📋 Nuestros planes locos futuros", fontsize=14, fontweight='bold', color='#B54A4A', pad=20)
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=150)
    buf.seek(0)
    plt.close(fig)
    return buf

if st.button("📸 Descargar mi lista de planes como imagen", use_container_width=True):
    img_buf = generar_imagen_planes(st.session_state.planes)
    b64 = base64.b64encode(img_buf.getvalue()).decode()
    href = f'<a href="data:image/png;base64,{b64}" download="mis_planes_locos.png" style="text-decoration: none; background-color: #B54A4A; color: white; padding: 0.5rem 1rem; border-radius: 8px; display: inline-block;">💾 Haz clic aquí para guardar la imagen</a>'
    st.markdown(href, unsafe_allow_html=True)

st.divider()

# ========== 5. MURO POLAROID ==========
st.subheader("🖼️ Muro de recuerdos (Polaroids)")
st.markdown("*Nuestros momentos favoritos en formato vintage. Pasa el mouse para ver el efecto.*")

recuerdos_fotos = [
    {"titulo": "Primera cita", "desc": "Nervios y sonrisas", "fecha": "May 2025", "foto": "images/primeracita.jpeg", "emoji": "🍔"},
    {"titulo": "Primera foto juntos", "desc": "Nuestro primer selfie", "fecha": "May 2025", "foto": "images/primerafotojuntos.jpeg", "emoji": "📷"},
    {"titulo": "Primer sushi", "desc": "Compartiendo comida", "fecha": "Jun 2025", "foto": "images/sushi.jpeg", "emoji": "🍣"},
    {"titulo": "En casa", "desc": "Nuestro refugio", "fecha": "Jul 2025", "foto": "images/micasa.jpeg", "emoji": "🏠"},
    {"titulo": "Nocturneando", "desc": "Aventuras de noche", "fecha": "Ago 2025", "foto": "images/nocturneando.jpeg", "emoji": "🌙"},
    {"titulo": "Navidad juntos", "desc": "Celebrando en familia", "fecha": "Dic 2025", "foto": "images/24diciembre.jpeg", "emoji": "🎄"},
    {"titulo": "San Valentín", "desc": "Nuestro primer 14F", "fecha": "Feb 2026", "foto": "images/14febrero.jpeg", "emoji": "💖"},
    {"titulo": "Enamorados", "desc": "Así nos sentimos", "fecha": "Siempre", "foto": "images/enamorados.jpeg", "emoji": "💕"},
    {"titulo": "Gaitas", "desc": "amor y  másamor", "fecha": "Dic 2025", "foto": "images/gaitas.jpeg", "emoji": "🎶"},
    {"titulo": "Arrunchando", "desc": "Nuestro momento favorito", "fecha": "2025", "foto": "images/arrunchar.jpeg", "emoji": "🛋️"},
    {"titulo": "Beso", "desc": "Un beso que dice todo", "fecha": "2025", "foto": "images/beso.jpeg", "emoji": "💋"},
    {"titulo": "Cafecito", "desc": "Mañanas compartidas", "fecha": "2025", "foto": "images/cafecita.jpeg", "emoji": "☕"},
    {"titulo": "Muecas", "desc": "De las cosas que mas me enamoran", "fecha": "2025", "foto": "images/mueca.jpeg", "emoji": "😜"},
    {"titulo": "Muecas", "desc": "De las cosas que mas me enamoran pt. 2", "fecha": "2025", "foto": "images/mueca2.jpeg", "emoji": "😜"},
    {"titulo": "Muecas", "desc": "De las cosas que mas me enamoran pt. 3", "fecha": "2025", "foto": "images/muecas3.jpeg", "emoji": "😜"},
    {"titulo": "Copiloto de mi vida", "desc": "La única persona que quiero tener a mi lado en todos los momentos", "fecha": "2025", "foto": "images/copiloto.jpeg", "emoji": "👫"},
    {"titulo": "Ejercicio", "desc": "Cuando nos creemos fitnness", "fecha": "2025", "foto": "images/volcan.jpeg", "emoji": "🏋️"},
    {"titulo": "Yo", "desc": "Solo porque te gusta esta foto", "fecha": "2025", "foto": "images/yo.jpeg", "emoji": "😎"},
    {"titulo": "Tu", "desc": "Obviamente hay que poner a la churra", "fecha": "2025", "foto": "images/guapa.jpeg", "emoji": "😍"},
    {"titulo": "Momestafudiosa", "desc": "De las cosas que mas me dan miedo (aunque esta era de joda, vale la referencia)", "fecha": "2025", "foto": "images/momestafudiosa.jpeg", "emoji": "😱"},
    {"titulo": "Nuestra esencia", "desc": "Hacer el rídiculo juntos es de lo que se trata el amor", "fecha": "2025", "foto": "images/24diciembre.jpeg", "emoji": "🤪"},
    {"titulo": "Un helaito o que", "desc": "Jamas puede faltar un helado", "fecha": "2025", "foto": "images/heladotijerazo.jpeg", "emoji": "🍦"},
    ]

cols_polaroid = st.columns(3)
for i, rec in enumerate(recuerdos_fotos):
    with cols_polaroid[i % 3]:
        st.markdown(f'<div class="polaroid">', unsafe_allow_html=True)
        
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

# ========== 6. HORÓSCOPO ==========
st.subheader("🔮 Horóscopo de la relación (versión mágica)")
st.markdown("*El universo tiene mensajes para nosotros...*")

frases_largas = [
    ("💫", "✨✨✨", "El universo está conspirando a tu favor. Hoy es un día perfecto para compartir un helado y reír sin razón."),
    ("🌙", "🌙🌙🌙", "La luna en cuarto creciente ilumina tu lado más romántico. Aprovecha para escribirle una nota sorpresa."),
    ("🔥", "💖💖💖", "La pasión está en su punto máximo. Hoy cualquier excusa es buena para un abrazo largo y un beso espontáneo."),
    ("🍔", "🍔🍔🍔", "Los planetas predicen antojos compartidos. Algo te dice que terminarán pidiendo hamburguesas a altas horas."),
    ("🎵", "🎶🎶🎶", "Una canción especial sonará hoy y te hará recordar el momento en que supiste que era el indicado."),
    ("💌", "💌💌💌", "El cosmos quiere que le digas 'te quiero' sin razón aparente. No la pienses, solo hazlo.")
]

if "horoscopo_mostrado" not in st.session_state:
    st.session_state.horoscopo_mostrado = False
    st.session_state.horoscopo_actual = None

col_h1, col_h2, col_h3 = st.columns([1, 2, 1])
with col_h2:
    if st.button("✨ VER PREDICCIÓN DEL DÍA ✨", use_container_width=True):
        st.session_state.horoscopo_actual = random.choice(frases_largas)
        st.session_state.horoscopo_mostrado = True

if st.session_state.horoscopo_mostrado and st.session_state.horoscopo_actual:
    icono, decoracion, mensaje = st.session_state.horoscopo_actual
    st.markdown(f"""
    <div class="horoscopo-card">
        <div style="font-size: 3rem;">{icono} {decoracion} {icono}</div>
        <p style="font-size: 1.1rem; line-height: 1.5;">{mensaje}</p>
        <div style="font-size: 0.8rem; margin-top: 1rem;">✨ Confía en el universo ✨</div>
    </div>
    """, unsafe_allow_html=True)

st.divider()

# ========== 8. BOTÓN SORPRESA FINAL ==========
st.subheader("✨ El último detalle ✨")
st.markdown("*Presiona aquí para que la magia se haga presente...*")

if st.button("🕯️ Revelar la magia de nuestro amor", use_container_width=True):
    st.markdown("""
    <style>
    @keyframes caerPetalo {
        0% { transform: translateY(-50px) rotate(0deg); opacity: 1; }
        100% { transform: translateY(100vh) rotate(360deg); opacity: 0; }
    }
    .petalo {
        position: fixed;
        top: 0;
        font-size: 24px;
        animation: caerPetalo 4s linear forwards;
        pointer-events: none;
        z-index: 9999;
    }
    </style>
    <div class="petalo" style="left: 5%; animation-delay: 0s;">🌹</div>
    <div class="petalo" style="left: 15%; animation-delay: 0.5s;">🌸</div>
    <div class="petalo" style="left: 25%; animation-delay: 1s;">🌺</div>
    <div class="petalo" style="left: 35%; animation-delay: 0.2s;">🌷</div>
    <div class="petalo" style="left: 45%; animation-delay: 0.7s;">🌹</div>
    <div class="petalo" style="left: 55%; animation-delay: 1.2s;">🌸</div>
    <div class="petalo" style="left: 65%; animation-delay: 0.4s;">🌺</div>
    <div class="petalo" style="left: 75%; animation-delay: 0.9s;">🌷</div>
    <div class="petalo" style="left: 85%; animation-delay: 1.4s;">🌹</div>
    <div class="petalo" style="left: 95%; animation-delay: 0.6s;">🌸</div>
    """, unsafe_allow_html=True)
    st.markdown("""
    <div style="background: linear-gradient(135deg, #2C2626, #1E1A1A); padding: 1.5rem; border-radius: 20px; text-align: center; border: 2px solid #B54A4A;">
        <h3 style="color: #B54A4A;">✨ Eres la luz de mi vida ✨</h3>
        <p style="font-size: 1.1rem;">Gracias por este año increíble. Te amo más allá de las estrellas.</p>
        <p style="font-size: 0.9rem;">💖 Cada día a tu lado es un regalo del universo 💖</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("*🧩 Hecho con todo el amor del mundo, utilizando estadísticas, biología y mucha programación. 💻💖*")