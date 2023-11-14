import mysql.connector
from flask import Flask

yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='admin',
    autocommit=True
)

app = Flask(__name__)
@app.route('/kenttä/<icao>')
def haeLentokentta(icao):
    sql = '''
    SELECT ident as 'icao', name, municipality
    FROM airport
    WHERE ident = %s
    '''
    kursori = yhteys.cursor(dictionary=True)
    kursori.execute(sql, (icao,))
    tulos = kursori.fetchone()
    return tulos

if __name__ == '__main__':
    app.run(use_reloader=True, host='127.0.0.1', port=3000)
