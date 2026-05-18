import streamlit as st
import random
from datetime import datetime

st.set_page_config(page_title="Carta de Aniversario", page_icon="💌")
st.title("💌 Una carta especial para ti")
st.markdown("*Elige palabras que describan nuestro año y generaré una carta única, ¡con sabor venezolano!*")

st.subheader("📝 Paso 1: Cuéntame qué recuerdos destacar")
palabras_usuario = st.text_area(
    "Escribe palabras clave separadas por comas:",
    placeholder="ejemplo: Migas, hamburguesas crispy, helados, tus risas, Caracas"
)

st.subheader("🎭 Paso 2: Elige el tono")
tono = st.selectbox("Tono de la carta:", ["Romántico", "Divertido", "Emotivo", "Aventurero"])

if st.button("✨ Generar carta mágica"):
    if not palabras_usuario.strip():
        st.warning("Escribe al menos una palabra clave, mi pana.")
    else:
        palabras = [p.strip() for p in palabras_usuario.split(",")]
        palabra_destacada = random.choice(palabras)
        
        if tono == "Romántico":
            inicio = "Mi vida,"
            cuerpo = f"Cada vez que recuerdo {palabra_destacada}, siento un calorcito en el pecho. Ese momento, como tantos otros, me hace pensar que el destino nos tenía preparado algo bien chevere."
            final = "Gracias por un año de amor, helados compartidos y promesas pa'l futuro. Te quiero un montón."
        elif tono == "Divertido":
            inicio = "¡Mi loca favorita!"
            cuerpo = f"¿Te acuerdas de {palabra_destacada}? Me parto de la risa solo de pensarlo. Contigo hasta las anécdotas más simples se convierten en historias épicas, como cuando pedimos hamburguesas crispy en Migas y casi nos ahogamos de tanto reír."
            final = "Que sigan los helados, las galletas y los abrazos improvisados. ¡Eres un sol, chama!"
        elif tono == "Emotivo":
            inicio = "Mi persona preferida en el mundo,"
            cuerpo = f"{palabra_destacada} es solo una pincelada de todo lo bonito que hemos vivido. Este año he aprendido que la felicidad tiene tu nombre y tu risa."
            final = "Gracias por ser mi refugio y mi mayor alegría. Eres la mejor persona que he conocido."
        else:  # Aventurero
            inicio = "¡Compañera de viaje!"
            cuerpo = f"{palabra_destacada} fue el inicio de una ruta increíble. Un año lleno de descubrimientos, sabores (como las crispy de Migas), nuevos lugares y miles de fotos."
            final = "Que nunca falten las ganas de seguir explorando juntos. ¡Te amo, mi pana de aventuras!"

        carta_completa = f"""
{inicio}

{cuerpo}

{final}

Con todo mi cariño,
Tu compañero

📅 {datetime.now().strftime("%d de %B de %Y")}
"""
        st.success("🎉 ¡Aquí tienes tu carta venezolana!")
        st.write(carta_completa)
        st.download_button("📥 Descargar carta", carta_completa, file_name=f"carta_aniversario_{datetime.now().strftime('%Y%m%d')}.txt")