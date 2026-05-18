import streamlit as st

st.title("🎮 ¿Cuánto sabes de nosotros?")

if "puntuacion" not in st.session_state:
    st.session_state.puntuacion = 0
    st.session_state.pregunta_actual = 0

preguntas = [
    {"pregunta": "¿Dónde fue nuestra primera cita?", 
     "opciones": ["Migas", "Cine", "Parque del Este", "Sambil", "Tolón", "Asousa"], 
     "respuesta": "Migas"},
    {"pregunta": "¿Qué comimos ese día?", 
     "opciones": ["Pizza", "Hamburguesas de pollo crispy", "Sushi", "perros calientes", "Ensalada", "Otro"], 
     "respuesta": "Hamburguesas de pollo crispy"}
]

if st.session_state.pregunta_actual < len(preguntas):
    p = preguntas[st.session_state.pregunta_actual]
    respuesta = st.radio(p["pregunta"], p["opciones"])
    if st.button("Siguiente"):
        if respuesta == p["respuesta"]:
            st.session_state.puntuacion += 1
        st.session_state.pregunta_actual += 1
        st.rerun()
else:
    st.success(f"¡Acertaste {st.session_state.puntuacion} de {len(preguntas)}!")
    if st.session_state.puntuacion == len(preguntas):
        st.balloons()
    if st.button("Jugar de nuevo"):
        st.session_state.puntuacion = 0
        st.session_state.pregunta_actual = 0
        st.rerun()