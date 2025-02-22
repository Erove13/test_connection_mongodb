import streamlit as st
import pandas as pd
from config import collection  # Importamos solo la colección

# Función para obtener los datos
def get_data():
    data = list(collection.find({}, {"_id": 0}))
    return pd.DataFrame(data)

# Interfaz en Streamlit
st.title("📊 Visualización de MongoDB en Streamlit")

if st.button("Cargar Datos"):
    df = get_data()
    st.dataframe(df)
