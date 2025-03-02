import streamlit as st
import pandas as pd
from config import collection  # Importamos solo la colección

# Función para obtener los datos
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return pd.DataFrame(data)

# Función para obtener los temas (Theme)
def get_themes():
    themes = collection.distinct("theme")  # Obtener temas únicos
    return themes

# Interfaz en Streamlit
st.title("📊 Visualización de MongoDB en Streamlit")

# Obtener todos los temas
themes = get_themes()

# Crear un selectbox para elegir un tema
selected_theme = st.selectbox("Selecciona un tema de LEGO", themes)

# Si el usuario ha seleccionado un tema
if selected_theme:
    # Filtrar los datos por el tema seleccionado
    df = get_data()
    filtered_df = df[df["theme"] == selected_theme]

    # Mostrar los detalles del set seleccionado
    if not filtered_df.empty:
        st.write(f"Detalles de los sets de LEGO para el tema: {selected_theme}")
        st.dataframe(filtered_df)
    else:
        st.write(f"No se encontraron sets para el tema: {selected_theme}")
