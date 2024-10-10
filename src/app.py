"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/members', methods=['GET'])
def handle_hello():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = members


    return jsonify(response_body), 200



@app.route('/member', methods=['POST'])
def add_member():
    body = request.get_json(force=True)

    if not jackson_family.add_member(body):
        return ({"Message": "Error al agregar familiar"}), 400
    
    return ({"Message": "Familiar agregado exitosamente"}),200

@app.route('/member/<int:id>', methods=['GET'])
def get_single_member(id):
    member = jackson_family.get_member(id)
    if not member:
        return ({"Message": "Error, Familiar no encontrado"}),404
      
    formmated_member = {
        "first_name": member["first_name"],
        "id": member["id"],
        "age": member["age"],
        "lucky_numbers" : member["lucky_numbers"]
    }

    return jsonify(formmated_member),200

@app.route('/member/<int:id>', methods=['DELETE'])
def remove_family_member(id):
    erased = jackson_family.delete_member(id)
    if not erased:
        return ({"Message": "Error al eliminar familiar o familiar no encontrado"})
    
    return jsonify({'done': True, "message": "Familiar eliminado con éxito"}), 200











   
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
