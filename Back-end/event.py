from global_database import *
from user import *
import user
from ubication import *
import ubication
from etiqueta import *
import etiqueta
import datetime

# Classe Event

class Event(Model):
    id = IntegerField(primary_key = True)
    titol = TextField() 
    descripcio = TextField()
    data_event = TextField(null = True)
    hora = TextField()
    ubicacio = ForeignKeyField(Ubication)
    # Actiu -> Encara et pots apuntar
    Actiu = BooleanField(default=True)
    token = IntegerField(default = 1)
    creador = ForeignKeyField(Usuari)
    # 3 etiquetes event
    etiqueta_A = ForeignKeyField(Etiqueta)
    etiqueta_B = ForeignKeyField(Etiqueta)
    etiqueta_C = ForeignKeyField(Etiqueta)
    esport_rang = TextField(null =True)
    esport_participants = TextField(null = True)
    club_nombre = TextField(null = True)
    altres_tematica_especifica = TextField(null = True)
    tipus = TextField()
 
    class Meta:
        database = db

def get_events(tipus):
    events = Event.select()
    resultat = list ()
    for e in events:
        if(e.tipus == tipus):
            resultat.append(e)
    return resultat

def get_event(id):
    event = Event.select().where(Event.id == id).get()
    if(event.tipus == 'Esport'):
        retorn = parsejar_esport(event)
        return retorn
    elif (event.tipus == 'Altres'):
        retorn = parsejar_altres(event)
        return retorn
    else:
        retorn = parsejar_club(event)
        return retorn


def inserir_esport(dades):
    data_e = datetime.date(dades.get('year'),dades.get('month'),dades.get('day'))
    Event.create(titol = dades.get('titol'),descripcio = dades.get('descripcio'),
            data_event = data_e.strftime('%d/%m/%Y'),
            ubicacio = dades.get('ubicacio'),
            actiu = dades.get('Actiu'),
            token = 1,
            creador = dades.get('creador'),
            hora = dades.get('hora'),
            etiqueta_A = dades.get('etiqueta_A'),
            etiqueta_B = dades.get('etiqueta_B'),
            etiqueta_C = dades.get('etiqueta_C'),
            tipus = dades.get('tipus'),
            esport_rang = dades.get('esport_rang'),
            esport_participants = dades.get('esport_participants')
        )

def parsejar_esport(event):
    etiqueta_A  = etiqueta.get_nom(event.etiqueta_A)
    etiqueta_B = etiqueta.get_nom(event.etiqueta_B)
    etiqueta_C = etiqueta.get_nom(event.etiqueta_C)

    ubicacio_id = event.ubicacio
    ubi = ubication.get_ubicacio(ubicacio_id)

    parser = {'id': event.id,
    'titol':event.titol,
    'descripcio':event.descripcio,
    'data_event':event.data_event,
    'hora' :event.hora,
    'ubicacio_latitude':ubi.get('latitude'),
    'ubicacio_longitude':ubi.get('longitude'),
    'ubicacio_nom':ubi.get('nom'),
    'Actiu' :event.Actiu,
    'token' :event.token,
    'esport_rang':event.esport_rang,
    'esport_participants':event.esport_participants
    }
    return parser


    

def inserir_altres(dades):
    Event.create(titol = dades.get('titol'),descripcio = dades.get('descripcio'),
            data_event = datetime.date(dades.get('year'),dades.get('month'),dades.get('day')),
            ubicacio = dades.get('ubicacio'),
            actiu = dades.get('Actiu'),
            token = 1,
            creador = dades.get('creador'),
            hora = dades.get('hora'),
            etiqueta_A = dades.get('etiqueta_A'),
            etiqueta_B = dades.get('etiqueta_B'),
            etiqueta_C = dades.get('etiqueta_C'),
            altres_tematica_especifica = dades.get('altres_tematica_especifica'),
            tipus = dades.get('tipus')
        )

