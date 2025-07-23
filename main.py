import json

# Load transaction data from JSON
with open("transactions.json", "r", encoding="utf-8") as f:
    transactions = json.load(f)

# Example: Print basic info for each transaction
for tx in transactions:
    print(f"{tx['date']} | {tx['name']} | ${tx['amount']} | {', '.join(tx.get('category', ['Uncategorized']))}")