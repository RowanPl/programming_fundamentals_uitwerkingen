#
# Schrijf een programma voor kassa medewerkers waarin je een bedrag (in centen) invoert, bijvoorbeeld 87 cent,
# en het programma geeft terug hoeveel munten van 50, 20, 10, 5, en 1 cent je terug zou moeten geven.
# Het programma gebruikt een while-loop om de berekening stap voor stap uit te voeren,
# telkens de grootste munt eraf halend totdat het bedrag nul is.
#
# Stappenplan:
#
# 1. Vraag de gebruiker om een bedrag in centen in te voeren (bijvoorbeeld 87).
#       (Bonus: check of de gebruiker niet meer dan 100 invoert)
# 2. Gebruik een while-loop om telkens de grootste muntwaarde van het bedrag af te trekken.
#    De loop stopt wanneer het bedrag nul is.
# 3. Maak in de while-loop, voor elke munt waarde een (nested) if-statement, waarin je het volgende doet:
#       - Bereken hoevaak die muntwaarde in het bedrag past.
#       - Trek zo vaak de muntwaarde van het bedrag af,
#         zodat de volgende iteratie van de while-loop het aangepast bedrag gebruikt
#       - Print hoeveel munten van deze waarde de gebruiker terug moet krijgen.
#
# Bonus: Breid het programma uit, zodat het ook briefgeld en euro munten kan teruggeven.

# De beschikbare muntwaarden
vijftig_cent = 50
twintig_cent = 20
tien_cent = 10
vijf_cent = 5
een_cent = 1


# Stap 1: Vraag de gebruiker om een bedrag in centen in te voeren
bedrag = float(input("Voer een bedrag in centen in: "))

# Bonus: check of de gebruiker niet meer dan 100 invoert
# if bedrag > 100:
#     print("Het bedrag mag niet meer dan 100 cent zijn.")
#     exit()
#
# # Stap 2: Gebruik een while-loop om telkens de grootste muntwaarde van het bedrag af te trekken
#
# while bedrag > 0:
#     # Stap 3: Maak in de while-loop, voor elke munt waarde een (nested) if-statement
#     if bedrag >= vijftig_cent:
#         munten = bedrag // vijftig_cent
#         bedrag -= munten * vijftig_cent
#         print(f"{munten} x 50 cent")
#     elif bedrag >= twintig_cent:
#         munten = bedrag // twintig_cent
#         bedrag -= munten * twintig_cent
#         print(f"{munten} x 20 cent")
#     elif bedrag >= tien_cent:
#         munten = bedrag // tien_cent
#         bedrag -= munten * tien_cent
#         print(f"{munten} x 10 cent")
#     elif bedrag >= vijf_cent:
#         munten = bedrag // vijf_cent
#         bedrag -= munten * vijf_cent
#         print(f"{munten} x 5 cent")
#     elif bedrag >= een_cent:
#         munten = bedrag // een_cent
#         bedrag -= munten * een_cent
#         print(f"{munten} x 1 cent")
#     else:
#         break

# Bonus: Breid het programma uit, zodat het ook briefgeld en euro munten kan teruggeven.
# De beschikbare briefgeldwaarden
vijftig_euro = 5000
twintig_euro = 2000
tien_euro = 1000
vijf_euro = 500

# De beschikbare euromunten
twee_euro = 200
een_euro = 100
vijftig_cent_euro = 50
twintig_cent_euro = 20
tien_cent_euro = 10
vijf_cent_euro = 5

while bedrag > 0:
    if bedrag >= vijftig_euro:
        munten = bedrag // vijftig_euro
        bedrag -= munten * vijftig_euro
        print(f"{munten} x 50 euro")
    elif bedrag >= twintig_euro:
        munten = bedrag // twintig_euro
        bedrag -= munten * twintig_euro
        print(f"{munten} x 20 euro")
    elif bedrag >= tien_euro:
        munten = bedrag // tien_euro
        bedrag -= munten * tien_euro
        print(f"{munten} x 10 euro")
    elif bedrag >= vijf_euro:
        munten = bedrag // vijf_euro
        bedrag -= munten * vijf_euro
        print(f"{munten} x 5 euro")
    elif bedrag >= twee_euro:
        munten = bedrag // twee_euro
        bedrag -= munten * twee_euro
        print(f"{munten} x 2 euro")
    elif bedrag >= een_euro:
        munten = bedrag // een_euro
        bedrag -= munten * een_euro
        print(f"{munten} x 1 euro")
    elif bedrag >= vijftig_cent_euro:
        munten = bedrag // vijftig_cent_euro
        bedrag -= munten * vijftig_cent_euro
        print(f"{munten} x 50 cent")
    elif bedrag >= twintig_cent_euro:
        munten = bedrag // twintig_cent_euro
        bedrag -= munten * twintig_cent_euro
        print(f"{munten} x 20 cent")
    elif bedrag >= tien_cent_euro:
        munten = bedrag // tien_cent_euro
        bedrag -= munten * tien_cent_euro
        print(f"{munten} x 10 cent")
    elif bedrag >= vijf_cent_euro:
        munten = bedrag // vijf_cent_euro
        bedrag -= munten * vijf_cent_euro
        print(f"{munten} x 5 cent")
    elif bedrag >= een_cent:
        munten = bedrag // een_cent
        bedrag -= munten * een_cent
        print(f"{munten} x 1 cent")
    else:
        break