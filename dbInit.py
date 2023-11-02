import pymongo
from pymongo import MongoClient
from marshmallow import Schema, fields, validate
from marshmallow import ValidationError
from config import db_host
from data import datos_inventario

client = MongoClient(db_host)

db = client.abaco

# Definir un esquema usando marshmallow
class InventarioSchema(Schema):
    producto_id = fields.Str(required=True)
    nombre = fields.Str(required=True)
    descripcion = fields.Str()
    precio_unitario = fields.Float(required=True)
    stock_actual = fields.Int(required=True)
    categoria = fields.Str()
    proveedor = fields.Str()
    fecha_entrada = fields.DateTime()

# Crear una instancia del esquema
inventario_schema = InventarioSchema()

try:
    # resultado = inventario_schema.load(datos_inventario)
    count = db.inventario.count_documents({})

    if count > 0: # Verificar si hay datos existentes
        db.inventario.drop()

    db.inventario.insert_many(datos_inventario)

    # print("Datos válidos:", resultado)
except Exception as error:
    print("Error de validación:", error)



