import streamlit as st
import random

st.set_page_config(page_title="🎮 El Juego del Amor", page_icon="🎮")

# CSS personalizado para la página del juego
st.markdown("""
<style>
    .game-header {
        text-align: center;
        padding: 1rem;
        background: linear-gradient(135deg, #2C2626, #3D2C2C);
        border-radius: 20px;
        margin-bottom: 2rem;
        border: 1px solid #B54A4A;
    }
    .question-card {
        background-color: #2C2626;
        border-radius: 20px;
        padding: 1.5rem;
        margin: 1rem 0;
        border-left: 8px solid #B54A4A;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
    }
    .pista-box {
        background-color: #3D2C2C;
        border-radius: 15px;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border: 1px dashed #B54A4A;
    }
    .score-badge {
        background-color: #B54A4A;
        border-radius: 50px;
        padding: 0.3rem 1rem;
        display: inline-block;
        font-weight: bold;
    }
    .feedback-correcto {
        background-color: #2E5C2E;
        border-radius: 10px;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-left: 5px solid #4CAF50;
    }
    .feedback-incorrecto {
        background-color: #5C2E2E;
        border-radius: 10px;
        padding: 0.8rem;
        margin: 0.5rem 0;
        border-left: 5px solid #F44336;
    }
    .stRadio > div {
        background-color: #3D2C2C;
        border-radius: 10px;
        padding: 0.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Header bonito
st.markdown("""
<div class="game-header">
    <h1>🎮 El Gran Juego de Nuestro Primer Año</h1>
    <p>✨ Responde estas preguntas y demuestra que me conoces… ¡o tendrás que pagar con un helado! ✨</p>
</div>
""", unsafe_allow_html=True)

# Inicializar estado del juego (TODOS los atributos)
if "puntuacion" not in st.session_state:
    st.session_state.puntuacion = 0
    st.session_state.pregunta_actual = 0
    st.session_state.respuestas_usuario = []
    st.session_state.feedback = ""
    st.session_state.feedback_tipo = ""
    st.session_state.juego_terminado = False  # <--- INICIALIZADO

# Banco de preguntas
preguntas = [
    {
        "pregunta": "¿Dónde fue nuestra primera cita?",
        "opciones": ["🍔 Migas (Caracas)", "🏊‍♀️ En la piscina", "🎬 En el cine", "🏠 En mi casa"],
        "respuesta": "🍔 Migas (Caracas)",
        "pista": "🍔 Había hamburguesas crispy de por medio y mucha nervia."
    },
    {
        "pregunta": "¿Qué comimos esa noche?",
        "opciones": ["🍔 Hamburguesas de pollo crispy", "🌭 Perros calientes", "🍣 Sushi", "🍕 Pizza"],
        "respuesta": "🍔 Hamburguesas de pollo crispy",
        "pista": "🍗 Crujientes, deliciosas y compartimos papas."
    },
    {
        "pregunta": "¿Cuál fue la primera canción que sonó en nuestro primer beso?",
        "opciones": ["🎵 Qué bonito - Bad Bunny", "🎵 El himno nacional", "🎵 Una canción de cuna", "🎵 Estábamos en silencio"],
        "respuesta": "🎵 Qué bonito - Bad Bunny",
        "pista": "🎤 El conejo malo y romántico sonaba de fondo."
    },
    {
        "pregunta": "¿Cuántos helados crees que hemos compartido (aproximadamente)?",
        "opciones": ["🍦 Menos de 5", "🍦 Entre 15 y 30", "🍦 Más de 50 (somos unos viciosos)", "🍦 No llevamos la cuenta"],
        "respuesta": "🍦 Más de 50 (somos unos viciosos)",
        "pista": "🍨 Tú eres team chocolate con menta, yo team cookies."
    },
    {
        "pregunta": "¿Cuál es mi apodo secreto para ti cuando te pones cariñosa?",
        "opciones": ["🐻 Mi osita", "💃 Mi chama loca", "❤️ Mi vida", "👑 Mi reina"],
        "respuesta": "💃 Mi chama loca",
        "pista": "🤪 Tiene que ver con tu personalidad alborotada y venezolana."
    },
    {
        "pregunta": "¿Qué día fue nuestra primera cita?",
        "opciones": ["📅 14 de febrero", "📅 3 de marzo", "📅 20 de marzo", "📅 10 de junio"],
        "respuesta": "📅 3 de marzo",
        "pista": "🗓️ Un día después del carnaval, el 3/3."
    },
    {
        "pregunta": "¿Cuál es nuestro lugar favorito para arrunchar?",
        "opciones": ["🛋️ El sofá de tu casa", "🛏️ Mi cama", "🎬 El cine", "🌳 El parque"],
        "respuesta": "🛋️ El sofá de tu casa",
        "pista": "🛋️ Donde vemos series hasta que el sueño nos vence."
    }
]

total = len(preguntas)

# Barra de progreso con estilo
st.markdown(f"""
<div style="margin: 1rem 0;">
    <div style="display: flex; justify-content: space-between; margin-bottom: 0.5rem;">
        <span>📊 Progreso</span>
        <span class="score-badge">{st.session_state.pregunta_actual} de {total}</span>
    </div>
</div>
""", unsafe_allow_html=True)

progreso = st.session_state.pregunta_actual / total if total > 0 else 0
st.progress(progreso)

# Si aún quedan preguntas y el juego no ha terminado
if st.session_state.pregunta_actual < total and not st.session_state.juego_terminado:
    p = preguntas[st.session_state.pregunta_actual]
    
    # Tarjeta de pregunta
    st.markdown(f"""
    <div class="question-card">
        <h3 style="color: #B54A4A; margin-bottom: 1rem;">❓ {p['pregunta']}</h3>
    </div>
    """, unsafe_allow_html=True)
    
    # Pista
    with st.expander("🔍 ¿Necesitas una pista? (no es trampa, es ayuda)"):
        st.markdown(f'<div class="pista-box">💡 {p["pista"]}</div>', unsafe_allow_html=True)
        st.caption("📌 Usa la pista si te atoras... pero perderás el chance de presumir.")
    
    # Opciones
    respuesta_usuario = st.radio(
        "Elige tu respuesta:",
        p["opciones"],
        key=f"q{st.session_state.pregunta_actual}",
        label_visibility="collapsed"
    )
    
    # Botón responder
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("✅ RESPONDER", use_container_width=True, type="primary"):
            if respuesta_usuario == p["respuesta"]:
                st.session_state.puntuacion += 1
                st.session_state.feedback = "🎉 ¡CORRECTA! Eres la mejor conocedora de mí. ¡Te ganaste un beso! 🎉"
                st.session_state.feedback_tipo = "correcto"
                st.balloons()
            else:
                st.session_state.feedback = f"😅 ¡UPS! La respuesta correcta era: **{p['respuesta']}**. ¡Me debes un helado! 🍦"
                st.session_state.feedback_tipo = "incorrecto"
            st.session_state.pregunta_actual += 1
            st.rerun()
    
    # Mostrar feedback
    if st.session_state.feedback:
        clase_feedback = "feedback-correcto" if st.session_state.feedback_tipo == "correcto" else "feedback-incorrecto"
        st.markdown(f'<div class="{clase_feedback}">{st.session_state.feedback}</div>', unsafe_allow_html=True)
        st.session_state.feedback = ""

else:
    # Juego terminado
    if not st.session_state.juego_terminado:
        st.session_state.juego_terminado = True
    
    st.balloons()
    
    st.markdown("### 🎊 ¡JUEGO COMPLETADO! 🎊")
    
    if st.session_state.puntuacion == total:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #2E5C2E, #1E3A1E); border-radius: 20px; padding: 2rem; text-align: center; margin: 1rem 0;">
            <h1 style="color: #FFD700;">💖 ¡PERFECTO! 💖</h1>
            <h2 style="color: #FFD700;">¡Eres la persona que mejor me conoce!</h2>
            <p style="font-size: 1.2rem;">Te has ganado un <strong>BESO ETERNO</strong> y un helado pagado por mí. 🍦</p>
            <p style="font-size: 1.5rem;">🎉🏆🎉</p>
        </div>
        """, unsafe_allow_html=True)
    elif st.session_state.puntuacion >= total - 2:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #3D2C2C, #2C1E1E); border-radius: 20px; padding: 2rem; text-align: center; margin: 1rem 0;">
            <h2 style="color: #FFB6C1;">🌟 ¡CASI PERFECTA! 🌟</h2>
            <p>Fallaste muy pocas. Te invito un helado igual. ¡Te quiero mucho!</p>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown("""
        <div style="background: linear-gradient(135deg, #3D2C2C, #2C1E1E); border-radius: 20px; padding: 2rem; text-align: center; margin: 1rem 0;">
            <h2 style="color: #FFB6C1;">😘 ¡NO PASA NADA! 😘</h2>
            <p>Aún nos quedan muchos años para que me conozcas mejor. ¡Te quiero igual, mi chama loca!</p>
        </div>
        """, unsafe_allow_html=True)
    
    st.metric("🎯 Puntuación final", f"{st.session_state.puntuacion} / {total}")
    
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        if st.button("🔄 JUGAR DE NUEVO", use_container_width=True):
            st.session_state.puntuacion = 0
            st.session_state.pregunta_actual = 0
            st.session_state.respuestas_usuario = []
            st.session_state.feedback = ""
            st.session_state.feedback_tipo = ""
            st.session_state.juego_terminado = False
            st.rerun()

# Sidebar
st.sidebar.markdown("## 📊 Estadísticas del juego")
st.sidebar.metric("🏆 Puntaje actual", f"{st.session_state.puntuacion} / {total}")
progreso_sidebar = st.session_state.puntuacion / total if total > 0 else 0
st.sidebar.progress(progreso_sidebar)

if st.session_state.puntuacion == total and total > 0:
    st.sidebar.success("💖 ¡CAMPEONA! 💖")
elif st.session_state.puntuacion >= total - 2 and total > 0:
    st.sidebar.info("🌟 ¡Vas excelente! 🌟")
elif st.session_state.pregunta_actual > 0:
    st.sidebar.info("💪 ¡Sigue así, campeona! 💪")

st.sidebar.markdown("---")
st.sidebar.caption("💡 **Tip:** Si no sabes una respuesta, usa la pista.")
st.sidebar.caption("🍦 **Premio:** Si aciertas todas, te invito un helado.")