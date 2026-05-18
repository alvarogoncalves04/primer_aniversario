import streamlit as st

st.set_page_config(page_title="Mi Regalo", page_icon="💖")
st.title("💖 ¡Feliz Primer Aniversario! 💖")
st.write("Esto es solo una prueba. Pronto añadiremos más cosas.")

if st.button("Haz clic para una sorpresa"):
    st.balloons()
    st.snow()