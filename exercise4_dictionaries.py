inventory = {
    "Laptop": 15,
    "Phone": 8,
    "Headphones": 25,
    "Charger": 5,
    "Keyboard": 12
}
print("Initial inventory:", inventory)

inventory["Mouse"] = 20
inventory["Phone"] = 10
print("\nUpdated inventory:", inventory)

def low_stock_items(inv):
    return {k: v for k, v in inv.items() if v < 10}

print("\nLow-stock products:", low_stock_items(inventory))

del inventory["Charger"]
print("\nAfter deleting 'Charger':", inventory)

print("\nProduct list:")
for product, qty in inventory.items():
    print(product, "→", qty)
