import streamlit as st

st.title("🎮 ¿Cuánto sabes de nosotros?")
st.markdown("*Responde estas preguntas y demuestra lo bien que me conoces. ¡Ganas un abrazo si aciertas todas!*")

if "puntuacion" not in st.session_state:
    st.session_state.puntuacion = 0
    st.session_state.pregunta_actual = 0

preguntas = [
    {"pregunta": "¿Dónde fue nuestra primera cita?", 
     "opciones": ["Migas (Caracas)", "Café Olé", "Parque del Este", "Sambil"], 
     "respuesta": "Migas (Caracas)"},
    
    {"pregunta": "¿Qué comimos esa noche?", 
     "opciones": ["Pizza", "Hamburguesas de pollo crispy", "Sushi", "Pastel"], 
     "respuesta": "Hamburguesas de pollo crispy"},
    
    {"pregunta": "¿Cuál es mi comida favorita que cocinas?", 
     "opciones": ["Pasta", "Pizza casera", "Ensalada", "Tortilla de papas"], 
     "respuesta": "Pasta"},  # <-- cámbialo por lo real
    
    {"pregunta": "¿Cuál fue la primera serie que vimos juntos?", 
     "opciones": ["Friends", "La Casa de Papel", "The Office", "Game of Thrones"], 
     "respuesta": "Friends"},  # <-- cámbialo por la real
    
    {"pregunta": "¿Qué canción sonaba cuando nos conocimos?", 
     "opciones": ["Qué bonito - Bad Bunny", "Dákiti - Bad Bunny", "Amor Tumbado - Natanael Cano", "Hasta la raíz - Natalia Lafourcade"], 
     "respuesta": "Qué bonito - Bad Bunny"}  # <-- cámbialo por la real
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
    st.success(f"🎉 ¡Acertaste {st.session_state.puntuacion} de {len(preguntas)}!")
    if st.session_state.puntuacion == len(preguntas):
        st.balloons()
        st.write("💖 ¡Eres la persona que mejor me conoce! Te ganaste un abrazo eterno.")
    else:
        st.write("¡No te preocupes! Seguimos construyendo recuerdos. 💕")
    if st.button("Jugar de nuevo"):
        st.session_state.puntuacion = 0
        st.session_state.pregunta_actual = 0
        st.rerun()