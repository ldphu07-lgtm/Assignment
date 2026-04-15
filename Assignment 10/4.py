from flask import Flask
import json

app = Flask(__name__)

airport_db = {
    "LFLL": {"name": "Lyon Saint-Exupery Airport", "city": "Lyon", "country": "FR"},
    "VVTS": {"name": "Tan Son Nhat International Airport", "city": "Ho Chi Minh City", "country": "VN"}
}

@app.route('/airport/<string:icao>')
def get_airport(icao):
    icao = icao.upper()
    if icao in airport_db:
        response = {
            "icao": icao,
            "name": airport_db[icao]["name"],
            "city": airport_db[icao]["city"],
            "country": airport_db[icao]["country"]
        }
        return json.dumps(response), 200
    else:
        return json.dumps({"error": "Airport not found"}), 404

if __name__ == '__main__':
    app.run(host = '127.0.0.1', port = 5000)
