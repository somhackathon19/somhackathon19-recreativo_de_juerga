# GRUP N. 9: MATCONN
## Desenvolupament
### Front-end
Desenvolupat amb Cordova, Framework7, Vue.js, Element.io
### Back-end
Desenvolupat amb Flask, peewee. Deployed a DigitalOcean.
### Xarxa Neuronal
Desenvolupada amb Python i numpy.
Executar `Back-end/full_neural_network.py`
## Testeig de l'API
Droplet public a:
157.230.45.171:5000/
Exemples de consultes:
  - GET esport event
    `curl -i http://157.230.45.171:500/api/esdeveniment/esport`
  - GET club event
    `curl -i http://157.230.45.171:500/api/esdeveniment/club`
  - GET altre event
    `curl -i http://157.230.45.171:500/api/esdeveniment/altre`
  - GET esport event by id
    `curl -i http://157.230.45.171:500/api/esdeveniment/esport/[id]`
  - GET altre event by id
    `curl -i http://157.230.45.171:500/api/esdeveniment/altre/[id]`
  - GET club event by id
    `curl -i http://157.230.45.171:500/api/esdeveniment/club/[id]`
  - GET etiquetes
    `curl -i http://157.230.45.171:500/api/etiquetes`
  - PUT sport event:
    `curl -i -H "Content-Type: application/json" -X PUT -d
     {
          "actiu": true,
          "creador": 4444,
          "day": 25,
          "descripcio": "3x3 MATARO. Palau esportiu Mora",
          "esport_participants": 8,
          "esport_rang": "6-12",
          "etiqueta_A": 92,
          "etiqueta_B": 108,
          "etiqueta_C": 0,
          "hora": "17:00",
          "month": 2,
          "tipus": "Esports",
          "titol": "3x3 Mataro",
          "ubicacio": 25,
          "year": 2019
        }
        http://157.230.45.171:500/api/esdeveniments/post/esport'
