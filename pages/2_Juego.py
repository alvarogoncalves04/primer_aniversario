import streamlit as st
import random

st.set_page_config(page_title="Juego del Amor", page_icon="🎮")

st.title("🎮 El Gran Juego de Nuestro Primer Año")
st.markdown("*Responde estas preguntas y demuestra que me conoces… ¡o tendrás que pagar con un helado! 🍦*")

# Inicializar estado del juego
if "puntuacion" not in st.session_state:
    st.session_state.puntuacion = 0
    st.session_state.pregunta_actual = 0
    st.session_state.respuestas_usuario = []
    st.session_state.feedback = ""

# Banco de preguntas (más graciosas y románticas)
preguntas = [
    {
        "pregunta": "¿Dónde fue nuestra primera cita?",
        "opciones": ["Migas (Caracas)", "Un callejón oscuro", "La luna", "Tu casa sin querer"],
        "respuesta": "Migas (Caracas)",
        "pista": "🍔 Pista: había hamburguesas crispy de por medio."
    },
    {
        "pregunta": "¿Qué comimos esa noche?",
        "opciones": ["Hamburguesas de pollo crispy", "Una ensalada aburrida", "Sopa de sobre", "Pizza con piña (aberración)"],
        "respuesta": "Hamburguesas de pollo crispy",
        "pista": "🍗 Pista: crujientes y deliciosas."
    },
    {
        "pregunta": "¿Cuál fue la primera canción que sonó en nuestro primer beso?",
        "opciones": ["Qué bonito - Bad Bunny", "El himno nacional", "Una canción de cuna", "Ninguna, estábamos en silencio"],
        "respuesta": "Qué bonito - Bad Bunny",
        "pista": "🎵 Pista: el conejo malo y romántico."
    },
    {
        "pregunta": "¿Cuántos helados crees que hemos compartido (aproximadamente)?",
        "opciones": ["Menos de 5 (mentira)", "Entre 15 y 30", "Más de 50 (somos unos viciosos)", "No llevamos la cuenta, pero muchos"],
        "respuesta": "Más de 50 (somos unos viciosos)",
        "pista": "🍦 Pista: eres adicta al chocolate con menta."
    },
    {
        "pregunta": "¿Cuál es mi apodo secreto para ti cuando te pones cariñosa?",
        "opciones": ["Mi osita", "Mi chama loca", "Mi vida", "Mi pana (pero con ojitos)"],
        "respuesta": "Mi chama loca",  # <-- cámbialo por el real
        "pista": "🤪 Pista: tiene que ver con tu personalidad alborotada."
    }
]

total = len(preguntas)

# Mostrar barra de progreso
progreso = st.session_state.pregunta_actual / total
st.progress(progreso, text=f"Pregunta {st.session_state.pregunta_actual} de {total}")

# Si aún quedan preguntas
if st.session_state.pregunta_actual < total:
    p = preguntas[st.session_state.pregunta_actual]
    st.subheader(f"❓ {p['pregunta']}")
    
    # Mostrar pista en un recuadro
    with st.expander("🔍 ¿Necesitas una pista?"):
        st.info(p["pista"])
    
    # Opciones en un radio button con estilo
    respuesta_usuario = st.radio(
        "Elige tu respuesta:",
        p["opciones"],
        key=f"q{st.session_state.pregunta_actual}",
        label_visibility="collapsed"
    )
    
    col1, col2 = st.columns([1, 4])
    with col1:
        if st.button("✅ Responder", use_container_width=True):
            if respuesta_usuario == p["respuesta"]:
                st.session_state.puntuacion += 1
                st.session_state.feedback = "🎉 ¡Correcta! Eres la mejor conocedora de mí."
                st.balloons()
            else:
                st.session_state.feedback = f"😅 ¡Ups! La respuesta correcta era: **{p['respuesta']}**. Te gano un helado."
            st.session_state.pregunta_actual += 1
            st.rerun()
    
    # Mostrar feedback de la pregunta anterior si existe
    if st.session_state.feedback:
        st.markdown(f"<div style='background-color:#2C2626; padding:10px; border-radius:10px;'>{st.session_state.feedback}</div>", unsafe_allow_html=True)
        st.session_state.feedback = ""
else:
    # Juego terminado
    st.balloons()
    st.snow()
    st.success(f"🎊 ¡Has acertado {st.session_state.puntuacion} de {total} preguntas! 🎊")
    
    if st.session_state.puntuacion == total:
        st.markdown("## 💖 ¡Eres la persona que mejor me conoce! 💖")
        st.markdown("Te has ganado un **beso eterno** y un helado pagado por mí. 🍦")
        st.image("https://media.giphy.com/media/3o7abB06u9bNzA8LC8/giphy.gif", width=300)
    elif st.session_state.puntuacion >= total-1:
        st.markdown("🌟 ¡Casi perfecta! Solo fallaste una. Te invito un helado igual. 🌟")
    else:
        st.markdown("😜 No pasa nada, aún nos quedan muchos años para que me conozcas mejor. ¡Te quiero igual! 😜")
    
    if st.button("🔄 Jugar de nuevo (y vengarte)"):
        st.session_state.puntuacion = 0
        st.session_state.pregunta_actual = 0
        st.session_state.respuestas_usuario = []
        st.rerun()

# Barra lateral con el marcador
st.sidebar.markdown("## 📊 Marcador")
st.sidebar.metric("Puntos acumulados", f"{st.session_state.puntuacion} / {total}")
st.sidebar.progress(st.session_state.puntuacion / total if total>0 else 0)
st.sidebar.info("💡 Consejo: si no sabes una respuesta, pide pista (¡pero perderás la oportunidad de presumir!)")