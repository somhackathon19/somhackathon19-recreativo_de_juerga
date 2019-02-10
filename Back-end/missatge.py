from user import *
from chat import *
from global_database import *

class Missatge(Model):

    id = IntegerField(primary_key=True)
    missatge = TextField()
    user = ForeignKeyField(Usuari)
    chat = ForeignKeyField(Chat)

    class Meta:
        database = db


def insert_missatge(dades):
    Missatge.create(
        missatge = dades.get('missatge'),
        user = dades.get('user'),
        event = dades.get('chat')
    )

def get_missatge(user, event):
    missatge = Missatge.select().where(Missatge.user == user & Missatge.event == event)
    return missatge

def init_database():
    db.create_tables([Missatge], safe = True)
