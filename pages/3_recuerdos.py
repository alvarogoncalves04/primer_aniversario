import streamlit as st
import random
from datetime import date, datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64

st.set_page_config(page_title="Rincón de Recuerdos", page_icon="🎉")

# CSS mejorado
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
        transition: all 0.3s !important;
    }
    .stButton button:hover {
        transform: scale(1.02);
        box-shadow: 0 5px 15px rgba(181,74,74,0.4) !important;
    }
    
    .horoscopo-card {
        background: linear-gradient(135deg, #2C2626, #1E1A1A);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        border: 2px solid #B54A4A;
        box-shadow: 0 0 20px rgba(181,74,74,0.2);
    }
    
    .stProgress > div > div {
        background: linear-gradient(90deg, #B54A4A, #FF6B6B) !important;
    }
    
    .sintonia-card {
        background: linear-gradient(135deg, #2C2626, #1E1A1A);
        border-radius: 20px;
        padding: 1.5rem;
        text-align: center;
        border: 2px solid #FFD700;
        box-shadow: 0 0 20px rgba(255,215,0,0.3);
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
proximo_aniversario = date(2027, 3, 3)
hoy = date.today()
dias_restantes = (proximo_aniversario - hoy).days

col_timer1, col_timer2, col_timer3 = st.columns([1, 2, 1])
with col_timer2:
    if dias_restantes > 0:
        st.metric("⏳ Días para nuestro segundo aniversario", dias_restantes, delta=None)
        st.progress(1 - dias_restantes/365, text="📅 Progreso del año en curso")
    else:
        st.success("🎂 ¡HOY ES NUESTRO ANIVERSARIO! 🎂")

st.divider()

# ========== 2. MURAL DE PIROPOS Y AGRADECIMIENTOS ==========
st.subheader("💬 Mural de piropos y cosas por las que estoy agradecido")
st.markdown("*Pequeñas razones que me hacen amarte cada día más...*")

piropos = [
    "💖 Gracias por enseñarme que el amor se demuestra con acciones, no solo con palabras.",
    "🌹 Gracias por aguantar mis chistes malos y reírte de ellos como si fueran buenos.",
    "✨ Gracias por ser tú, auténtica, real y sin filtros.",
    "💕 Gracias por cada 'te quiero' inesperado que me saca una sonrisa tonta.",
    "🌸 Gracias por las tardes de helado y las mañanas de café compartido.",
    "🎵 Gracias por ser la musa que inspira cada uno de mis días.",
    "💪 Gracias por estar a mi lado en los días grises y celebrar los brillantes.",
    "🍔 Gracias por esa primera cita en Migas que cambió mi vida para siempre.",
    "💖 Eres mi persona favorita en el universo entero.",
    "🌙 Contigo hasta la luna y nunca quiero volver.",
    "✨ Cada día a tu lado es un nuevo capítulo de nuestra historia de amor.",
    "💕 Gracias por hacerme sentir el hombre más afortunado del mundo."
]

# Mostrar piropos en un carrusel manual (3 columnas)
cols_piropos = st.columns(3)
for i, piropo in enumerate(piropos):
    with cols_piropos[i % 3]:
        st.markdown(f"""
        <div class="piropo-card">
            {piropo}
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ========== 3. LÍNEA DE TIEMPO (10 eventos para que edites) ==========
st.subheader("📅 Línea de tiempo de nuestros momentos épicos")
st.markdown("*Desliza sobre cada evento para ver el detalle*")

timeline = [
    ("3 Mar 2025", "⭐ Nuestra primera cita en Migas", "Hamburguesas, risas y electricidad en el aire."),
    ("DD MMM AAAA", "📝 Evento 2 - Edítame", "Descripción del evento 2"),
    ("DD MMM AAAA", "📝 Evento 3 - Edítame", "Descripción del evento 3"),
    ("DD MMM AAAA", "📝 Evento 4 - Edítame", "Descripción del evento 4"),
    ("DD MMM AAAA", "📝 Evento 5 - Edítame", "Descripción del evento 5"),
    ("DD MMM AAAA", "📝 Evento 6 - Edítame", "Descripción del evento 6"),
    ("DD MMM AAAA", "📝 Evento 7 - Edítame", "Descripción del evento 7"),
    ("DD MMM AAAA", "📝 Evento 8 - Edítame", "Descripción del evento 8"),
    ("DD MMM AAAA", "📝 Evento 9 - Edítame", "Descripción del evento 9"),
    ("3 Mar 2026", "💖 Primer aniversario", "Hoy celebramos este año increíble. ¡Te amo más que nunca!")
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

# ========== 5. MURO POLAROID CON TODAS LAS FOTOS ==========
st.subheader("🖼️ Muro de recuerdos (Polaroids)")
st.markdown("*Nuestros momentos favoritos en formato vintage. Pasa el mouse para ver el efecto.*")

recuerdos_fotos = [
    {"titulo": "Primera cita en Migas", "desc": "Hamburguesas crispy", "fecha": "Mar 2025", "foto": "images/primeracita.jpeg", "emoji": "🍔"},
    {"titulo": "Primera foto juntos", "desc": "Nuestro primer selfie", "fecha": "Mar 2025", "foto": "images/primerafotojuntos.jpeg", "emoji": "📷"},
    {"titulo": "Noche de sushi", "desc": "Compartiendo comida", "fecha": "Abr 2025", "foto": "images/sushi.jpeg", "emoji": "🍣"},
    {"titulo": "En nuestra casa", "desc": "Nuestro refugio", "fecha": "May 2025", "foto": "images/micasa.jpeg", "emoji": "🏠"},
    {"titulo": "Nocturneando", "desc": "Aventuras de noche", "fecha": "Jun 2025", "foto": "images/nocturneando.jpeg", "emoji": "🌙"},
    {"titulo": "Navidad juntos", "desc": "Celebrando en familia", "fecha": "Dic 2025", "foto": "images/24diciembre.jpeg", "emoji": "🎄"},
    {"titulo": "San Valentín", "desc": "Nuestro primer 14F", "fecha": "Feb 2026", "foto": "images/14febrero.jpeg", "emoji": "💖"},
    {"titulo": "Enamorados", "desc": "Así nos sentimos", "fecha": "Siempre", "foto": "images/enamorados.jpeg", "emoji": "💕"},
    {"titulo": "Gaitas venezolanas", "desc": "Tradición y amor", "fecha": "Dic 2025", "foto": "images/gaitas.jpeg", "emoji": "🎶"},
    {"titulo": "Arrunchando", "desc": "Nuestro momento favorito", "fecha": "2025", "foto": "images/arrunchar.jpeg", "emoji": "🛋️"},
    {"titulo": "Beso", "desc": "Un beso que dice todo", "fecha": "2025", "foto": "images/beso.jpeg", "emoji": "💋"},
    {"titulo": "Cafecito", "desc": "Mañanas compartidas", "fecha": "2025", "foto": "images/cafecita.jpeg", "emoji": "☕"}
]

cols_polaroid = st.columns(3)
for i, rec in enumerate(recuerdos_fotos):
    with cols_polaroid[i % 3]:
        st.markdown(f'<div class="polaroid">', unsafe_allow_html=True)
        
        if rec["foto"]:
            try:
                from PIL import Image
                img = Image.open(rec["foto"])
                st.image(img, use_container_width=True)
            except:
                st.markdown(f"<div style='font-size: 3rem; text-align:center;'>{rec['emoji']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div style='font-size: 3rem; text-align:center;'>{rec['emoji']}</div>", unsafe_allow_html=True)
        
        st.markdown(f"""
            <strong>{rec['titulo']}</strong><br>
            <span style="font-size:0.8rem;">{rec['desc']}</span><br>
            <span style="font-size:0.7rem; color:#7A5A5A;">{rec['fecha']}</span>
        </div>
        """, unsafe_allow_html=True)

st.divider()

# ========== 6. HORÓSCOPO (con frases y sin problemas de persistencia) ==========
st.subheader("🔮 Horóscopo de la relación (versión mágica)")
st.markdown("*El universo tiene mensajes para nosotros...*")

frases_largas = [
    ("💫", "✨✨✨", "El universo está conspirando a tu favor. Hoy es un día perfecto para compartir un helado y reír sin razón."),
    ("🌙", "🌙🌙🌙", "La luna en cuarto creciente ilumina tu lado más romántico. Aprovecha para escribirle una nota sorpresa."),
    ("🔥", "💖💖💖", "La pasión está en su punto máximo. Hoy cualquier excusa es buena para un abrazo largo y un beso espontáneo."),
    ("🍔", "🍔🍔🍔", "Los planetas predicen antojos compartidos. Algo te dice que terminarán pidiendo hamburguesas a altas horas."),
    ("🎵", "🎶🎶🎶", "Una canción especial sonará hoy y te hará recordar el momento en que supiste que era el indicado."),
    ("💌", "💌💌💌", "El cosmos quiere que le digas 'te quiero' sin razón aparente. No la pienses, solo hazlo."),
    ("🐧", "🐧🐧🐧", "Como los pingüinos, su amor es para siempre. Hoy es un buen día para planear una nueva aventura juntos."),
    ("🌞", "☀️☀️☀️", "El sol brilla con fuerza hoy, igual que su amor. Aprovechen para salir juntos y crear un nuevo recuerdo."),
    ("🍦", "🍦🍦🍦", "Los astros predicen un antojo de helado en pareja. No lo duden, vayan por uno y disfruten."),
    ("🎁", "🎁🎁🎁", "El universo tiene una sorpresa preparada para ustedes hoy. Presten atención a las pequeñas señales."),
    ("💎", "💎💎💎", "Su relación es más valiosa que cualquier tesoro. Hoy es un buen día para recordar todo lo que han construido."),
    ("🕯️", "🕯️🕯️🕯️", "La llama del amor brilla con fuerza. Manténganla encendida con pequeños gestos de cariño."),
    ("🎈", "🎈🎈🎈", "La alegría está en el aire. Celebren su amor con una pequeña aventura, aunque sea pedir su comida favorita."),
    ("🌟", "🌟🌟🌟", "Hoy eres su estrella favorita y él la tuya. No olviden decírselo con una mirada, un beso o un abrazo."),
    ("💪", "💪💪💪", "Han superado cada obstáculo juntos. El universo les sonríe por su fortaleza como pareja.")
]

# Inicializar estado del horóscopo
if "horoscopo_mostrado" not in st.session_state:
    st.session_state.horoscopo_mostrado = False
    st.session_state.horoscopo_actual = None
    st.session_state.mensaje_mostrado = ""

col_h1, col_h2, col_h3 = st.columns([1, 2, 1])
with col_h2:
    if st.button("✨ VER PREDICCIÓN DEL DÍA ✨", use_container_width=True):
        st.session_state.horoscopo_actual = random.choice(frases_largas)
        st.session_state.horoscopo_mostrado = True

# Mostrar horóscopo si existe en session_state
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

# ========== 7. SINTONÍA DE NUESTRO AMOR ==========

st.subheader("🎵 La sintonía de nuestro amor")

st.markdown("""
<div class="sintonia-card">
    <div style="font-size: 3rem;">🎤🎶💖</div>
    <h3 style="color: #FFD700;">Mi Niña Bonita - Chino & Nacho</h3>
    <p style="font-size: 1rem;">"Eres tú, mi niña bonita, la que me quita las penas, la que me llena el alma de amor..."</p>
</div>
""", unsafe_allow_html=True)

if st.button("🎵 ESCUCHAR LA SINTONÍA DE NUESTRO AMOR 🎵", use_container_width=True):
    # iframe que solo reproduce el audio (embed de YouTube sin controles de video)
    st.html("""
    <iframe width="0" height="0" src="https://www.youtube.com/embed/5kPk1Qy7V8M?autoplay=1" 
            style="display:none" allow="autoplay"></iframe>
    """)
    st.success("🎶 ¡Disfruta nuestra canción! Se está reproduciendo en segundo plano. 🎶")

# ========== 8. BOTÓN SORPRESA FINAL (SIN GLOBOS) ==========
st.subheader("✨ El último detalle ✨")
st.markdown("*Presiona aquí para que la magia se haga presente...*")

if st.button("🕯️ Revelar la magia de nuestro amor", use_container_width=True):
    # Pétalos de rosa (sin globos)
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
        <p style="font-size: 0.8rem; margin-top: 1rem;">🎵 Y cada día me enamoro más de ti, mi niña bonita 🎵</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("---")
st.caption("*Hecho con todo el amor del mundo, utilizando estadísticas, biología y mucha programación. 💻💖*")