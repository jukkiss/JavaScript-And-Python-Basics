from auto import Auto

auto1 = Auto("ABC-123", 143)
auto1.kiihdytä(30)
print(f"Auton nopeus on {auto1.nopeus}")
auto1.kiihdytä(70)
print(f"Auton nopeus on {auto1.nopeus}")
auto1.kiihdytä(50)
print(f"Auton nopeus on {auto1.nopeus}")
auto1.kiihdytä(-200)
print(f"Auton nopeus on {auto1.nopeus}")

