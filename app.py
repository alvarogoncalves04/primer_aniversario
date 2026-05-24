import streamlit as st
from datetime import date

st.set_page_config(page_title="Primer Aniversario", page_icon="💖")

# CSS personalizado para fondo oscuro y texto blanco legible
st.markdown("""
<style>
    .stApp {
        background-color: #1E1A1A;
    }
    body, .stMarkdown, .stText, .stTitle, .stSubheader, 
    .stHeader, .stCaption, .stMetric, .stAlert, div, p, span, label {
        color: #FFFFFF !important;
    }
    .stButton button {
        background-color: #B54A4A !important;
        color: white !important;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: #8B3A3A !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #2C2626 !important;
    }
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    .js-plotly-plot .plotly .gtitle,
    .js-plotly-plot .plotly .xtitle,
    .js-plotly-plot .plotly .ytitle,
    .js-plotly-plot .plotly .legend text,
    .js-plotly-plot .plotly .annotation-text {
        fill: #FFFFFF !important;
        color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

st.title("💖 ¡Feliz Primer Aniversario, Victoria! 💖")
st.markdown("*Hoy celebramos 365 días de amor, risas y aprendizaje juntos. Donde hemos aprendido día a día a ser mejores personas, pareja, seres humanos"
"   hemos aprendido amarnos de la manera que nos llena, comunicarnos en nuestro lenguaje de muecas, y sobretodas las cosas  seguir adelante superando cualquier obstáculo*")
st.markdown("**¡Tengo imnumerables razones para amarte churri!**")

fecha_inicio = date(2025, 3, 3)
dias_juntos = (date.today() - fecha_inicio).days
st.metric("📅 Días desde que me robaste un beso en faces", dias_juntos)

# Foto de portada (más pequeña con primera foto juntos)
try:
    from PIL import Image
    img = Image.open("images/primerafotojuntos.jpeg")
    # Usar columnas para centrar y reducir tamaño
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, use_container_width=True)
        st.caption("💖 Nuestra primera foto juntos(decentes) 💖")
except:
    st.info("📸 Pronto pondré aquí nuestra foto favorita.")
if st.button("🎁 Haz clic para una sorpresa"):
    st.balloons()
    # Estrellas fugaces
    st.markdown("""
    <style>
    @keyframes estrellaFugaz {
        0% { transform: translate(0, 0) rotate(45deg); opacity: 1; }
        100% { transform: translate(300px, 300px) rotate(45deg); opacity: 0; }
    }
    .estrella-fugaz {
        position: fixed;
        font-size: 24px;
        animation: estrellaFugaz 2s ease-out forwards;
        pointer-events: none;
        z-index: 9999;
    }
    @keyframes flotarCorazones {
        0% { transform: translateY(0px) rotate(0deg); opacity: 1; }
        100% { transform: translateY(-150px) rotate(20deg); opacity: 0; }
    }
    .corazon-sorpresa {
        position: fixed;
        bottom: 0;
        font-size: 28px;
        animation: flotarCorazones 3s ease-out forwards;
        pointer-events: none;
        z-index: 9999;
    }
    </style>
    <div class="estrella-fugaz" style="top: 10%; left: 0%; animation-delay: 0s;">⭐</div>
    <div class="estrella-fugaz" style="top: 30%; left: 20%; animation-delay: 0.3s;">✨</div>
    <div class="estrella-fugaz" style="top: 50%; left: 10%; animation-delay: 0.6s;">🌟</div>
    <div class="estrella-fugaz" style="top: 70%; left: 30%; animation-delay: 0.9s;">💫</div>
    <div class="estrella-fugaz" style="top: 20%; left: 50%; animation-delay: 0.4s;">⭐</div>
    <div class="estrella-fugaz" style="top: 60%; left: 70%; animation-delay: 0.7s;">✨</div>
    <div class="corazon-sorpresa" style="left: 10%; animation-delay: 0s;">❤️</div>
    <div class="corazon-sorpresa" style="left: 25%; animation-delay: 0.4s;">💖</div>
    <div class="corazon-sorpresa" style="left: 40%; animation-delay: 0.8s;">💗</div>
    <div class="corazon-sorpresa" style="left: 55%; animation-delay: 0.2s;">💕</div>
    <div class="corazon-sorpresa" style="left: 70%; animation-delay: 0.6s;">💘</div>
    <div class="corazon-sorpresa" style="left: 85%; animation-delay: 1s;">💝</div>
    <div class="corazon-sorpresa" style="left: 95%; animation-delay: 0.3s;">💓</div>
    """, unsafe_allow_html=True)
    st.success("¡Te amo más que ayer y menos que mañana! 💕")
    

st.sidebar.title("📅 Nuestro primer año")
st.sidebar.info("Usa el menú de arriba para ver el dashboard, jugar o recibir una carta especial.")