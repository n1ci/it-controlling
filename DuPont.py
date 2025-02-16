def calculate_dupont(params):
    """
    Berechnet die Eckpunkte des DuPont-Schemas basierend auf den verfügbaren Parametern.
    Fehlende Parameter werden ignoriert.

    :param params: Dictionary mit Parametern und Werten (in kCHF)
    """
    # Extrahiere Werte aus params, falls vorhanden
    umlaufvermoegen_2021 = params.get("umlaufvermoegen_2021", 0)
    anlagevermoegen_2021 = params.get("anlagevermoegen_2021", 0)
    umlaufvermoegen_2020 = params.get("umlaufvermoegen_2020", 0)
    anlagevermoegen_2020 = params.get("anlagevermoegen_2020", 0)
    eigenkapital_2021 = params.get("eigenkapital_2021", 0)
    kurzfristiges_fk_2021 = params.get("kurzfristiges_fk_2021", 0)
    langfristiges_fk_2021 = params.get("langfristiges_fk_2021", 0)
    umsatz_2021 = params.get("umsatz_2021", 0)
    abschreibungen_2021 = params.get("abschreibungen_2021", 0)
    finanz_ergebnis_2021 = params.get("finanz_ergebnis_2021", 0)
    steuern_2021 = params.get("steuern_2021", 0)
    personalaufwand_2021 = params.get("personalaufwand_2021", 0)
    cloud_hosting_2021 = params.get("cloud_hosting_2021", 0)
    uebriger_aufwand_2021 = params.get("uebriger_aufwand_2021", 0)

    # Berechnungen (nur wenn die notwendigen Parameter vorhanden sind)
    total_assets_2021 = umlaufvermoegen_2021 + anlagevermoegen_2021
    total_assets_2020 = umlaufvermoegen_2020 + anlagevermoegen_2020
    total_assets_avg = (total_assets_2021 + total_assets_2020) / 2 if total_assets_2021 and total_assets_2020 else None

    total_liabilities_2021 = kurzfristiges_fk_2021 + langfristiges_fk_2021
    total_equity_and_liabilities = total_assets_2021

    fremdkapitalquote = (total_liabilities_2021 / total_assets_2021) * 100 if total_liabilities_2021 and total_assets_2021 else None
    eigenkapitalquote = (eigenkapital_2021 / total_assets_2021) * 100 if eigenkapital_2021 and total_assets_2021 else None
    verschuldungsgrad = (total_liabilities_2021 / eigenkapital_2021) * 100 if total_liabilities_2021 and eigenkapital_2021 else None

    ebit = umsatz_2021 - sum(
        filter(None, [personalaufwand_2021, cloud_hosting_2021, uebriger_aufwand_2021, abschreibungen_2021])
    )
    net_profit = ebit - steuern_2021 if ebit and steuern_2021 else None
    net_profit_margin = (net_profit / umsatz_2021) * 100 if net_profit and umsatz_2021 else None
    sales_to_assets_ratio = (umsatz_2021 / total_assets_avg) * 100 if umsatz_2021 and total_assets_avg else None
    roa = (net_profit / total_assets_avg) * 100 if net_profit and total_assets_avg else None
    interest_to_assets = (finanz_ergebnis_2021 / total_assets_avg) * 100 if finanz_ergebnis_2021 and total_assets_avg else None
    roi = roa - interest_to_assets if roa and interest_to_assets else None
    roe = (net_profit / eigenkapital_2021) * 100 if net_profit and eigenkapital_2021 else None

    # Ergebnisse ausgeben
    print(f"EBIT: {ebit:.2f} kCHF" if ebit else "EBIT: Nicht berechenbar")
    print(f"Net Profit: {net_profit:.2f} kCHF" if net_profit else "Net Profit: Nicht berechenbar")
    print(f"Net Profit Margin: {net_profit_margin:.2f} %" if net_profit_margin else "Net Profit Margin: Nicht berechenbar")
    print(f"Assets (average): {total_assets_avg:.2f} kCHF" if total_assets_avg else "Assets (average): Nicht berechenbar")
    print(f"Sales-to-Assets Ratio: {sales_to_assets_ratio:.2f} %" if sales_to_assets_ratio else "Sales-to-Assets Ratio: Nicht berechenbar")
    print(f"ROA: {roa:.2f} %" if roa else "ROA: Nicht berechenbar")
    print(f"Interest / Assets: {interest_to_assets:.2f} %" if interest_to_assets else "Interest / Assets: Nicht berechenbar")
    print(f"ROI: {roi:.2f} %" if roi else "ROI: Nicht berechenbar")
    print(f"ROE: {roe:.2f} %" if roe else "ROE: Nicht berechenbar")
    print(f"Fremdkapitalquote: {fremdkapitalquote:.2f} %" if fremdkapitalquote else "Fremdkapitalquote: Nicht berechenbar")
    print(f"Eigenkapitalquote: {eigenkapitalquote:.2f} %" if eigenkapitalquote else "Eigenkapitalquote: Nicht berechenbar")
    print(f"Verschuldungsgrad: {verschuldungsgrad:.2f} %" if verschuldungsgrad else "Verschuldungsgrad: Nicht berechenbar")


if __name__ == "__main__":
    # Beispielparameter
    params = {
        "umlaufvermoegen_2021": 3520,
        "anlagevermoegen_2021": 4400,
        "umlaufvermoegen_2020": 3080,
        "anlagevermoegen_2020": 4620,
        "kurzfristiges_fk_2021": 1210,
        "langfristiges_fk_2021": 2310,
        "eigenkapital_2021": 4400,
        "umsatz_2021": 6600,
        "abschreibungen_2021": 550,
        "finanz_ergebnis_2021": 88,
        "steuern_2021": 330,
        "personalaufwand_2021": 2200,
        "cloud_hosting_2021": 550,
        "uebriger_aufwand_2021": 2420,
    }

    calculate_dupont(params)