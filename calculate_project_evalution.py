import numpy_financial as npf
import pandas as pd


def calculate_project_evaluation(initial_investment, cash_flows, discount_rate):
    irr = npf.irr([initial_investment] + cash_flows) * 100  # in Prozent (interne Kapitalverzinsung)
    npv = npf.npv(discount_rate, [initial_investment] + cash_flows)  # Nettobarwert
    return irr, npv


def main():
    # Variabel: Projektdaten (Initialinvestment & Cashflows pro Jahr)
    projects = {
        "A": {
            "initial_investment": -220000,  # Variabel: Anfangsinvestition
            "cash_flows": [75000, 65000, 55000, 45000, 35000],  # Variabel: Rückflüsse pro Jahr
        },
        "B": {
            "initial_investment": -250000,  # Variabel: Anfangsinvestition
            "cash_flows": [80000, 70000, 60000, 50000, 40000],  # Variabel: Rückflüsse pro Jahr
        },
    }
    discount_rate = 0.05  # Variabel: Zinssatz

    results = []
    for project, data in projects.items():
        irr, npv = calculate_project_evaluation(data["initial_investment"], data["cash_flows"], discount_rate)
        results.append([project, irr, npv])

    # Entscheidung basierend auf dem NPV
    best_project = max(results, key=lambda x: x[2])[0]

    # Ergebnisse als Tabelle ausgeben
    df = pd.DataFrame(results, columns=["Projekt", "Interne Kapitalverzinsung (IRR) %", "Nettobarwert (NPV) CHF"])
    print(df.to_string(index=False))
    print(f"\nDas wirtschaftlich bessere Projekt ist: Projekt {best_project}")


if __name__ == "__main__":
    main()