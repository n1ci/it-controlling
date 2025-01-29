import numpy as np

# Gegebene Daten
months = list(range(1, 13))
production_quantity = [100, 110, 120, 160, 150, 145, 130, 80, 105, 110, 120, 140]
total_cost = [140700, 144700, 146500, 149800, 154600, 150500, 146600, 137700, 141900, 146700, 148100, 147000]

# Gesamte Produktion und Gesamtkosten
total_production = sum(production_quantity)
total_cost_year = sum(total_cost)

# Frage 1: Durchschnittliche Kosten pro Einheit
average_cost_per_unit = total_cost_year / total_production
print(f"Durchschnittliche Kosten pro Einheit: {average_cost_per_unit:.2f} CHF")

# Frage 2: Bestimmung der Parameter der Kostenfunktion (C(x) = Cf + cv * x)
x = np.array(production_quantity)  # Produktionsmengen
y = np.array(total_cost)  # Gesamtkosten
A = np.vstack([x, np.ones(len(x))]).T
cv, cf = np.linalg.lstsq(A, y, rcond=None)[0]  # Lineare Regression
print(f"Fixkosten (Cf): {cf:.2f} CHF")
print(f"Variable Kosten pro Einheit (cv): {cv:.2f} CHF")

# Frage 3: Zielproduktionsmenge für 90% der durchschnittlichen Kosten
target_average_cost = 0.9 * average_cost_per_unit  # Ziel: 90% der aktuellen Durchschnittskosten
target_production = cf / (target_average_cost - cv)  # Formel zur Zielproduktionsmenge
print(f"Zielproduktionsmenge: {int(target_production)} Einheiten/Jahr")

# Frage 4: Reduktion der Fixkosten, um Gesamtkosten um 10% zu senken
target_total_cost = 0.9 * total_cost_year  # Ziel: Gesamtkosten um 10% reduzieren
cf_new = target_total_cost - cv * total_production  # Neue Fixkosten
cf_reduction_percentage = ((cf - cf_new) / cf) * 100  # Prozentuale Reduktion der Fixkosten
print(f"Reduktion der Fixkosten: {cf_reduction_percentage:.2f} %")

# Frage 5: Reduktion der variablen Kosten pro Einheit, um Gesamtkosten um 10% zu senken
cv_new = (target_total_cost - cf) / total_production  # Neue variable Kosten pro Einheit
cv_reduction_per_unit = cv - cv_new  # Differenz zu aktuellen variablen Kosten
print(f"Reduktion der variablen Kosten pro Einheit: {cv_reduction_per_unit:.2f} CHF")