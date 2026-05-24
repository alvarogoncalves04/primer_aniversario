import streamlit as st
from datetime import datetime
import matplotlib.pyplot as plt
from io import BytesIO
import base64

st.set_page_config(page_title="Carta de Aniversario", page_icon="💌")

# CSS para la carta visible en la web
st.markdown("""
<style>
    .stApp {
        background-color: #1E1A1A;
    }
    .carta-wrapper {
        background-color: #FEF7E6;
        background-image: radial-gradient(circle, #E3D5C0 1.2px, transparent 1.2px);
        background-size: 24px 24px;
        border-radius: 28px;
        padding: 2rem;
        margin: 20px 0;
        box-shadow: 0 20px 35px rgba(0,0,0,0.4);
        border: 1px solid #D4A373;
        font-family: 'Georgia', 'Times New Roman', serif;
        color: #2C1A1A;
    }
    .carta-titulo {
        font-size: 2rem;
        text-align: center;
        font-weight: bold;
        color: #9B2E2E;
        border-bottom: 2px solid #D4A373;
        display: inline-block;
        width: auto;
        margin: 0 auto 1rem auto;
        padding-bottom: 0.3rem;
        letter-spacing: 1px;
    }
    .carta-fecha {
        text-align: right;
        font-style: italic;
        color: #7A5A5A;
        margin-bottom: 2rem;
        font-size: 0.9rem;
    }
    .carta-contenido {
        font-size: 1.05rem;
        line-height: 1.7;
        text-align: justify;
        white-space: pre-wrap;
    }
    .carta-firma {
        margin-top: 2rem;
        text-align: right;
        font-family: 'Brush Script MT', cursive;
        font-size: 1.5rem;
        color: #9B2E2E;
    }
    .sobre-container {
        text-align: center;
        background-color: #2C2626;
        border-radius: 40px;
        padding: 2rem;
        cursor: pointer;
        transition: all 0.3s ease;
        border: 1px solid #D4A373;
    }
    .sobre-container:hover {
        background-color: #3D2C2C;
        transform: scale(1.01);
    }
    .sobre-icono {
        font-size: 4.5rem;
        filter: drop-shadow(2px 4px 6px black);
    }
    .sobre-texto {
        color: #F5E6E6;
        font-size: 1.2rem;
        margin-top: 0.8rem;
    }
</style>
""", unsafe_allow_html=True)

st.title("💌 Una carta de corazón a corazón")
st.markdown("*Hoy te escribo estas palabras, porque a veces el amor se cuenta mejor con tinta y papel.*")

# Estado de la carta
if "carta_abierta" not in st.session_state:
    st.session_state.carta_abierta = False

# Contenido de la carta (puedes editarlo extensamente)
contenido_carta = """Mi vida,

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
Tu pana del alma 💖"""

def generar_imagen_carta(contenido):
    """Genera una imagen PNG de la carta con diseño elegante"""
    fig = plt.figure(figsize=(8, 12), facecolor='#FEF7E6')
    ax = fig.add_axes([0, 0, 1, 1])
    ax.axis('off')
    
    # Marco decorativo (opcional)
    ax.plot([0.05, 0.95, 0.95, 0.05, 0.05], [0.05, 0.05, 0.95, 0.95, 0.05], 
            color='#D4A373', linewidth=1.5, transform=fig.transFigure, clip_on=False)
    
    # Título
    fig.text(0.5, 0.92, "Para mi amor en nuestro primer aniversario", 
             fontsize=18, ha='center', family='serif', weight='bold', color='#9B2E2E')
    
    # Fecha
    fig.text(0.93, 0.88, f"Caracas, {datetime.now().strftime('%d de %B de %Y')}", 
             fontsize=10, ha='right', style='italic', color='#7A5A5A')
    
    # Contenido
    fig.text(0.08, 0.8, contenido, fontsize=11, ha='left', va='top', 
             family='serif', wrap=True, linespacing=1.5, color='#2C1A1A')
    
    # Firma
    fig.text(0.92, 0.12, "Con todo mi corazón,", fontsize=12, ha='right', 
             style='italic', color='#9B2E2E')
    fig.text(0.92, 0.09, "Tu compañero", fontsize=12, ha='right', 
             style='italic', color='#9B2E2E')
    
    # Guardar en buffer
    buf = BytesIO()
    plt.savefig(buf, format='png', bbox_inches='tight', dpi=150, facecolor=fig.get_facecolor())
    buf.seek(0)
    plt.close(fig)
    return buf

# Mostrar sobre cerrado o carta abierta
if not st.session_state.carta_abierta:
    st.markdown("""
    <div class="sobre-container">
        <div class="sobre-icono">💌</div>
        <div class="sobre-texto">Hay una carta esperándote...</div>
        <div class="sobre-texto" style="font-size:0.9rem;">Haz clic en el botón para abrirla</div>
    </div>
    """, unsafe_allow_html=True)
    if st.button("📨 Abrir carta mágica", use_container_width=True):
        st.session_state.carta_abierta = True
        st.rerun()
else:
    # Mostrar la carta en pantalla (HTML/CSS)
    st.markdown(f"""
    <div class="carta-wrapper">
        <div style="text-align: center;">
            <div class="carta-titulo">Para mi amor en nuestro primer aniversario</div>
        </div>
        <div class="carta-fecha">Caracas, {datetime.now().strftime('%d de %B de %Y')}</div>
        <div class="carta-contenido">{contenido_carta}</div>
        <div class="carta-firma">Con todo mi corazón,<br>Tu compañero</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Botón de descarga como imagen PNG
    if st.button("📸 Descargar esta carta como imagen PNG", use_container_width=True):
        img_buf = generar_imagen_carta(contenido_carta)
        b64 = base64.b64encode(img_buf.getvalue()).decode('utf-8')
        href = f'<a href="data:image/png;base64,{b64}" download="carta_aniversario.png">Haz clic aquí para guardar la imagen</a>'
        st.markdown(href, unsafe_allow_html=True)
        st.success("¡Imagen generada! Haz clic en el enlace de arriba para descargarla.")
    
    if st.button("🔒 Cerrar carta", use_container_width=True):
        st.session_state.carta_abierta = False
        st.rerun()