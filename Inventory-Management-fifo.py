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