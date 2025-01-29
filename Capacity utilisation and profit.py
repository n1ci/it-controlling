import numpy as np
import pandas as pd


def calculate_tariffs(primary_costs, services):
    """
    Berechnet die Tarife (Verrechnungspreise) pro Kostenstelle.

    :param primary_costs: Liste der Primärkosten pro Kostenstelle (in CHF)
    :param services: Matrix der bezogenen Leistungen zwischen Kostenstellen (in Stunden)
    :return: Liste der berechneten Tarife pro Kostenstelle (in CHF/h)
    """
    num_cost_centers = len(primary_costs)

    # Erstellen der Koeffizientenmatrix und der rechten Seite des Gleichungssystems
    A = np.zeros((num_cost_centers, num_cost_centers))
    b = np.array(primary_costs, dtype=float)

    for i in range(num_cost_centers):
        A[i, i] = 1
        for j in range(num_cost_centers):
            A[i, j] -= services[j][i]  # Abzug der bezogenen Leistungen (transpose beachten)

    # Lösen des Gleichungssystems für die Tarife
    tariffs = np.linalg.solve(A, b)
    return tariffs


def main():
    # Eingabe der Primärkosten pro Kostenstelle
    primary_costs = [10680, 4080, 1880, 92000, 101240, 81800, 19920]  # CHF pro Kostenstelle

    # Eingabe der Leistungsbeziehungen (Matrix der Stunden zwischen Kostenstellen)
    services = [
        [0, 0, 10, 20, 30, 40, 80],  # Leistungen von A
        [0, 0, 0, 10, 20, 0, 100],  # Leistungen von B
        [0, 0, 0, 50, 40, 0, 40],  # Leistungen von C
        [0, 0, 0, 0, 30, 0, 50],  # Leistungen von D
        [0, 0, 0, 0, 0, 20, 0],  # Leistungen von E
        [0, 0, 0, 0, 0, 0, 0],  # Leistungen von F
        [0, 0, 0, 0, 20, 0, 0],  # Leistungen von G
    ]

    # Kostenträger-Leistungen
    cost_driver = {"A": 30, "D": 300, "E": 200, "F": 80, "G": 180}

    # Berechnung der Tarife
    tariffs = calculate_tariffs(primary_costs, services)

    # Ergebnisse tabellarisch darstellen
    cost_centers = ["A", "B", "C", "D", "E", "F", "G"]
    df = pd.DataFrame(services, columns=cost_centers, index=cost_centers)
    df["Primärkosten (CHF)"] = primary_costs
    df["Tarif (CHF/h)"] = tariffs

    # Kostenträger hinzufügen
    df.loc["Kostenträger"] = [
                                 cost_driver.get(center, 0) for center in cost_centers
                             ] + [0, 0]  # Kostenträger hat keine eigenen Primärkosten oder Tarife

    # Ausgabe der Tabelle
    pd.options.display.float_format = "{:.2f}".format
    print("Tariftabelle:")
    print(df.to_string())


if __name__ == "__main__":
    main()