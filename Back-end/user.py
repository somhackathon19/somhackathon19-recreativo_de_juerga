from global_database import *
from ubication import *
import datetime

# Usuari

class Usuari(Model):
    nom = TextField()
    cognom = TextField()
    correu = TextField()
    username = TextField(unique = True)
    telefon = IntegerField(primary_key = True)
    sexe = BooleanField()
    data_naixement = DateTimeField()
    domicili = TextField()
    ubication = ForeignKeyField(Ubication)
    token = IntegerField()

    class Meta:
        database = db


def insert (dades):
    usuari_creat = Usuari.create(nom = dades.get('nom'),
    cognom = dades.get('cognom'), 
    correu = dades.get('correu'),
    username = dades.get('username'),
    telefon = dades.get('telefon'),
    sexe = dades.get('sexe'),
    data_naixement = datetime.date(dades.get('year'), dades.get('month'), dades.get('day')),
    domicili = dades.get('domicili'),
    ubication = dades.get('ubication'),
    token = 1)

    return usuari_creat

def get_usuari(username):
    user = Usuari.select().where(Usuari.username == username)
    return user

def get_tokens(username):
    user = get_user(username)
    return user.token

def init_database():
    db.create_tables([Usuari], safe = True)

def generar_dades():
    print("Generant dades usuari...")
    ruben = {'nom':'Ruben','cognom':'Gil','correu':'r@tecnocampus.cat',
'username':'rubencito_girou','telefon':11111,
'sexe':True,'year':1998,'month':9,'day':10,'domicili':'carrerA',
'ubication':2}
    ignasi = {'nom':'Ignasi','cognom':'Oliver','correu':'i@tecnocampus.cat',
'username':'nachito','telefon':2222,
'sexe':True,'year':1998,'month':9,'day':10 ,'domicili':'carrerB',
'ubication':2}
    alex = {'nom':'Alex','cognom':'Alcaide','correu':'a@tecnocampus.cat',
'username':'Alejandro','telefon':3333,
'sexe':True,'year':1998,'month':9,'day':10,'domicili':'carrerC',
'ubication':2}
    sergi = {'nom':'Sergi','cognom':'Obiols','correu':'s@tecnocampus.cat',
'username':'sergi_obi9','telefon':4444,
'sexe':True,'year':1998,'month':9,'day':10 ,'domicili':'carrerD',
'ubication':2}
    xavi = {'nom':'Xavi','cognom':'Ortega','correu':'x@tecnocampus.cat',
'username':'xortega','telefon':5555,
'sexe':True,'year':1998,'month':9,'day':10,'domicili':'carrerE',
'ubication':2}

    insert(ruben)
    insert(ignasi)
    insert(alex)
    insert(sergi)
    insert(xavi)

