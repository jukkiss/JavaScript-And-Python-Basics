suku = input("Anna biologinen sukupuolesi: Nainen tai Mies. ").upper()
hemo = int(input("Anna hemoglobiiniarvosi g/l: "))

if suku == "NAINEN":
    if hemo < 117:
        print("Hemoglobiinisi on alhainen.")
    elif hemo > 175:
        print("Hemoglobiinisi on korkea.")
    else:
        print("Hemoglobiinisi on normaali.")

if suku == "MIES":
    if hemo < 134:
        print("Hemoglobiinisi on alhainen.")
    elif hemo > 195:
        print("Hemoglobiinisi on korkea.")
    else:
        print("Hemoglobiinisi on normaali.")
