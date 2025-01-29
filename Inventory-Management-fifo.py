# // Goated
transactions = [
    # this ist init
    {"type": "in", "qty": 40, "price": 12},
    # this ist init
    {"type": "in", "qty": 30, "price": 12},
    {"type": "in", "qty": 50, "price": 13},
    {"type": "out", "qty": 80},
    {"type": "in", "qty": 150, "price": 12},
    {"type": "in", "qty": 40, "price": 13},
    {"type": "out", "qty": 60},
    {"type": "out", "qty": 80},
    {"type": "in", "qty": 20, "price": 14},
]


def calculate_wa():
    stock = []
    total_qty = 0
    total_cost = 0

    for t in transactions:
        if t["type"] == "in":
            total_qty += t["qty"]
            total_cost += t["qty"] * t["price"]
        else:
            if total_qty == 0:
                continue
            avg_price = total_cost / total_qty
            remove_qty = min(t["qty"], total_qty)
            total_cost -= remove_qty * avg_price
            total_qty -= remove_qty

    avg_price = total_cost / total_qty if total_qty != 0 else 0
    return round(total_cost, 2), round(avg_price, 2)


def calculate_ma():
    stock = []
    total_qty = 0
    total_cost = 0
    current_avg = 0

    for t in transactions:
        if t["type"] == "in":
            total_qty += t["qty"]
            total_cost += t["qty"] * t["price"]
            current_avg = total_cost / total_qty
        else:
            if total_qty == 0:
                continue
            remove_qty = min(t["qty"], total_qty)
            total_cost -= remove_qty * current_avg
            total_qty -= remove_qty
            if total_qty > 0:
                current_avg = total_cost / total_qty

    avg_price = current_avg if total_qty != 0 else 0
    return round(total_cost, 2), round(avg_price, 2)


def calculate_fifo():
    stock = []

    for t in transactions:
        if t["type"] == "in":
            stock.append({"qty": t["qty"], "price": t["price"]})
        else:
            remaining = t["qty"]
            while remaining > 0 and stock:
                if stock[0]["qty"] > remaining:
                    stock[0]["qty"] -= remaining
                    remaining = 0
                else:
                    remaining -= stock[0]["qty"]
                    stock.pop(0)

    total_cost = sum(b["qty"] * b["price"] for b in stock)
    avg_price = total_cost / sum(b["qty"] for b in stock) if stock else 0
    return round(total_cost, 2), round(avg_price, 2)


def calculate_lifo():
    stock = []

    for t in transactions:
        if t["type"] == "in":
            stock.append({"qty": t["qty"], "price": t["price"]})
        else:
            remaining = t["qty"]
            while remaining > 0 and stock:
                if stock[-1]["qty"] > remaining:
                    stock[-1]["qty"] -= remaining
                    remaining = 0
                else:
                    remaining -= stock[-1]["qty"]
                    stock.pop()

    total_cost = sum(b["qty"] * b["price"] for b in stock)
    avg_price = total_cost / sum(b["qty"] for b in stock) if stock else 0
    return round(total_cost, 2), round(avg_price, 2)


def calculate_hifo():
    stock = []

    for t in transactions:
        if t["type"] == "in":
            stock.append({"qty": t["qty"], "price": t["price"]})
            stock.sort(key=lambda x: -x["price"])
        else:
            remaining = t["qty"]
            while remaining > 0 and stock:
                if stock[0]["qty"] > remaining:
                    stock[0]["qty"] -= remaining
                    remaining = 0
                else:
                    remaining -= stock[0]["qty"]
                    stock.pop(0)

    total_cost = sum(b["qty"] * b["price"] for b in stock)
    avg_price = total_cost / sum(b["qty"] for b in stock) if stock else 0
    return round(total_cost, 2), round(avg_price, 2)


# Berechnungen
wa = calculate_wa()
ma = calculate_ma()
fifo = calculate_fifo()
lifo = calculate_lifo()
hifo = calculate_hifo()

# Ausgabe der Tabelle
print(f"{'Method -->':<12} | {'WA':<8} | {'MA':<8} | {'FIFO':<8} | {'LIFO':<8} | {'HIFO':<8}")
print("-" * 65)
print(f"{'Closing stock CHF':<12} | {wa[0]:<8} | {ma[0]:<8} | {fifo[0]:<8} | {lifo[0]:<8} | {hifo[0]:<8}")
print(f"{'Average price (@end)':<12} | {wa[1]:<8} | {ma[1]:<8} | {fifo[1]:<8} | {lifo[1]:<8} | {hifo[1]:<8}")


