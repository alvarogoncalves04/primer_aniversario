import streamlit as st
from datetime import date

st.set_page_config(page_title="Primer Aniversario", page_icon="💖")

# CSS personalizado para fondo oscuro y texto blanco legible
st.markdown("""
<style>
    /* Fondo general oscuro */
    .stApp {
        background-color: #1E1A1A;
    }
    /* Todos los textos en blanco */
    body, .stMarkdown, .stText, .stTitle, .stSubheader, 
    .stHeader, .stCaption, .stMetric, .stAlert, div, p, span, label {
        color: #FFFFFF !important;
    }
    /* Botones con color vino */
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
    /* Sidebar oscura */
    section[data-testid="stSidebar"] {
        background-color: #2C2626 !important;
    }
    section[data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }
    /* Gráficas de Plotly - texto blanco */
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
st.markdown("*Hoy celebramos 365 días de amor, risas y aprendizaje juntos.*")
st.markdown("**¡Qué chévere haber llegado hasta aquí, mi pana del alma!**")

# Fecha de inicio (cámbiala si es otra)
fecha_inicio = date(2025, 2, 14)  # 14 de febrero de 2025
dias_juntos = (date.today() - fecha_inicio).days
st.metric("📅 Días desde que nos conocimos en Migas", dias_juntos)

# Imagen de portada (si ya tienes una foto en images/portada.jpg)
try:
    from PIL import Image
    img = Image.open("images/portada.jpg")
    st.image(img, use_column_width=True)
except:
    st.info("📸 Pronto pondré aquí nuestra foto favorita.")

if st.button("🎁 Haz clic para una sorpresa"):
    st.balloons()
    st.snow()
    st.success("¡Te amo más que ayer y menos que mañana! 💕")

st.sidebar.title("📅 Nuestro primer año")
st.sidebar.info("Usa el menú de arriba para ver el dashboard, jugar o recibir una carta especial.")