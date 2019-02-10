from global_database import *
from event import *


class Chat(Model):
    id = IntegerField(primary_key=True)
    event = ForeignKeyField(Event)
    
    class Meta:
        database = db

def inserir_xat(event):
    chat = Chat.create(Chat.event == event)
    return chat

def init_database():
    db.create_tables([Chat], safe = True)