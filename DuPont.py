# Gegeben seien die Abschlüsse der Firma Practico für das Jahr 2021, sowie Vergangenheitswerte für 2020 (Bilanz). Bestimmen Sie aus diesen Angaben die Eckpunkte des DuPont-Schemas!

def calculate_dupont():
    # Gegebene Werte in kCHF
    umlaufvermoegen_2021 = 3520
    anlagevermoegen_2021 = 4400
    umlaufvermoegen_2020 = 3080
    anlagevermoegen_2020 = 4620

    kurzfristiges_fk_2021 = 1210
    langfristiges_fk_2021 = 2310
    eigenkapital_2021 = 4400

    umsatz_2021 = 6600
    abschreibungen_2021 = 550
    finanz_ergebnis_2021 = 88
    steuern_2021 = 330
    personalaufwand_2021 = 2200
    cloud_hosting_2021 = 550
    uebriger_aufwand_2021 = 2420

    # Berechnungen
    ebit = umsatz_2021 - (personalaufwand_2021 + cloud_hosting_2021 + uebriger_aufwand_2021 + abschreibungen_2021)
    net_profit = ebit - steuern_2021
    net_profit_margin = (net_profit / umsatz_2021) * 100

    assets_avg = ((umlaufvermoegen_2021 + anlagevermoegen_2021) + (umlaufvermoegen_2020 + anlagevermoegen_2020)) / 2
    sales_to_assets_ratio = (umsatz_2021 / assets_avg) * 100
    roa = (net_profit / assets_avg) * 100
    interest_to_assets = (finanz_ergebnis_2021 / assets_avg) * 100
    roi = roa - interest_to_assets
    roe = (net_profit / eigenkapital_2021) * 100

    # Ergebnisse ausgeben
    print(f"EBIT: {ebit:.2f} kCHF")
    print(f"Net Profit: {net_profit:.2f} kCHF")
    print(f"Net Profit Margin: {net_profit_margin:.2f} %")
    print(f"Assets (average): {assets_avg:.2f} kCHF")
    print(f"Sales-to-Assets Ratio: {sales_to_assets_ratio:.2f} %")
    print(f"ROA: {roa:.2f} %")
    print(f"Interest / Assets: {interest_to_assets:.2f} %")
    print(f"ROI: {roi:.2f} %")
    print(f"ROE: {roe:.2f} %")


if __name__ == "__main__":
    calculate_dupont()
