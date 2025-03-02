from pymongo import MongoClient

# Datos de conexión directamente en el archivo config.py
MONGO_URI = "mongodb+srv://erove:ironbrick@cluster0.b1drs.mongodb.net/?retryWrites=true&w=majority"
MONGO_DB = "Ironbrick"
MONGO_COLLECTION = "Lego_colab"

# Crear conexión a MongoDB
client = MongoClient(MONGO_URI)

# Acceder a la base de datos y colección
db = client[MONGO_DB]
collection = db[MONGO_COLLECTION]
