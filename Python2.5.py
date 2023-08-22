print('Anna leiviskät: ')
leivi = float(input())
print('Anna naulat: ')
naula = float(input())
print('Anna luodit: ')
luoti = float(input())

leiviskag = leivi * 20 * 32 * 13.3
naulag = naula * 32 * 13.3
luotig = luoti * 13.3

loppulasku = leiviskag + naulag + luotig

kiloina = loppulasku / 1000

kilot = int(kiloina)

grammat = (kiloina - kilot) * 1000

print(f"Massa nykymittojen mukaan on {kilot} kiloa ja {grammat:.0f} grammaa.")
