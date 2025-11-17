import streamlit as st
from PIL import Image

# ---------- Funciones "dummy" que luego reemplazarás con tu modelo ----------

def interpretar_linea_sismica(imagen, fase, polaridad):
    return (
        f"Interpretación sísmica preliminar:\n\n"
        f"- Fase: {fase}\n"
        f"- Polaridad: {polaridad}\n"
        f"- Reflectores continuos en el sector central.\n"
        f"- Variación de amplitudes hacia los flancos sugieren cambios de facies.\n"
        f"- Dos unidades sísmicas separadas por posible discordancia."
    )

def indicar_anomalias_hidrocarburos(imagen, fase, polaridad):
    return (
        "Anomalías de hidrocarburos:\n\n"
        "- Alta amplitud localizada (posible bright spot).\n"
        "- Terminación plana de reflectores (posible flat spot).\n"
        "- Recomendación: confirmar con atributos AVO y pozos."
    )

# ------------------- INTERFAZ DE GEOPETROIA -----------------------

st.set_page_config(page_title="GeoPetroIA", page_icon="🛢️")

st.title("🛢️ GeoPetroIA")
st.write("Bienvenido a GeoPetroIA. Plataforma diseñada para **interpretación sísmica** y detección de **anomalías de hidrocarburos**.")

st.markdown("---")

opcion = st.radio(
    "Seleccione el tipo de análisis:",
    ["Interpretación de línea sísmica",
     "Indicar anomalías de hidrocarburos",
     "Ambos (interpretación + anomalías)"]
)

st.markdown("### 1️⃣ Cargar la imagen sísmica")
archivo = st.file_uploader("Suba una imagen JPG/PNG:", type=["jpg", "jpeg", "png"])

st.markdown("### 2️⃣ Parámetros sísmicos")
col1, col2 = st.columns(2)

with col1:
    fase = st.text_input("Fase de los datos", placeholder="Ej: fase normal, rotada 180°...")

with col2:
    polaridad = st.text_input("Polaridad", placeholder="Ej: SEG normal, SEG inversa...")

if st.button("Analizar"):
    if archivo is None:
        st.error("Debe cargar una imagen sísmica.")
    elif fase == "" or polaridad == "":
        st.error("Debe ingresar fase y polaridad.")
    else:
        imagen = Image.open(archivo)
        st.image(imagen, caption="Línea sísmica cargada", use_column_width=True)

        st.markdown("---")
        st.subheader("Resultados de GeoPetroIA")

        # Siempre primero interpretación
        interpretacion = interpretar_linea_sismica(imagen, fase, polaridad)
        st.markdown("### 📌 Interpretación sísmica")
        st.write(interpretacion)

        # Luego anomalías (según la opción)
        if o
