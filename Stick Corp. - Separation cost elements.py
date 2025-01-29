def calculate_costs():
    # Gegebene Werte
    max_output = 5000  # Maximale Kapazität (Einheiten pro Tag)
    direct_costs = 20000  # Direkte Kosten bei voller Kapazität
    fixed_costs = 16000  # Fixkosten pro Tag
    variable_costs_per_unit = 6  # Variable Kosten pro Einheit

    # 1. Gesamtkosten bei voller Kapazität
    total_variable_costs = variable_costs_per_unit * max_output  # Variable Gesamtkosten
    total_costs_full_capacity = fixed_costs + total_variable_costs

    # 2. Variable Gemeinkosten bei voller Kapazität
    variable_overhead_costs = total_variable_costs - direct_costs

    # 3. Gesamtkosten pro Einheit bei voller Kapazität
    total_cost_per_unit_full_capacity = total_costs_full_capacity / max_output

    # 4. Gesamtkosten pro Einheit bei 80% Kapazität
    output_80_percent = 0.8 * max_output  # Output bei 80% Kapazität
    total_variable_costs_80 = variable_costs_per_unit * output_80_percent
    total_costs_80_percent = fixed_costs + total_variable_costs_80
    total_cost_per_unit_80_percent = total_costs_80_percent / output_80_percent

    # Ergebnisse
    print(f"Gesamtkosten bei voller Kapazität: {total_costs_full_capacity} USD")
    print(f"Variable Gemeinkosten bei voller Kapazität: {variable_overhead_costs} USD")
    print(f"Gesamtkosten pro Einheit bei voller Kapazität: {total_cost_per_unit_full_capacity:.2f} USD")
    print(f"Gesamtkosten pro Einheit bei 80% Kapazität: {total_cost_per_unit_80_percent:.2f} USD")

# Skript ausführen
calculate_costs()