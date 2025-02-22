import os
from dotenv import load_dotenv
from pymongo import MongoClient

# Cargar las variables de entorno
load_dotenv()

# Obtener las variables de entorno
MONGO_URI = os.getenv("MONGO_URI")
MONGO_DB = os.getenv("MONGO_DB")
MONGO_COLLECTION = os.getenv("MONGO_COLLECTION")

# Verifica si las variables de entorno están cargadas correctamente
print(f'MONGO_URI: {os.getenv("MONGO_URI")}')
print(f'MONGO_DB: {os.getenv("MONGO_DB")}')
print(f'MONGO_COLLECTION: {os.getenv("MONGO_COLLECTION")}')

# Verificar que las variables no están vacías
if not MONGO_URI or not MONGO_DB or not MONGO_COLLECTION:
    raise ValueError("Faltan algunas variables de entorno en el archivo .env")

# Validar que MONGO_DB sea una cadena de texto
if not isinstance(MONGO_DB, str):
    raise TypeError("MONGO_DB debe ser una cadena de texto")

# Crear conexión a MongoDB
client = MongoClient(MONGO_URI)

# Acceder a la base de datos y colección
db = client[MONGO_DB]  # Esto debe ser una cadena (str)
collection = db[MONGO_COLLECTION]
