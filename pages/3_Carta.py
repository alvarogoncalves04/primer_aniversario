import streamlit as st
from datetime import datetime

st.set_page_config(page_title="Carta de Aniversario", page_icon="💌")

# Estilo CSS para simular papel de carta
st.markdown("""
<style>
    .carta-container {
        background-color: #FFF8F0;
        padding: 2rem;
        border-radius: 20px;
        box-shadow: 0 10px 25px rgba(0,0,0,0.2);
        font-family: 'Georgia', serif;
        color: #3E2A2A;
        border: 1px solid #D4A5A5;
        margin: 20px 0;
    }
    .carta-titulo {
        font-size: 2rem;
        text-align: center;
        font-weight: bold;
        margin-bottom: 1rem;
        color: #B54A4A;
    }
    .carta-fecha {
        text-align: right;
        font-style: italic;
        margin-bottom: 1.5rem;
        color: #7A5A5A;
    }
    .carta-contenido {
        font-size: 1.1rem;
        line-height: 1.6;
        text-align: justify;
        white-space: pre-wrap;
    }
    .sobre {
        text-align: center;
        font-size: 5rem;
        cursor: pointer;
        padding: 2rem;
        background-color: #2C2626;
        border-radius: 20px;
        transition: transform 0.3s;
    }
    .sobre:hover {
        transform: scale(1.05);
    }
</style>
""", unsafe_allow_html=True)

st.title("💌 Una carta de corazón a corazón")
st.markdown("*Hoy te escribo estas palabras, porque a veces el amor se cuenta mejor con tinta y papel.*")

# Inicializar estado de la carta (abierta o cerrada)
if "carta_abierta" not in st.session_state:
    st.session_state.carta_abierta = False

# Mostrar sobre cerrado si no se ha abierto
if not st.session_state.carta_abierta:
    st.markdown("""
    <div class="sobre">
        📬
        <p style="font-size: 1rem; margin-top: 0.5rem;">Haz clic en el botón para abrir tu carta</p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📨 Abrir carta mágica"):
        st.session_state.carta_abierta = True
        st.rerun()
else:
    # Carta desplegada
    st.markdown("""
    <div class="carta-container">
        <div class="carta-titulo">Para mi amor en nuestro primer aniversario</div>
        <div class="carta-fecha">Caracas, {fecha}</div>
        <div class="carta-contenido">
        {contenido}
        </div>
        <div style="margin-top: 2rem; text-align: right;">
        Con todo mi corazón,<br>
        Tu compañero
        </div>
    </div>
    """.format(
        fecha=datetime.now().strftime("%d de %B de %Y"),
        contenido="""
        Mi vida,

        Hoy, al mirar hacia atrás y ver todo lo que hemos caminado juntos, no puedo evitar sonreír como un niño. 
        Un año parece mucho y nada a la vez. Mucho porque en estos 365 días hemos llenado cada rincón de recuerdos inolvidables: 
        las hamburguesas crispy en Migas, las tardes de helado en el parque, las series que vimos abrazados hasta que el sueño nos venció.
        Nada porque contigo el tiempo vuela, y siento que fue ayer cuando te vi por primera vez y supe que algo especial iba a pasar.

        Eres la persona que le dio color a mis estadísticas, la que convirtió mis gráficos de barras en latidos, 
        la que me enseñó que la biología del amor se escribe con mayúsculas. 
        Gracias por cada abrazo, cada risa, cada discusión tonta que terminó en un beso. 
        Gracias por ser mi calma en el caos y mi aventura en la rutina.

        Este es solo el primer capítulo de una historia que apenas empieza. 
        Te prometo seguir llenando páginas de momentos felices, de viajes, de helados compartidos, 
        de conversaciones hasta tarde y de silencios cómplices.

        Feliz primer aniversario, mi chama loca. Te amo más de lo que las palabras pueden escribir.

        Con cariño infinito,
        Tu pana del alma 💖
        """
    ), unsafe_allow_html=True)
    
    st.download_button("📥 Descargar esta carta como archivo de texto", 
                       data="Para mi amor en nuestro primer aniversario\n\n" +
                            "Mi vida,\n\nHoy, al mirar atrás... (aquí va el texto completo)\n\nTe amo.",
                       file_name=f"carta_aniversario_{datetime.now().strftime('%Y%m%d')}.txt",
                       mime="text/plain")
    
    if st.button("💬 Quiero escribirle una carta de vuelta"):
        st.markdown("### ✍️ Escribe tu respuesta")
        respuesta = st.text_area("Tus palabras para él:", height=300)
        if st.button("Guardar y descargar respuesta"):
            if respuesta:
                st.download_button("Descargar tu carta", respuesta, "mi_respuesta.txt")
                st.success("¡Tu respuesta ha sido guardada! Se la entregarás en físico también, ¿verdad?")
            else:
                st.warning("Escribe algo antes de guardar.")
    
    if st.button("🔒 Cerrar carta (volver al sobre)"):
        st.session_state.carta_abierta = False
        st.rerun()