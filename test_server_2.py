#!/usr/bin/env python2
'''A small program to demo Flask as the basis of a REST web service.

Author: Sebastian Oliva (200815609@ingenieria.usac.edu.gt)
'''

import json
import uuid
import random

from flask import Flask, session, request, render_template, jsonify, Response


app = Flask("EDD_codigo_ejemplo_proyecto1")


class Plane(object):
  '''Object that we use to model planes with name, id, and status.'''
  STATUS_STRINGS = ["flying", "landing"] 
    
  def __init__(self, name, model):
    self.id = uuid.uuid4()
    self.name = name.title()
    self.model = model
    self.status = 0

  def aterrizar(self):
    self.status = 1
   
  def create_public_view(self):
    return {"name": self.name, "id": unicode(self.id), "status": Plane.STATUS_STRINGS[self.status]}


planes_list = []

for i in range(10):
  nombre = "avion " + unicode(i)
  avion_o = Plane(random.choice(["Aadvark", "Pinguino", "Elefante"])+" "+random.choice(["Azul","Verde","Naranja"]), random.choice(["787-DreamLiner", "737", "747", "A380", "A320", "A340"]))
  planes_list.append(avion_o)


@app.route('/aviones/')
def display_chatbot_ui():
##     direccion_obj = {
##         "linea1": "blarblar",
##         "pais": "GT"
##     }
##     destinatario = {
##       "nombre": "mi_nombre",
##       "direccion": direccion_obj
##     }

  # Jsonify no funciona aqui
  planes_objects_list = map(lambda plane: plane.create_public_view(), planes_list)
  return Response(json.dumps(planes_objects_list), mimetype="application/json")
  

@app.route('/aviones/agregar', methods=['POST'])
def create_plane():
  '''Creates a plane instance based on a POST form with name and model set, returns the object.
  
  Useage sample: $ curl -X POST -d "name=avioncio&model=797-5000" http://localhost:5000/aviones/agregar  
  '''
    
  name_sent = request.form['name']
  model_sent = request.form['model']
  plane = Plane(name_sent, model_sent)
  app.logger.debug(unicode(plane.create_public_view()))
  planes_list.append(plane)
  return jsonify(plane.create_public_view())


@app.route('/saludar')
def saludarme():
  return "Hola mundo!"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')