def parsejar_altres(event):
    ubicacio = event.ubicacio
    ubi = ubication.get_ubicacio(ubicacio)
    parser = {'id': event.id,
    'titol':event.titol,
    'descripcio':event.descripcio,
    'data_event':event.data_event,
    'hora' :event.hora,
    'ubicacio_latitude':ubi.get('latitude'),
    'ubicacio_longitude':ubi.get('longitude'),
    'ubicacio_nom':ubi.get('nom'),
    'Actiu' :event.Actiu,
    'token' :event.token,
    'altres_tematica_especifica' :event.altres_tematica_especifica}
    return parser

def get_event_altres():
    return Event.select().where(Event.tipus == 'Altres')

def inserir_club(dades):
    Event.create(titol = dades.get('titol'),descripcio = dades.get('descripcio'),
            data_event = datetime.date(dades.get('year'),dades.get('month'),dades.get('day')),
            ubicacio = dades.get('ubicacio'),
            actiu = dades.get('Actiu'),
            token = 1,
            creador = dades.get('creador'),
            hora = dades.get('hora'),
            etiqueta_A = dades.get('etiqueta_A'),
            etiqueta_B = dades.get('etiqueta_B'),
            etiqueta_C = dades.get('etiqueta_C'),
            club_nombre = dades.get('club_nombre'),
            tipus = dades.get('tipus')
        )

def parsejar_club(event):
    ubicacio = event.ubicacio
    ubi = ubication.get_ubicacio(ubicacio)
    parser = {'id': event.id,
    'titol':event.titol,
    'descripcio':event.descripcio,
    'hora' :event.hora,
    'places' :event.club_nombre,
    'ubicacio_latitude':ubi.get('latitude'),
    'ubicacio_longitude':ubi.get('longitude'),
    'ubicacio_nom':ubi.get('nom'),
    }
    return parser

def get_event_club():
    return Event.select().where(Event.tipus == 'Club')



# Inicialitzacio base dades
def init_database():
    db.create_tables([Event], safe=True)


