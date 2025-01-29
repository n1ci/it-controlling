# Gegeben seien 3 Produkte A, B und C mit folgenden Angaben:
#
# Produkt	A	B	C
# Absatzmengen	3000	1800	2000
# Produktionsmengen	2800	1800	1600
# Herstellkosten pro Stück	4	12	9.5
# Verwaltungs- und Vertriebskosten pro Stück	3	8	6
# Verkaufspreis pro Stück	10	30	28
# Aufgabe: Berechnen Sie den kurzfristigen Betriebsgewinn nach dem Gesamtkostenverfahren!
# Gesamtkostenverfahren
# Gesamte Herstellkosten	CHF Antwort 1 Frage 4
# 48000
# Umsatzerlöse A	CHF Antwort 2 Frage 4
# 30000
# Gesamte Verwaltungs- und Vertriebskosten	CHF Antwort 3 Frage 4
# 35400
# Umsatzerlöse B	CHF Antwort 4 Frage 4
# 54000
# Betriebsgewinn	CHF Antwort 5 Frage 4
# 52000
# Umsatzerlöse C	CHF Antwort 6 Frage 4
# 56000
#  	 	Bestandesveränderung zu Herstellkosten gesamt	CHF -4600
# Total	CHF Antwort 7 Frage 4
# 135400
# Total	CHF 135400


def calculate_operating_profit_with_soll_haben():
    # Gegebene Daten
    products = {
        "A": {
            "absatzmenge": 3000,
            "produktionsmenge": 2800,
            "herstellkosten_pro_stueck": 4,
            "verwaltungsvertriebskosten_pro_stueck": 3,
            "verkaufspreis_pro_stueck": 10,
        },
        "B": {
            "absatzmenge": 1800,
            "produktionsmenge": 1800,
            "herstellkosten_pro_stueck": 12,
            "verwaltungsvertriebskosten_pro_stueck": 8,
            "verkaufspreis_pro_stueck": 30,
        },
        "C": {
            "absatzmenge": 2000,
            "produktionsmenge": 1600,
            "herstellkosten_pro_stueck": 9.5,
            "verwaltungsvertriebskosten_pro_stueck": 6,
            "verkaufspreis_pro_stueck": 28,
        },
    }

    # Berechnungen
    gesamte_herstellkosten = 0
    gesamtkosten_vv = 0
    umsatzerloese = {"A": 0, "B": 0, "C": 0}
    bestandsveraenderung = 0

    for product, data in products.items():
        herstellkosten = data["produktionsmenge"] * data["herstellkosten_pro_stueck"]
        vv_kosten = data["absatzmenge"] * data["verwaltungsvertriebskosten_pro_stueck"]
        umsatz = data["absatzmenge"] * data["verkaufspreis_pro_stueck"]
        bestand = (data["produktionsmenge"] - data["absatzmenge"]) * data["herstellkosten_pro_stueck"]

        gesamte_herstellkosten += herstellkosten
        gesamtkosten_vv += vv_kosten
        umsatzerloese[product] = umsatz
        bestandsveraenderung += bestand

    # Betriebsgewinn berechnen
    betriebsgewinn = sum(umsatzerloese.values()) - gesamte_herstellkosten - gesamtkosten_vv + bestandsveraenderung

    # Soll- und Haben-Seite
    soll = {
        "Gesamte Herstellkosten": gesamte_herstellkosten,
        "Gesamte Verwaltungs- und Vertriebskosten": gesamtkosten_vv,
        "Betriebsgewinn": betriebsgewinn,
    }

    haben = {
        "Umsatzerlöse A": umsatzerloese["A"],
        "Umsatzerlöse B": umsatzerloese["B"],
        "Umsatzerlöse C": umsatzerloese["C"],
        "Bestandsveränderung zu Herstellkosten gesamt": bestandsveraenderung,
    }

    # Totals berechnen
    soll_total = sum(soll.values())
    haben_total = sum(haben.values())

    # Ergebnisse ausgeben
    print("Soll-Seite:")
    for key, value in soll.items():
        print(f"{key}: {value:.2f} CHF")

    print("\nHaben-Seite:")
    for key, value in haben.items():
        print(f"{key}: {value:.2f} CHF")

    print(f"\nTotal Soll: {soll_total:.2f} CHF")
    print(f"Total Haben: {haben_total:.2f} CHF")

if __name__ == "__main__":
    calculate_operating_profit_with_soll_haben()
