import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

st.title("📊 Nuestro primer año en datos")
st.markdown("*Elige un idioma de nuestro amor: estadísticas o biología*")

if "modo_seleccionado" not in st.session_state:
    st.session_state.modo_seleccionado = None

col1, col2 = st.columns(2)
with col1:
    if st.button("📈 Modo Estadístico", use_container_width=True):
        st.session_state.modo_seleccionado = "Estadístico"
        st.rerun()
with col2:
    if st.button("🔬 Modo Biólogo", use_container_width=True):
        st.session_state.modo_seleccionado = "Biólogo"
        st.rerun()

st.divider()

if st.session_state.modo_seleccionado is None:
    st.info("👆 Haz clic en uno de los botones de arriba para ver los datos de nuestro año.")
    st.stop()

if st.session_state.modo_seleccionado == "Estadístico":
    st.subheader("📊 Datos y tendencias de nuestro año")
    
    snacks = pd.DataFrame({
        "Snack": ["Helados 🍦", "Perros calientes 🌭", "Hamburguesas 🍔", "tostadas mexicanas 🌯", "Chocorramitos 🍫"],
        "Veces que comimos juntos": [15, 18, 5, 2, 10]
    })
    fig1 = px.bar(snacks, x="Snack", y="Veces que comimos juntos", title="¡Carrera de antojos compartidos (aprox)!", color="Snack")
    st.plotly_chart(fig1, use_container_width=True)

    actividades = pd.DataFrame({
        "Actividad": ["Ver películas 📺", "ir a comer helados", "Cocinar juntos 👩‍🍳", "Tomar fotos 📸", "Abrazarnos 🤗(mucho mas que eso)"],
        "Cantidad": [5, 22, 30, 67, 200]
    })
    fig2 = px.bar(actividades, x="Actividad", y="Cantidad", title="¿Qué hemos hecho más veces?", color="Actividad")
    st.plotly_chart(fig2, use_container_width=True)

    lugares = pd.DataFrame({
        "Lugar": ["Migas 🍔", "piscina 🏊‍♀️", "McDonald's 🍔🍟", "club ⚽🏀"],
        "Visitas": [8, 5, 4, 20]
    })
    fig3 = px.bar(lugares, x="Lugar", y="Visitas", title="Nuestros rincones favoritos", color="Lugar")
    st.plotly_chart(fig3, use_container_width=True)

    fecha_primera_cita = date(2025, 3, 3)
    dias_juntos = (date.today() - fecha_primera_cita).days
    st.metric("📅 Días desde que tuvimos nuestra primera cita", dias_juntos)
    
    # Galería de fotos  
    st.subheader("📸 Algunas de nuestras fotos favoritas")
    col1, col2, col3 = st.columns(3)
    with col1:
        try:
            st.image("images/primeracita.jpeg", caption="Primera cita en Migas 🍔", use_container_width=True)
        except:
            st.image("https://placehold.co/300x200?text=Migas", use_container_width=True)
    with col2:
        try:
            st.image("images/primerafotojuntos.jpeg", caption="Nuestra primera foto juntos 📷", use_container_width=True)
        except:
            st.image("https://placehold.co/300x200?text=Selfie", use_container_width=True)
    with col3:
        try:
            st.image("images/enamorados.jpeg", caption="Enamorados 💖", use_container_width=True)
        except:
            st.image("https://placehold.co/300x200?text=Amor", use_container_width=True)
    
    col4, col5, col6 = st.columns(3)
    with col4:
        try:
            st.image("images/sushi.jpeg", caption="Primer sushi juntos 🍣", use_container_width=True)
        except:
            st.image("https://placehold.co/300x200?text=Sushi", use_container_width=True)
    with col5:
        try:
            st.image("images/micasa.jpeg", caption=" Cuando conociste mi casa 🏠", use_container_width=True)
        except:
            st.image("https://placehold.co/300x200?text=Casa", use_container_width=True)
    with col6:
        try:
            st.image("images/24diciembre.jpeg", caption="Navidad juntos 🎄", use_container_width=True)
        except:
            st.image("https://placehold.co/300x200?text=Navidad", use_container_width=True)

    st.success("🎉 Dato freak: Nos hemos mandado aproximadamente 2,555 mensajes de 'te amo' (contados mentalmente como de a 7 diarios).")

