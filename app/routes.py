from app.models.planet import Planet
from flask import request, Blueprint, make_response, jsonify
from app import db

planets_bp = Blueprint("planets", __name__, url_prefix="/planets")

@planets_bp.route("", methods=["GET","POST"])
def handle_planets():
    if request.method == "GET":
        planets = Planet.query.all()
        planets_response = []
        for planet in planets:
            planets_response.append({
                "id" : planet.id,
                "name" : planet.name,
                "description" : planet.description,
                "distance from earth" : planet.distance_from_earth
            })
        return jsonify(planets_response)
    
    elif request.method == "POST":
        request_body = request.get_json()
        new_planet = Planet(name=request_body["name"],
                            description=request_body["description"],
                            distance_from_earth=request_body["distance from earth"]
                            )
        db.session.add(new_planet)
        db.session.commit()

        return make_response(f"Planet {new_planet.name} was successfully added", 201)
    
@planets_bp.route("/<planet_id>", methods=["GET"])
def handle_planet(planet_id):
    planet = Planet.query.get(planet_id)

    return{
        "id" : planet.id,
        "name" : planet.name,
        "description" : planet.description,
        "distance_from_earth" : planet.distance_from_earth
    }