def bereken_wisselgeld(bedrag):
    waarden = [
        (5000, "50 euro"),
        (2000, "20 euro"),
        (1000, "10 euro"),
        (500, "5 euro"),
        (200, "2 euro"),
        (100, "1 euro"),
        (50, "50 cent"),
        (20, "20 cent"),
        (10, "10 cent"),
        (5, "5 cent"),
        (1, "1 cent")
    ]

    while bedrag > 0:
        for waarde, naam in waarden:
            if bedrag >= waarde:
                munten = bedrag // waarde
                bedrag -= munten * waarde
                print(f"{munten} x {naam}")
                break

def main():
    bedrag = float(input("Voer een bedrag in centen in: "))
    bereken_wisselgeld(bedrag)

if __name__ == "__main__":
    main()