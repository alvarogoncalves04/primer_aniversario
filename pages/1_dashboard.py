import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import date

st.title("📊 Nuestro primer año en datos")
st.markdown("*Elige tu lente favorito: estadísticas o biología*")

# Inicializar modo en session state
if "modo" not in st.session_state:
    st.session_state.modo = "Estadístico"

col1, col2 = st.columns(2)
with col1:
    if st.button("📈 Modo Estadístico (mi estilo)", use_container_width=True):
        st.session_state.modo = "Estadístico"
        st.rerun()
with col2:
    if st.button("🔬 Modo Biólogo (tu estilo)", use_container_width=True):
        st.session_state.modo = "Biólogo"
        st.rerun()

st.divider()

# ================= MODO ESTADÍSTICO =================
if st.session_state.modo == "Estadístico":
    st.subheader("📊 Datos y tendencias de nuestro año")
    
    # Gráfica 1: Competencia de snacks favoritos
    snacks = pd.DataFrame({
        "Snack": ["Helados 🍦", "Galletas 🍪", "Hamburguesas 🍔", "Papitas 🥔", "Chocolate 🍫"],
        "Veces que comimos juntos": [24, 18, 12, 30, 15]
    })
    fig1 = px.bar(snacks, x="Snack", y="Veces que comimos juntos", title="¡Carrera de antojos compartidos!", color="Snack")
    st.plotly_chart(fig1, use_container_width=True)

    # Gráfica 2: Actividades favoritas
    actividades = pd.DataFrame({
        "Actividad": ["Ver series 📺", "Caminar por el parque 🌳", "Cocinar juntos 👩‍🍳", "Tomar fotos 📸", "Abrazarnos 🤗"],
        "Cantidad": [45, 22, 18, 67, 200]
    })
    fig2 = px.bar(actividades, x="Actividad", y="Cantidad", title="¿Qué hemos hecho más veces?", color="Actividad")
    st.plotly_chart(fig2, use_container_width=True)

    # Gráfica 3: Lugares más visitados
    lugares = pd.DataFrame({
        "Lugar": ["Migas 🍔", "Parque del Este 🌳", "Cine 🎬", "Nuestra casa 🏠"],
        "Visitas": [8, 5, 4, 150]
    })
    fig3 = px.bar(lugares, x="Lugar", y="Visitas", title="Nuestros rincones favoritos", color="Lugar")
    st.plotly_chart(fig3, use_container_width=True)

    # Contador de días desde primera cita
    fecha_primera_cita = date(2025, 2, 14)
    dias_juntos = (date.today() - fecha_primera_cita).days
    st.metric("📅 Días desde que nos conocimos en Migas", dias_juntos)
    st.success("🎉 Dato freak: Nos hemos mandado aproximadamente 1,234 mensajes de 'te quiero' (contados mentalmente).")

# ================= MODO BIÓLOGO =================
else:
    st.subheader("🧬 Nuestra relación bajo el microscopio")
    st.markdown("*Análisis biológico del amor (con mucho cariño)*")

    # Simbiosis (mutualismo)
    mutualismo = pd.DataFrame({
        "Aspecto": ["Alegría", "Paciencia", "Locura", "Abrazos", "Helados"],
        "Tu aporte": [95, 80, 98, 100, 70],
        "Mi aporte": [90, 85, 85, 90, 95]
    })
    fig_bio1 = px.bar(mutualismo, x="Aspecto", y=["Tu aporte", "Mi aporte"], barmode="group",
                      title="🤝 Mutualismo: lo que aportamos cada uno",
                      color_discrete_sequence=["#FFB6C1", "#ADD8E6"])
    st.plotly_chart(fig_bio1, use_container_width=True)

    # Hormonas del amor
    hormonas = pd.DataFrame({
        "Hormona": ["Oxitocina\n(abrazos)", "Dopamina\n(aventuras)", "Serotonina\n(paz)", "Adrenalina\n(emociones)"],
        "Nivel (%)": [95, 88, 92, 78]
    })
    fig_bio2 = px.bar(hormonas, x="Hormona", y="Nivel (%)", title="🧪 Producción de hormonas del amor",
                      color="Hormona", text_auto=True)
    st.plotly_chart(fig_bio2, use_container_width=True)

    # Evolución de sentimientos (línea de tiempo biológica)
    meses = ["Ene", "Feb", "Mar", "Abr", "May", "Jun"]
    felicidad = [70, 85, 90, 88, 95, 98]
    df_evo = pd.DataFrame({"Mes": meses, "Índice de felicidad (unidades biológicas)": felicidad})
    fig_bio3 = px.line(df_evo, x="Mes", y="Índice de felicidad (unidades biológicas)",
                       title="📈 Evolución de nuestros sentimientos (como una especie en extinción pero al revés)",
                       markers=True)
    st.plotly_chart(fig_bio3, use_container_width=True)

    # Especie emblemática
    st.subheader("🐧 Nuestra especie emblemática")
    st.markdown("""
    **Los pingüinos de Magallanes** se emparejan de por vida y realizan largas migraciones juntos.
    Nosotros, aunque no volamos, hemos recorrido kilómetros de risas y helados. 🍦
    """)
    st.markdown("<h1 style='text-align: center; font-size: 80px;'>🐧💖🐧</h1>", unsafe_allow_html=True)
    st.caption("Pingüinos enamorados (como nosotros)")
    # Dato curioso biológico
    st.info("💡 **Dato bio-romántico:** Los caballitos de mar son monógamos y se dan la cola todos los días. Nosotros nos damos la mano (y a veces un beso). ¡Misma energía!")
    
    # Contador de días en versión biológica
    fecha_primera_cita = date(2025, 2, 14)
    dias_juntos = (date.today() - fecha_primera_cita).days
    st.metric("📅 Ciclos de la Tierra desde nuestro encuentro", f"{dias_juntos} días")
    st.caption("*Unidad de medida: rotaciones terrestres*")