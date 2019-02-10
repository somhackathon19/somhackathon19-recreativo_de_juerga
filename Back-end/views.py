from flask import render_template, jsonify, abort, make_response, request, url_for
import flask
from flask_cors import CORS

from ubication import *
import ubication
from user import *
import user

import event

from subscripcio import *
import subscripcio
from inscripcio import *
import inscripcio
from chat import *
import chat
from etiqueta import *
import etiqueta


# Required for API:

app = flask.Flask(__name__)


@app.route("/test_api")
def test_api():
    #user_obj = ubication.Ubication.select()
    #json_data = json.dumps(model_to_dict(user_obj))
    # NO PETA:
    ubications = ubication.get_ubicacions()
    print("resultat ubicacions:")
    print (ubications)
    for u in ubications:
        print(u.latitude)
    return "Hellow world"


# Get Methods


@app.route("/omplir_dades")
def omplir_dades():
    print("Generant events")
    event.data_faker()
    return "Omplint dades"


@app.route('/api/esdeveniment/esport')
def get_event_esport():
    llistat_events = event.get_events('Esports')
    llistat_parsejat = list()
    for e in llistat_events:
        e = event.parsejar_esport(e)
        llistat_parsejat.append(e)
    
    response = flask.jsonify(llistat_parsejat)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/api/esdeveniment/altres")
def get_event_altres():
    print("Altres")
    llistat_events = event.get_event_altres()
    llistat_parsejat = list()
    for e in llistat_events:
        e = event.parsejar_altres(e)
        llistat_parsejat.append(e)
    
    response = flask.jsonify(llistat_parsejat)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/api/esdeveniment/club")
def get_event_club():
    print("Club")
    llistat_events = event.get_event_club()
    llistat_parsejat = list()
    for e in llistat_events:
        e = event.parsejar_esport(e)
        llistat_parsejat.append(e)
    
    response = flask.jsonify(llistat_parsejat)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/api/etiquetes")
def get_event_etiquetes():
    e = etiqueta.get_all_tags()
    llistat_etiquetes = list()
    for a in e:
        a = etiqueta.parsejar_etiqueta(a)
        llistat_etiquetes.append(a)

    response = flask.jsonify(llistat_etiquetes)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response

@app.route("/api/esdeveniment/<id>")
def get_esdeveniment_id(id = id):
    response = flask.jsonify(event.get_event(id))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/api/esdeveniment/esport/<id>")
def get_esdeveniment_esport_id(id = id):
    response = flask.jsonify(event.get_event(id))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response


@app.route("/api/esdeveniment/club/<id>")
def get_esdeveniment_club_id(id = id):
    response = flask.jsonify(event.get_event(id))
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
# Post methods

@app.route('/api/esdeveniments/post/esport', methods=['POST'])
def post_esdeveniment_esport():
    #if not request.json or not 'id' in request.json:
    #    abort(400)
    #parser = event.parsejar_esport(request.json)
    event.inserir_esport(request.json)
    
    #return jsonify
    response = flask.jsonify(request.json)
    response.headers.add('Access-Control-Allow-Origin', '*')
    return response
    
@app.route('/api/ubicacio/<id>')
def get_ubicacio(id):
    ubi =  ubication.get_ubicacio(id)
    return jsonify(ubi)

"""
@page.route('/api/v1.0/tests', methods=['POST'])
@auth.login_required
def create_test():
    if not request.json or not 'title' in request.json:
        abort(400)
    test = {
        'id': tests[-1]['id'] + 1,
        'title': request.json['title'],
        'description': request.json.get('description', ""),
        'done': False
    }
    tests.append(test)
return jsonify({'test': test}), 201
"""


if __name__ == "__main__":
    app.run(debug = True)
    CORS(app)