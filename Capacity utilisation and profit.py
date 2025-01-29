# Gegebene Werte
cost_90_percent = 370000  # Kosten bei 90% Kapazitätsauslastung
cost_50_percent = 250000  # Kosten bei 50% Kapazitätsauslastung
capacity_100_percent = 20000  # Maximale Stückzahl bei 100% Kapazität
sales_price_per_unit = 22.50  # Verkaufspreis pro Einheit

# Berechnungen der fixen (Cf) und variablen (cv) Kosten
x_90 = 0.9 * capacity_100_percent  # Auslastung bei 90%
x_50 = 0.5 * capacity_100_percent  # Auslastung bei 50%

# Gleichungen:
# C(90%) = Cf + cv * x_90
# C(50%) = Cf + cv * x_50
# cv = (C(90%) - C(50%)) / (x_90 - x_50)
cv = (cost_90_percent - cost_50_percent) / (x_90 - x_50)

# Cf = C(90%) - cv * x_90
cf = cost_90_percent - cv * x_90

# Profit bei 100% Kapazität
total_cost_100_percent = cf + cv * capacity_100_percent
total_revenue_100_percent = sales_price_per_unit * capacity_100_percent
profit_100_percent = total_revenue_100_percent - total_cost_100_percent

# Ergebnisse
print("Cf (Fixkosten):", int(cf))
print("cv (Variable Kosten pro Stück):", round(cv, 2))
print("Profit bei 100% Kapazitätsauslastung:", int(profit_100_percent))


