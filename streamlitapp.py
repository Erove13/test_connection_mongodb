import streamlit as st
import pandas as pd
import pickle
import pymongo
import os
from dotenv import load_dotenv

# Cargar variables de entorno
load_dotenv()
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("MONGO_DB")
COLLECTION_NAME = "lego_final_venta"

# Conectar a MongoDB
@st.cache_data
def load_data():
    client = pymongo.MongoClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]
    data = pd.DataFrame(list(collection.find()))
    return data

# Cargar el modelo de recomendación
@st.cache_resource
def load_model():
    with open("recommender.pkl", "rb") as file:
        model = pickle.load(file)
    return model

df = load_data()
model = load_model()

st.title("Sistema de Recomendación")

# Mostrar los primeros registros de la base de datos
st.write("Vista previa de la base de datos:")
st.dataframe(df.head())

# Seleccionar un elemento para obtener recomendaciones
item = st.selectbox("Selecciona un ítem para recomendar:", df.iloc[:, 0])

if st.button("Obtener Recomendaciones"):
    recommendations = model.recommend(item)  # Esto depende de cómo funcione tu modelo
    st.write("Recomendaciones:")
    st.write(recommendations)
