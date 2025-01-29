import numpy_financial as npf
import pandas as pd

# Gegeben seien ein Projekt A (Anfangsinvestition CHF 220000, Rückflusse pro Jahr s. unten) und ein Projekt B (Anfangsinvestition CHF 250000, Rückflusse pro Jahr s. unten), beide jeweils mit einer Laufzeit von 5 Jahren. Der Zinssatz beträgt 5%.
#
# Jahr	Rückflüsse (Einzahlungen) CHF Projekt A	Rückflüsse (Einzahlungen) CHF Projekt B
# 1	75000	80000
# 2	65000	70000
# 3	55000	60000
# 4	45000	50000
# 5	35000	40000
# Wert	A	B
# Interne Kapitalverzinsung (IRR auf Englisch) in % (nur Zahl, keine Einheiten!!)	Antwort 1 Frage 2
# 9.12
#  [W: 20%]	Antwort 2 Frage 2
# 7.26
#  [W: 20%]
# Nettobarwert (Net Present Value NPV auf Englisch) in CHF (nur Zahl, keine Einheiten!!)	Antwort 3 Frage 2
# 22341.58
#  [W: 20%]	Antwort 4 Frage 2
# 13988.97
#  [W: 20%]
# Entscheiden Sie sich aufgrund des Kriteriums Nettobarwert (Net Present Value NPV auf Englisch) für das "wirtschaftlich bessere" Projekt!
#
# Antwort 5 Frage 2
# Proj A



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