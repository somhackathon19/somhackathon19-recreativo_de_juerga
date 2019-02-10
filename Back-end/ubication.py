from global_database import *

# Classe ubicacio
class Ubication(Model):    
    id = IntegerField(primary_key = True)
    latitude = TextField()
    longitude = TextField()
    nom = TextField()

    class Meta:
        database = db

def inserir_ubicacio(dades):
    ubicacio = Ubication.create(
        latitude = dades.get('latitude'),
        longitude = dades.get('longitude'),
        nom = dades.get('nom'))


def get_ubicacio(id):
    ubicacio = Ubication.select().where(Ubication.id == id).get()
    parse = {'nom':ubicacio.nom,'latitude':ubicacio.latitude,
    'longitude':ubicacio.longitude}
    return parse

def get_ubicacions():
    return Ubication.select()

def get_ubicacions_esportives():
    return Ubication.select().where(Ubication.nom == 'Equipament Esportiu').get()

def get_ubicacions_interior():
    return Ubication.select().where(Ubication.nom == 'Interior').get()

def get_ubicacions_zona_verda():
    return Ubication.select().where(Ubication.nom == 'Zona Verda').get()




def init_database():
    db.create_tables([Ubication], safe = True)

# Per netejar la base de dades
def eliminar_ubicacions():
    Query = Ubication.delete()
    Query.execute
