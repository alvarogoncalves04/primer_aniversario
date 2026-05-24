import streamlit as st
from datetime import date

st.set_page_config(page_title="Mi sueño a tu lado ", page_icon="👨‍👩‍👧")

st.markdown("""
<style>
    .stApp {
        background-color: #1E1A1A;
    }
    .motivacion-card {
        background: linear-gradient(135deg, #2C2626, #3D2C2C);
        border-radius: 30px;
        padding: 2rem;
        text-align: center;
        border: 2px solid #B54A4A;
        box-shadow: 0 10px 30px rgba(0,0,0,0.3);
        margin: 1rem 0;
    }
    .frase-motivacion {
        font-size: 1.3rem;
        font-style: italic;
        color: #FFD700;
        margin-top: 1.5rem;
    }
    .autor {
        font-size: 0.9rem;
        color: #B54A4A;
        margin-top: 0.5rem;
    }
    .stButton button {
        background: linear-gradient(135deg, #B54A4A, #8B3A3A) !important;
        border: none !important;
        color: white !important;
    }
</style>
""", unsafe_allow_html=True)

# Título
st.markdown("""
<div style="text-align: center; margin-bottom: 2rem;">
    <div style="font-size: 3rem;">👨‍👩‍👧</div>
    <h1 style="color: #B54A4A;">Mi Sueño a tu Lado</h1>
    <p style="font-size: 1rem;">La razón por la que cada día me esfuerzo por ser mejor</p>
</div>
""", unsafe_allow_html=True)

# ========== FOTO FAMILIAR ==========
try:
    from PIL import Image
    img = Image.open("images/familia.jpeg")
    
    # Mostrar foto centrada y con tamaño reducido
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.image(img, use_container_width=True)
        st.caption(" Nuestra familia")
except:
    st.warning("📸 La foto familiar se cargará pronto...")

st.divider()

# ========== MENSAJE FINAL ==========
st.markdown("""
<div style="text-align: center; padding: 1rem;">
    <p style="font-size: 0.9rem;">Gracias por ser mi motivación, mi fuerza y mi razón para seguir adelante. Porque tener una familia a tu lado es todo lo que he soñado.</p>
    <p style="font-size: 0.8rem;">Cada día me esfuerzo por ser la mejor versión de mí mismo... por ti, por nosotros, por nuestra familia.</p>
</div>
""", unsafe_allow_html=True)

st.caption("*👨‍👩‍👧 Porque una familia unida es el tesoro más valioso.*")