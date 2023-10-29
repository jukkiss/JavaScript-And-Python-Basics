from auto import Sähköauto, Polttomoottoriauto

sauto = Sähköauto("ABC-15", 180,52.5)
pauto = Polttomoottoriauto("ACD-123",165,32.3)

sauto.kiihdytä(80)
pauto.kiihdytä(60)

sauto.kulje(3)
pauto.kulje(3)

print(f"Sähköauton matkamittarilukema: {sauto.matka}. Polttomoottoriauton matkamittarilukema: {pauto.matka}.")