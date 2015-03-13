#!/usr/bin/env python2
import json
import uuid

from flask import Flask, session, request, render_template, jsonify


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
  planes_list = {"id": unicode(uuid.uuid4()), "nombre": nombre}
  aviones.append(avion_o)


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
  return flask.Response(json.dumps(planes_objects_list), mimetype="application/json")
  

@app.route('/aviones/agregar', methods=['POST'])
def create_message():
  message_sent = request.form['message']
  app.logger.debug(message_sent)
  return "creado :"+ message_sent


@app.route('/saludar')
def saludarme():
  return "Hola mundo!"


if __name__ == "__main__":
  app.run(debug=True, host='0.0.0.0')