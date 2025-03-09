import streamlit as st
import pandas as pd
import pickle
import pymongo

# Conectar a MongoDB usando Streamlit Secrets
@st.cache_resource
def init_mongo_connection():
    return pymongo.MongoClient(st.secrets["mongo"]["uri"])

mongo_client = init_mongo_connection()
mongo_db = mongo_client[st.secrets["mongo"]["db"]]
mongo_collection = mongo_db[st.secrets["mongo"]["collection"]]

# Cargar la base de datos
@st.cache_data
def load_data():
    data = pd.DataFrame(list(mongo_collection.find()))
    return data

# Cargar el modelo de recomendación
@st.cache_resource
def load_model():
    with open("stacking_model.pkl", "rb") as file:
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
