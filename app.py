import streamlit as st
from datetime import date

st.set_page_config(page_title="Primer Aniversario", page_icon="💖")
st.markdown("""

<style>
    .stApp {
        background-color: #1A1414;
    }
    body, .stMarkdown, .stText, .stTitle, .stSubheader, 
    .stHeader, .stCaption, .stMetric, .stAlert, div, p, span, label {
        color: #FFEDED !important;
    }
    .stButton button {
        background-color: #8B2A45 !important;
        color: #FFEDED !important;
        border: none;
        border-radius: 8px;
        padding: 0.5rem 1rem;
    }
    .stButton button:hover {
        background-color: #A83452 !important;
        color: white !important;
    }
    section[data-testid="stSidebar"] {
        background-color: #2C1E22 !important;
    }
    section[data-testid="stSidebar"] * {
        color: #FFEDED !important;
    }
    .st-emotion-cache-1v0mbdj:first-child {
        display: none !important;
    }
</style>
""", unsafe_allow_html=True)
st.title("💖 ¡Feliz Primer Aniversario, Victoria! 💖")
st.markdown("*Hoy celebramos 365 días de amor, risas y aprendizaje juntos. Donde hemos aprendido día a día a ser mejores personas, pareja, seres humanos. Hemos aprendido amarnos de la manera que nos llena, comunicarnos en nuestro lenguaje de muecas, y sobretodas las cosas seguir adelante superando cualquier obstáculo*")
st.markdown("**¡Tengo innumerables razones para amarte churri!**")

fecha_inicio = date(2025, 2, 14)  # Fecha de inicio de la relación
dias_juntos = (date.today() - fecha_inicio).days
st.metric("📅 Días desde que me robaste un beso en faces", dias_juntos)

# Foto de portada
try:
    from PIL import Image
    img = Image.open("images/primerafotojuntos.jpeg")
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, use_container_width=True)
        st.caption("💖 Nuestra primera foto juntos 💖")
except:
    st.info("📸 Pronto pondré aquí nuestra foto favorita.")

if st.button("🎁 Haz clic para una sorpresa"):
    st.balloons()
    st.success("¡Te amo más que ayer y menos que mañana! 💕")   