from flask import Flask, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  

sustancias = [
    {"name": "Cloruro de vinilo", "cas": "75-01-4"},
    {"name": "Metileno-bis (2-cloroanilina) (MBOCA)", "cas": "101-14-4"},
    {"name": "Estireno (fenil etileno)", "cas": "100-42-5"},
    {"name": "Dinitrotolueno", "cas": "121-14-2"},
    {"name": "Acrilonitrilo", "cas": "107-13-1"},
    {"name": "Tetracloruro de carbono", "cas": "56-23-5"},
    {"name": "Hidracina", "cas": "302-01-2"},
    {"name": "Benzo(a)pireno", "cas": "50-32-8"},
    {"name": "Acrilamina", "cas": "79-06-1"},
    {"name": "Benceno", "cas": "71-43-2"},
    {"name": "Cloruro de metileno", "cas": "75-09-2"},
    {"name": "Dioxano", "cas": "123-91-1"},
    {"name": "Butadieno", "cas": "106-99-0"},
    {"name": "Tolueno diisocianato", "cas": "26471-62-5"},
    {"name": "Amino difenilo", "cas": "92-67-1"},
    {"name": "Dicloroetano", "cas": "107-06-2"},
    {"name": "Oxido de etileno", "cas": "75-21-8"}
]

estados = [
    "Aguascalientes", "Baja California", "Baja California Sur", "Campeche",
    "Chiapas", "Chihuahua", "Ciudad de México", "Coahuila", "Colima", "Durango",
    "Estado de México", "Guanajuato", "Guerrero", "Hidalgo", "Jalisco", "Michoacán",
    "Morelos", "Nayarit", "Nuevo León", "Oaxaca", "Puebla", "Querétaro", "Quintana Roo",
    "San Luis Potosí", "Sinaloa", "Sonora", "Tabasco", "Tamaulipas", "Tlaxcala", "Veracruz",
    "Yucatán", "Zacatecas"
]

@app.route('/api/sustancias', methods=['GET'])
def get_sustancias():
    return jsonify({"sustancias": sustancias, "estados": estados})

if __name__ == '__main__':
    app.run(debug=True)
