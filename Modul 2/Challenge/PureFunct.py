def calculate_total_stock(items):
    total_stock = 0
    for item in items:
        total_stock += item['stock']
    return total_stock

def add_stock(items, item_name, quantity):
    updated_items = items.copy()

    for item in updated_items:
        if item['name'] == item_name:
            item['stock'] += quantity
            print(f"Stok {item_name} ditambahkan sebanyak {quantity}. Stok saat ini: {item['stock']}")
            break
    else:
        print(f"Barang {item_name} tidak ditemukan dalam daftar.")

    return updated_items

items = [
    {'name': 'Pensil', 'stock': 100},
    {'name': 'Buku', 'stock': 50},
]

updated_items = add_stock(items, 'Pensil', 50)

total_stock = calculate_total_stock(updated_items)
print(f"Total stok barang terbaru: {total_stock}")