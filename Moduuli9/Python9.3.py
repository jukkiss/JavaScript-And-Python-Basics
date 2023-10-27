import random
from auto import Auto

auto1 = Auto("ABC-123", 143)
auto1.kiihdytä(60)
auto1.kulje(1.5)
print(f"Auton matka on {auto1.matka} km/h.")
