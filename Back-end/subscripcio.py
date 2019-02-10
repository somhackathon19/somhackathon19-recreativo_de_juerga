from global_database import *
from event import *
from user import *
import datetime



# Subscripcio

class Subscripcio(Model):
    id = IntegerField(primary_key = True)
    event = ForeignKeyField(Event)
    user = ForeignKeyField(Usuari)
    data_alta = DateTimeField(default=datetime.datetime.now)
    
    class Meta:
        database = db


def insert_subcription(dades):
    Subscripcio.create(club = dades.get('club'),
    user = dades.get('user'))

def get_subscripcio(user, club):
    subscripcio = Subscripcio.select().where(
             Subscripcio.user == user &  Subscripcio.club == club)
    return subscripcio

def delete_subscription(user, club):
    query = Subscripcio.delete().where(Subscripcio.user == user &
    Subscripcio.club == club)

    query.execute()

def init_database():
    db.create_tables([Subscripcio], safe = True)