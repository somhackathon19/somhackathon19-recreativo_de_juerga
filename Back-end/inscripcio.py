from global_database import *
from event import *
import datetime

# Inscripcions
class Inscripcio(Model):
    id = IntegerField(primary_key = True)
    moment_inscripcio = DateTimeField(default=datetime.datetime.now)
    event =  ForeignKeyField(Event)
    usuari = ForeignKeyField(Usuari)

    class Meta:
        database = db


def get_inscripcio(id):
    inscripcio = Inscripcio.select().where(Insicripcio.id == id)
    return inscripcio

def inserir_inscripcio(dades):
    Inscripcio.create(
        event = dades.get('event'),
        usuari = dades.get('usuari')
    )

def inscripcio_finalitzada(event, user):
    event = Event.select_event(event)
    if (event.data_event >= datetime.datetime.now):
        usuari = Usuari.get_usuari(user)
        usuari.tokens = usuari.tokens + 1

def init_database():
    db.create_tables([Inscripcio], safe = True)