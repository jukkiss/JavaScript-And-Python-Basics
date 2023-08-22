kuha = int(input("Anna kuhan pituus sentteinä: "))

if kuha < 37:
    minimi = 37 - kuha
    print(f'Kuha on alamittainen {minimi} sentillä, heitä takaisin jontkahan.')
else:
    print('Hieno kala, hyvää ruokahalua.')
