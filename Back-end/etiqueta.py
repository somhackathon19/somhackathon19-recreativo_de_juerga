from global_database import * 

class Etiqueta(Model):
    id = IntegerField(primary_key = True)
    nom = TextField()

    class Meta:
        database = db

def init_database():
    db.create_tables([Etiqueta], safe = True)

def get_nom(id):
    etiqueta = Etiqueta.select(Etiqueta.nom).where(Etiqueta.id == id)
    return etiqueta


def parsejar_etiqueta(etiqueta):
    dades = {'id':etiqueta.id,'nom':etiqueta.nom}
    return dades

def get_all_tags():
    return Etiqueta.select()

def inserir_etiqueta(dades):
    etiqueta = Etiqueta.create(nom = dades.get('nom'))
    return etiqueta

def generar_dades():
## Etiquetes events
    etiqueta_basquet_mati = {'nom':'Basquet - mati'}
    etiqueta_basquet_tarda = {'nom':'Basquet - tarda'}
    etiqueta_basquet_nit = {'nom':'Basquet - nit'}

    etiqueta_futbol_mati = {'nom':'Futbol - mati'}
    etiqueta_futbol_tarda = {'nom':'Futbol - tarda'}
    etiqueta_futbol_nit = {'nom':'Futbol - nit'}

    etiqueta_escacs_mati = {'nom':'Escacs - mati'}
    etiqueta_escacs_tarda = {'nom':'Escacs - tarda'}
    etiqueta_escacs_nit = {'nom':'Escacs - nit'}

    etiqueta_club_lectura = {'nom':'Club lectura'}
    etiqueta_club_pelicules = {'nom':'Club pelicules'}
    etiqueta_club_futbol = {'nom':'Club futbol'}


    etiqueta_bici_mati = {'nom':'Bici - mati'}
    etiqueta_bici_tarda = {'nom':'Bici - tarda'}
    etiqueta_bici_nit = {'nom':'Bici - nit'}

    etiqueta_excursions = {'nom':'Excursions'}
    etiqueta_mercat = {'nom':'Mercat'}

    # Etiquetes barris
    etiqueta_barri_boet = {'nom':'Boet'}
    etiqueta_barri_eixample = {'nom':'Eixample'}
    etiqueta_barri_centre = {'nom':'Centre'}
    etiqueta_barri_escorxador = {'nom':'El palau escorxador'}
    etiqueta_barri_rocafonda = {'nom':'Rocafonda'}
    etiqueta_barri_molins = {'nom':'Els molins'}
    etiqueta_barri_vista_alegre = {'nom':'Vista alegre'}
    etiqueta_barri_cirera = {'nom':'Cirera'}
    etiqueta_barri_llantia = {'nom':'Llantia'}
    etiqueta_barri_cerdanyola = {'nom':'Cerdanyola'}
    etiqueta_barri_peramas = {'nom':'Peramas'}

    inserir_etiqueta(etiqueta_basquet_mati)
    inserir_etiqueta(etiqueta_basquet_tarda)
    inserir_etiqueta(etiqueta_basquet_nit)
    inserir_etiqueta(etiqueta_futbol_mati)
    inserir_etiqueta(etiqueta_futbol_tarda)
    inserir_etiqueta(etiqueta_futbol_nit)
    inserir_etiqueta(etiqueta_escacs_mati)
    inserir_etiqueta(etiqueta_escacs_tarda)
    inserir_etiqueta(etiqueta_escacs_nit)

    inserir_etiqueta(etiqueta_club_lectura)
    inserir_etiqueta(etiqueta_club_pelicules)
    inserir_etiqueta(etiqueta_club_futbol)

    inserir_etiqueta(etiqueta_bici_mati)
    inserir_etiqueta(etiqueta_bici_tarda)
    inserir_etiqueta(etiqueta_bici_nit)

    inserir_etiqueta(etiqueta_excursions)
    inserir_etiqueta(etiqueta_mercat)

    inserir_etiqueta(etiqueta_barri_boet)
    inserir_etiqueta(etiqueta_barri_eixample)
    inserir_etiqueta(etiqueta_barri_centre)
    inserir_etiqueta(etiqueta_barri_escorxador)
    inserir_etiqueta(etiqueta_barri_rocafonda)
    inserir_etiqueta(etiqueta_barri_molins)
    inserir_etiqueta(etiqueta_barri_vista_alegre)
    inserir_etiqueta(etiqueta_barri_cirera)
    inserir_etiqueta(etiqueta_barri_llantia)
    inserir_etiqueta(etiqueta_barri_cerdanyola)
    inserir_etiqueta(etiqueta_barri_peramas)