def data_faker():
    event_sport = {'titol':'3x3 partit basquet','descripcio': 'Partit de basquet 3x3. Pla den boet. Es necessita un minim de 6 persones (2 equips) i un maxim de 12 (4 equips). Es busca nivell perque ens estem preparant per un torneig internacional',
                  'year':2019, 'month':2,'day':20,'hora':'17:00','ubicacio':25,'creador':4444,'actiu':True,'etiqueta_A':92,
                 'etiqueta_B':108,'etiqueta_C':0, 'esport_rang':'6 - 12', 'esport_participants':8,
                  'tipus':'Esports'}

    event_bici = {'titol':'Ruta en bici 100 km','descripcio': 'Ruta en bici 100 km. Sortim des de Sant Simó, on hi ha la gasolinera i anem majoritariament per la Nacional. Es busca gran "peloton". Al final de la ruta dinarem tots junts per fer bon rollo. Restaurant reservat. 10 € persona.','year':2019,
   'month':2,'day':23,'hora':'09:00','ubicacio':25,'creador':11111,'actiu':True,'etiqueta_A':75,
                 'etiqueta_B':83,'etiqueta_C':0,'esport_rang':'2 - 20', 'esport_participants':18,
                  'tipus':'Esports'}

    event_escacs = {
   'titol':'Torneig escacs','descripcio': 'Torneig escacs de nivell. Es faran partides de 10 minuts amb les regles oficials. Es necessita un minim de 2 persones i un maxim de 10. Per passar de ronda guanya el millor de 5 partides. La ubicació es al bloc de pisos del costat dels mossos del pla den Boet','year':2019,
   'month':2,'day':25,'hora':'18:00','ubicacio':25,'creador':11111,'actiu':True,'etiqueta_A':70,
                 'etiqueta_B':54,'etiqueta_C':0,'esport_rang':'2 - 10', 'esport_participants':6,
                  'tipus':'Esports'}
    inserir_esport(event_sport)
    inserir_esport(event_bici)
    inserir_esport(event_escacs)
    event_club_lectura = {
     'titol': 'Club lectura', 'descripcio': 'Club lectura de genere policiaca. Es busca que es fanatica daquest genere. Per compartir opinions, sugerir nous llibres, llibres llegits.. Junts aprenem més', 'year': 2019,
     'month': 5, 'day': 25, 'hora': '14:00', 'ubicacio': 25, 'creador': 11111, 'actiu': True,
     'etiqueta_A': 72,
       'etiqueta_B': 54, 'etiqueta_C': 0, 'places': '50',
       'tipus': 'Club'}
    inserir_club(event_club_lectura)
    event_altres_mercat = {'titol': 'Mercadillo Boet', 'descripcio': 'Mercadillo del barri Pla den Boet. Dissabte. Gran varietat de productes (roba, complements cuina, llibres, elements per a la llar..), bon pla per passar un dissabte al mati!', 'year': 2019 ,
       'month': 2, 'day': 17, 'hora': '09:00', 'ubicacio': 25, 'creador': 4444, 'actiu': True,
       'etiqueta_A': 108,
       'etiqueta_B': 79, 'etiqueta_C': 0, 'altres_tematica_especifica': 'Mercat',
       'tipus': 'Altres'}
    inserir_altres(event_altres_mercat)
    event_club_pelicules = {'titol':'Club de pel·licules Harry Potter','descripcio':'Club de pel·licules Harry Potter! Tagraden els llibres de la autora JK Rowling? Uneixte i compartim opinions!','year':2019,
            'month':3, 'day':10,'ubicacio':25, 'creador':11111, 'actiu':True,
          'etiqueta_A':79,'etiqueta_B':54,'etiqueta_C':0,
           'hora':'19:25','places':50, 'tipus':'Altres'}
    inserir_club(event_club_pelicules)

    event_esportA = {
   'titol':'3x3 Basquet boet','descripcio': 'Big time show a les pistes exteriors de les pistes exteriors del Boet. Es necessita un minim de 6 jugadors (2 equips) i un maxim de 12 (4 equips). Es busca nivell per tornar amb bona forma a les competicions. Us esperem','year':2019,
   'month':2,'day':25,'hora':'18:00','ubicacio':25,'creador':11111,'actiu':True,'etiqueta_A':92,
                 'etiqueta_B':54,'etiqueta_C':0,'esport_rang':'6 - 12', 'esport_participants':6,
                  'tipus':'Esports'}
    event_esportB = {'titol':'"3x3 MATARO. Palau esportiu Mora"','descripcio': 'sorganitza un torneig de 3x3 patrocinat per Nutrisport. Els equips poden ser de 4 jugadors. Minim dinscrits 4 equips i un maxim de 12. La ubicacio es el Josep Mora. Us esperem!','year':2019,
   'month':2,'day':25,'hora':'18:00','ubicacio':25,'creador':11111,'actiu':True,'etiqueta_A':92,
                 'etiqueta_B':54,'etiqueta_C':0,'esport_rang':'12 - 36', 'esport_participants':6,
                  'tipus':'Esports'}

    inserir_esport(event_esportA)
    inserir_esport(event_esportB)

    event_clubA = {'titol':'Club lectura drama','descripcio':'Club de lectura del gran? Uneixte amb nosaltres i comparteix els teus llibres!','year':2019,
            'month':3, 'day':10, 'ubicacio':25, 'creador':11111, 'actiu':True,
            'etiqueta_A':79,'etiqueta_B':54,'etiqueta_C':0, 'tipus':'Club',
            'hora':'19:25','places':50}
    
    event_clubB = {'titol':'Club lectura terror','descripcio':'Tagrada el terror? Uneixte! Compartim llibres! I si son bons veiem les seves pel·licules. Avorrit no estaras','year':2019,
            'hora':'19:25','month':10, 'day':25, 'ubicacio':25, 'creador':11111, 'actiu':True,
            'etiqueta_A':79,'etiqueta_B':54,'etiqueta_C':0,'tipus':'Club',
            'places':50}
    
    inserir_club(event_clubA)
    inserir_club(event_clubB)
