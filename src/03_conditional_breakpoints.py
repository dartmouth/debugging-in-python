"""
Learning objectives
- Use conditional breakpoints to stop only when a certain condition is met.
- Monitor complex expressions and variables with the Watch panel.
"""

transactions = [
    {"id": 1, "amount": 120},
    {"id": 2, "amount": -50},
    {"id": 3, "amount": -30},
    {"id": 4, "amount": 200},
    {"id": 5, "amount": -500},
    {"id": 6, "amount": 200},
]


def process(transactions, starting_balance=100):
    balance = starting_balance

    for t in transactions:
        amount = t["amount"]

        balance += amount

        flag = "OVERDRAWN" if balance < 0 else "OK"

    return balance, flag


if __name__ == "__main__":
    ending_balance, flag = process(transactions)
    print("Ending balance:", ending_balance)
    print("Flag:", flag)
