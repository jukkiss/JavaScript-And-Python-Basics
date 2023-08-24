
sentit = input("Anna tuumat: ")

while sentit != sentit.startswith("-"):
    if sentit.startswith("-"):
        break
    tuuma = int(sentit) / 2.54

    print(f"Tulos on {tuuma:.2f} senttiä.")
    sentit = input("Anna sentit: ")