# import pandas as pd
#
#
# def calculate_wa(transactions, end_date=None):
#     total_qty = 0
#     total_cost = 0
#
#     for _, t in transactions.iterrows():
#         if end_date and t["Date"] > end_date:
#             break
#         if t["Type"] in ["IN", "INIT"]:
#             total_qty += t["Q"]
#             total_cost += t["Q"] * t["P"]
#         elif t["Type"] == "OUT":
#             if total_qty == 0:
#                 continue
#             avg_price = total_cost / total_qty
#             remove_qty = min(t["Q"], total_qty)
#             total_cost -= remove_qty * avg_price
#             total_qty -= remove_qty
#
#     avg_price = total_cost / total_qty if total_qty != 0 else 0
#     return round(total_cost, 2), round(avg_price, 2), total_qty
#
#
# def calculate_fifo(transactions, end_date=None):
#     stock = []
#     fifo_abgang_17_2 = 0
#     fifo_done = False
#
#     for i, t in transactions.iterrows():
#         if end_date and t["Date"] > end_date:
#             break
#         if t["Type"] in ["IN", "INIT"]:
#             stock.append({"qty": t["Q"], "price": t["P"]})
#         elif t["Type"] == "OUT":
#             remaining = t["Q"]
#             while remaining > 0 and stock:
#                 if stock[0]["qty"] > remaining:
#                     if not fifo_done and t["Date"] == "17.2.":
#                         fifo_abgang_17_2 += remaining * stock[0]["price"]
#                     stock[0]["qty"] -= remaining
#                     remaining = 0
#                 else:
#                     if not fifo_done and t["Date"] == "17.2.":
#                         fifo_abgang_17_2 += stock[0]["qty"] * stock[0]["price"]
#                     remaining -= stock[0]["qty"]
#                     stock.pop(0)
#             if t["Date"] == "17.2.":
#                 fifo_done = True
#
#     total_cost = sum(b["qty"] * b["price"] for b in stock)
#     avg_price = total_cost / sum(b["qty"] for b in stock) if stock else 0
#     return round(total_cost, 2), round(avg_price, 2), sum(b["qty"] for b in stock), round(fifo_abgang_17_2, 2)
#
#
# def calculate_ma(transactions, end_date=None):
#     total_qty = 0
#     total_cost = 0
#     current_avg = 0
#     ma_abgang_11_3 = 0
#
#     for i, t in transactions.iterrows():
#         if end_date and t["Date"] > end_date:
#             break
#         if t["Type"] in ["IN", "INIT"]:
#             total_qty += t["Q"]
#             total_cost += t["Q"] * t["P"]
#             current_avg = total_cost / total_qty
#         elif t["Type"] == "OUT":
#             if total_qty == 0:
#                 continue
#             remove_qty = min(t["Q"], total_qty)
#             if t["Date"] == "11.3.":
#                 ma_abgang_11_3 += remove_qty * current_avg
#             total_cost -= remove_qty * current_avg
#             total_qty -= remove_qty
#             if total_qty > 0:
#                 current_avg = total_cost / total_qty
#
#     avg_price = current_avg if total_qty != 0 else 0
#     return round(total_cost, 2), round(avg_price, 2), total_qty, round(ma_abgang_11_3, 2)
#
#
# # Beispiel-Aufruf mit Datum
# transactions = pd.DataFrame([
#     {"Date": "1.1.", "Type": "INIT", "Q": 40, "P": 12},
#     {"Date": "21.1.", "Type": "IN", "Q": 30, "P": 12},
#     {"Date": "15.2.", "Type": "IN", "Q": 50, "P": 13},
#     {"Date": "17.2.", "Type": "OUT", "Q": 80, "P": None},
#     {"Date": "27.2.", "Type": "IN", "Q": 150, "P": 12},
#     {"Date": "10.3.", "Type": "IN", "Q": 40, "P": 13},
#     {"Date": "11.3.", "Type": "OUT", "Q": 60, "P": None},
#     {"Date": "28.3.", "Type": "OUT", "Q": 80, "P": None},
#     {"Date": "29.3.", "Type": "IN", "Q": 20, "P": 14},
#     {"Date": "31.3.", "Type": "FINAL", "Q": None, "P": None},
# ])
#
# # Datum festlegen
# end_date = "31.3."
#
# # Berechnungen
# wa = calculate_wa(transactions, end_date)
# fifo = calculate_fifo(transactions, end_date)
# ma = calculate_ma(transactions, end_date)
#
# # Ergebnisse ausgeben
# print(f"Ergebnisse bis {end_date}:")
# print(f"Gewogener Durchschnitt (WA): Bestand = {wa[2]} Stück, Wert = {wa[0]} CHF, Preis = {wa[1]} CHF")
# print(f"FIFO: Bestand = {fifo[2]} Stück, Wert = {fifo[0]} CHF, Preis = {fifo[1]} CHF")
# print(f"MA: Bestand = {ma[2]} Stück, Wert = {ma[0]} CHF, Preis = {ma[1]} CHF")
