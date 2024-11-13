from flask import Flask, jsonify
import mysql.connector

app = Flask(__name__)

db_config = {
    "host": "127.0.0.1",
    "port": 3306,
    "user": "python",
    "password": "salasana",
    "database": "flight_game"
}

def fetch_airport_info(icao_code):
    connection = mysql.connector.connect(**db_config)
    cursor = connection.cursor(dictionary=True)
    query = "SELECT name, municipality FROM airport WHERE ident = %s"
    cursor.execute(query, (icao_code,))
    result = cursor.fetchone()
    cursor.close()
    connection.close()
    return result

@app.route("/kenttä/<string:icao_code>", methods=['GET'])
def get_airport(icao_code):
    airport = fetch_airport_info(icao_code)
    if airport:
        tulos = {
            "ICAO": icao_code,
            "Name": airport["name"],
            "Municipality": airport["municipality"]
        }
        return jsonify(tulos)
    else:
        return jsonify({"error": "Lentokenttää ei löytynyt"}), 404

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
