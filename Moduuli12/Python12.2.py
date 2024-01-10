import requests
def kelvinmuunnin(kelvin):
    return kelvin - 273.15


avain = "api here"
kaupunki = input("Anna kaupungin nimi: ")
pyyntö = f"http://api.openweathermap.org/data/2.5/weather?q={kaupunki}&appid={avain}"

try:
    vastaus = requests.get(pyyntö)
    json_vastaus = vastaus.json()

    if vastaus.status_code==200:
        sää = json_vastaus["weather"][0]["description"]
        kelvin_asteet = json_vastaus["main"]["temp"]
        celsius_asteet = kelvinmuunnin(kelvin_asteet)
        print(F"Paikkakunta: {kaupunki}. Sään kuvaus: {sää}. Lämpötila {celsius_asteet:.2f} C")
except requests.exceptions.RequestException as e:
    print("Haku epäonnistui")


