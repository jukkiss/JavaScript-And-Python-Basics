import mysql.connector

def hae(icao):
    sql = "SELECT name, municipality, ident FROM airport"
    sql += " WHERE ident='" + icao + "'"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"Lentokentän kunta on {rivi[1]}.")
    return


yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='admin',
    autocommit=True
)

icao = input("Anna lentokentän ICAO-koodi, nähdäksesi lentokentän sijaintikunnan: ")
hae(icao)