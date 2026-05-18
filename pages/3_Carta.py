import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Carta de Aniversario", page_icon="💌")
st.title("💌 Una carta especial para ti")
st.markdown("*Elige palabras que describan nuestro año y generaré una carta única.*")

# Palabras sugeridas (puedes cambiarlas)
st.subheader("📝 Paso 1: Cuéntame qué recuerdos destacar")
palabras_usuario = st.text_area(
    "Escribe palabras clave separadas por comas:",
    placeholder="ejemplo: Migas, hamburguesas crispy, tus risas, Caracas, primeras fotos"
)

st.subheader("🎭 Paso 2: Elige el tono")
tono = st.selectbox("Tono de la carta:", ["Romántico", "Divertido", "Emotivo", "Aventurero"])

if st.button("✨ Generar carta mágica"):
    if not palabras_usuario.strip():
        st.warning("Escribe al menos una palabra clave.")
    else:
        # Procesar palabras
        palabras = [p.strip() for p in palabras_usuario.split(",")]
        palabra_destacada = random.choice(palabras)
        
        # Plantillas según tono
        if tono == "Romántico":
            inicio = "Mi amor,"
            cuerpo = f"Cada vez que recuerdo {palabra_destacada}, mi corazón late más fuerte. Ese momento, como tantos otros, me hace sentir que contigo el tiempo se detiene."
            final = "Gracias por un año de ternura, complicidad y sueños compartidos."
        elif tono == "Divertido":
            inicio = "¡Mi loca favorita!"
            cuerpo = f"¿Te acuerdas de {palabra_destacada}? Me parto de risa solo de pensarlo. Contigo hasta las anécdotas más simples se convierten en historias épicas."
            final = "Que sigan los planes improvisados, las hamburguesas y las carcajadas. ¡Te quiero!"
        elif tono == "Emotivo":
            inicio = "Mi persona preferida en el mundo,"
            cuerpo = f"{palabra_destacada} es solo una pincelada de todo lo bonito que hemos vivido. Este año he aprendido que la felicidad tiene tu nombre."
            final = "Eres mi refugio y mi mayor alegría."
        else:  # Aventurero
            inicio = "¡Compañera de viaje!"
            cuerpo = f"{palabra_destacada} fue el inicio de una ruta increíble. Un año lleno de descubrimientos, sabores (como las crispy de Migas) y nuevos horizontes."
            final = "Que nunca falten las ganas de seguir explorando juntos. ¡Te amo!"

        # Construir carta completa
        carta_completa = f"""
{inicio}

{cuerpo}

{final}

Con todo mi cariño,
Tu compañero

📅 {datetime.now().strftime("%d de %B de %Y")}
"""
        st.success("🎉 ¡Tu carta está lista!")
        st.write(carta_completa)
        st.download_button("📥 Descargar carta", carta_completa, file_name=f"carta_aniversario_{datetime.now().strftime('%Y%m%d')}.txt")