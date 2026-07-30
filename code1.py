# Sample data: list of transactions
transactions = [
    {"account_number": "ACC101", "type": "Deposit", "amount": 5000},
    {"account_number": "ACC102", "type": "Deposit", "amount": 12000},
    {"account_number": "ACC101", "type": "Withdrawal", "amount": 2000},
    {"account_number": "ACC103", "type": "Deposit", "amount": 15000},
    {"account_number": "ACC102", "type": "Withdrawal", "amount": 10500},  # Suspicious
    {"account_number": "ACC101", "type": "Deposit", "amount": 8000},
]

# Initialize variables
total_deposits = 0
total_withdrawals = 0
balances = {}
suspicious_withdrawals = []

# Process transactions
for tx in transactions:
    acc = tx["account_number"]
    tx_type = tx["type"]
    amount = tx["amount"]
    
    # Initialize account balance if not already present
    if acc not in balances:
        balances[acc] = 0
        
    if tx_type == "Deposit":
        total_deposits += amount
        balances[acc] += amount
    elif tx_type == "Withdrawal":
        total_withdrawals += amount
        balances[acc] -= amount
        # Flag suspicious withdrawals
        if amount > 10000:
            suspicious_withdrawals.append((acc, amount))

# Find the account with the highest final balance
highest_balance_account = max(balances, key=balances.get)

# Display Results
print("--- BANK TRANSACTION REPORT ---")
print(f"Total Deposits: ${total_deposits:,}")
print(f"Total Withdrawals: ${total_withdrawals:,}")
print(f"Highest Balance Account: {highest_balance_account} (${balances[highest_balance_account]:,})")

print("\nSuspicious Withdrawals (> $10,000):")
if suspicious_withdrawals:
    for acc, amount in suspicious_withdrawals:
        print(f"  - Account: {acc}, Amount: ${amount:,}")
else:
    print("  - None")

print("\nFinal Balances:")
for acc, bal in balances.items():
    print(f"  - Account {acc}: ${bal:,}")
