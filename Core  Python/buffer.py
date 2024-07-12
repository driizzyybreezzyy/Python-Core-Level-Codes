class MaxLimitExceededException(Exception):
    pass

class MaxAmountExceededException(Exception):
    pass

class Bank:
    def __init__(self, max_transactions, max_amount):
        self.max_transactions = max_transactions
        self.max_amount = max_amount

    def withdraw(self, amount):
        if amount > self.max_amount:
            raise MaxAmountExceededException("Amount exceeds the maximum limit holding.")
        if self.max_transactions == 0:
            raise MaxLimitExceededException("Maximum transaction limit exceeded.")

        self.max_transactions -= 1
        self.max_amount -= amount
        print(f"Transaction successful. Remaining transaction count: {self.max_transactions}, Remaining amount: {self.max_amount}")

class HDFCBank(Bank):
    def __init__(self):
        super().__init__(max_transactions=3, max_amount=20000)

class AXISBank(Bank):
    def __init__(self):
        super().__init__(max_transactions=5, max_amount=30000)

def main():
    while True:
        print("Choose a bank: 1 - HDFC Bank, 2 - AXIS Bank")
        choice = int(input())
        bank = None
        max_transactions = 0

        if choice == 1:
            bank = HDFCBank()
            max_transactions = 3
        elif choice == 2:
            bank = AXISBank()
            max_transactions = 5
        else:
            print("Invalid choice. Please choose a valid bank.")
            continue

        transaction_count = 0
        while transaction_count < max_transactions:
            amount = int(input("Enter the amount to withdraw: "))
            try:
                bank.withdraw(amount)
                transaction_count += 1
            except MaxLimitExceededException as e:
                print(e)
                break
            except MaxAmountExceededException as e:
                print(e)

        continue_transaction = input("Do you want to perform transactions for another bank? (yes/no) ")
        if continue_transaction.lower() != "yes":
            print("Thank you for using the ATM.")
            break

if __name__ == "__main__":
    main()
