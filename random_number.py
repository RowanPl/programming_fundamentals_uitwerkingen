# In deze opdracht ga je een script schrijven waarbij de gebruikter een geheim getal moet raden.
#
# Stappenplan:
#
# 1. Maak een variable "random_getal" en geef deze een willekeurige integer waarde tussen 1 en 10.
# 2. Vraag de gebruiker om het getal te raden
# 3. Gebruik een while-loop die blijft draaien zolang de gebruiker het verkeerde getal raadt.
# 4. Geef feedback of de ingevoerde waarde te hoog of te laag is.
# 5. Wanneer de gebruiker het juiste getal raadt, beëindig de loop en print een felicitatiebericht.
#
# BONUS: Gebruik `import random` en `random.randomInt(1, 10)` om je geheime getal mee te maken
# en deze zo ook voor jezelf geheim te houden.

import random

random_number = random.randint(1, 10)
guess = int(input("Raad het getal tussen 1 en 10: "))
attempts = 0

while guess != random_number:
    if guess < random_number:
        print("Het getal is te laag. Probeer het opnieuw.")
    else:
        print("Het getal is te hoog. Probeer het opnieuw.")
    guess = int(input("Raad het getal tussen 1 en 10: "))
    attempts += 1

print(f"Gefeliciteerd! Je hebt het getal geraden in {attempts} pogingen.")



