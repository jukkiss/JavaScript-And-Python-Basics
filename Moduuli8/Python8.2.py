import mysql.connector

def hae(maa):
    sql = "SELECT TYPE, COUNT(*), type FROM airport"
    sql += " WHERE iso_country='" + maa + "' GROUP BY type"
    kursori = yhteys.cursor()
    kursori.execute(sql)
    tulos = kursori.fetchall()
    print("Ohessa kentän lukumäärät tyypeittäin.")
    if kursori.rowcount >0 :
        for rivi in tulos:
            print(f"{rivi[2]} {rivi[1]}.")
    return


yhteys = mysql.connector.connect(
    host='localhost',
    port=3306,
    database='flight_game',
    user='root',
    password='admin',
    autocommit=True
)

maa = input("Anna maatunnus tulostaaksesi maassa olevat lentokentät tyypeittäin: ")
hae(maa)