else:
    st.subheader("🧬 Nuestra relación bajo el microscopio")
    st.markdown("*Análisis biológico del amor (con mucho cariño)*")

    mutualismo = pd.DataFrame({
        "Aspecto": ["Alegría", "Paciencia", "Locura", "Abrazos", "Helados"],
        "Tu aporte": [95, 75, 98, 100, 70],
        "Mi aporte": [90, 85, 60, 90, 50]
    })
    fig_bio1 = px.bar(mutualismo, x="Aspecto", y=["Tu aporte", "Mi aporte"], barmode="group",
                      title="🤝 Mutualismo: lo que aportamos cada uno",
                      color_discrete_sequence=["#FFB6C1", "#ADD8E6"])
    st.plotly_chart(fig_bio1, use_container_width=True)

    hormonas = pd.DataFrame({
        "Hormona": ["Oxitocina\n(abrazos)", "Dopamina\n(aventuras)", "Serotonina\n(paz)", "Adrenalina\n(emociones)"],
        "Nivel (%)": [95, 88, 92, 78]
    })
    fig_bio2 = px.bar(hormonas, x="Hormona", y="Nivel (%)", title="🧪 Producción de hormonas del amor",
                      color="Hormona", text_auto=True)
    st.plotly_chart(fig_bio2, use_container_width=True)

    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun", "Jul", "Ago", "Sep", "Oct", "Nov", "Dic"]
    felicidad = [30, 40, 42, 45, 50, 63, 75, 78, 79, 81, 82, 95]
    df_evo = pd.DataFrame({"Mes": meses, "Índice de felicidad (unidades biológicas)": felicidad})
    fig_bio3 = px.line(df_evo, x="Mes", y="Índice de felicidad (unidades biológicas)",
                       title="📈 Evolución de nuestros sentimientos",
                       markers=True)
    st.plotly_chart(fig_bio3, use_container_width=True)

    st.subheader("🐧 Nuestra especie emblemática")
    st.markdown("""
    **Los pingüinos de Magallanes** se emparejan de por vida y realizan largas migraciones juntos.
    Nosotros, aunque no volamos, hemos recorrido kilómetros de risas, besos, arrunchos y helados. 🍦
    """)
    st.markdown("<h1 style='text-align: center; font-size: 60px;'>🐧💖🐧</h1>", unsafe_allow_html=True)
    st.caption("Pingüinos enamorados (como nosotros)")
    
    # Galería de fotos modo biólogo
    st.subheader("📸 Evidencia fotográfica de nuestro amor")
    col_b1, col_b2, col_b3 = st.columns(3)
    with col_b1:
        try:
            st.image("images/nocturneando.jpeg", caption="Nocturneando 🌙", use_container_width=True)
        except:
            st.image("https://placehold.co/300x200?text=Nocturna", use_container_width=True)
    with col_b2:
        try:
            st.image("images/gaitas.jpeg", caption="Gaitas en tu cumpleaños 🎶", use_container_width=True)
        except:
            st.image("https://placehold.co/300x200?text=Gaitas", use_container_width=True)
    with col_b3:
        try:
            st.image("images/14febrero.jpeg", caption="14 de febrero 💕", use_container_width=True)
        except:
            st.image("https://placehold.co/300x200?text=SanValentin", use_container_width=True)

    st.info("💡 **Dato bio-romántico:** Los caballitos de mar son monógamos y se dan la cola todos los días. ¡Misma energía!")
    
    fecha_primera_cita = date(2025, 3, 3)
    dias_juntos = (date.today() - fecha_primera_cita).days
    st.metric("📅 Ciclos de la Tierra desde nuestro encuentro", f"{dias_juntos} días")
    st.caption("*Unidad de medida: rotaciones terrestres*")