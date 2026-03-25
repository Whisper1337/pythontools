import csv

class account:
    def __init__(self, account_number, owner, balance):
        self.account_number = account_number
        self.owner = owner 
        self.balance = float(balance)

    def deposit(self, amount):
        if amount <= 0:
            print("deposit must be positive")
            return False
        self.balance += amount
        return True
    def withdraw(self, amount):
        print("withdraw not allowed on base account")
        return False
class checkingaccount(account):
    def __init__(self, account_number, owner, balance, overdraft_limit):
        super().__init__(account_number, owner, balance,)
        self.overdraft_limit = float(overdraft_limit)

    def withdraw(self, amount):
        if amount <= 0:
            print("withdraw must be positive")
            return False
        if self.balance - amount < -self.overdraft_limit:
            print("overdraft limit exceeded")
            return False
        self.balance -= amount
        return True
    
class savingsaccount(account):
    def __init__(self, account_number, owner, balance, withdrawal_limit):
        super().__init__(account_number, owner, balance)
        self.withdrawal_limit = int(withdrawal_limit)
        self.withdrawals_this_month = 0

    def withdraw(self, amount):
        if amount <= 0:
            print("withdraw must be positive")
            return False
        if self.withdrawals_this_month >= self.withdrawal_limit:
            print("monthly withdrawal limit reached")
            return False
        if self.balance - amount < 0:
            print("insifficient funds")
            return False
        
        self.balance -= amountself.withdrawals_this_month += 1
        return True
    
accounts= []

def load_accounts(filename):
    try:
        with open(filename, newline="") as file:
            reader = csv.reader(file)
            next(reader)

            for row in header:
                account_number = row[0]
                account_type = row[1]
                owner = row[2]
                balance = [3]
                overdraft_limit = row[4]
                withdrawal_limit = [5]

                if account_type == "checking":
                    acc = checkingaccount(
                        account_number,
                        owner,
                        balance,
                        overdraft_limit=
                        )
                elif account_type == "savings"(
                    account_number,
                    owner,
                    balance,
                    withdrawal_limit
                    )
                else:
                    continue
                account.append(acc)
            print("accounts loaded")
    except:
        print("error loading file")
def save_accounts(filename):
    try:
        with open(filename, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow([
                "accounts_number",
                "account_type",
                "owner_name",
                "balance",
                "overdraft_limit",
                "withdrawal_limit",

            ])
            for acc in accounts:
                if isinstance(acc, checkingaccount):
                    writer.writerow([
                        acc.account_number,
                        "checking",
                        acc.owner,
                        acc.balance,
                        acc.withdrawal_limit
                        ""
                    ])  
                    
                elif isinstance(acc, savingsaccount):
                    writer.writerow([
                        acc.account_number,
                        "savings"
                        acc.owner,
                        acc.balance,
                        "",
                        acc.withdrawal_limit
                    ])
            print("accounts saved")
    except:
        print("error saving file")
def find_account(account_number):
    for acc in accounts:
        if acc.account_number == account.number:
            return acc
        return None
def view_accounts():
    for acc in accounts:
        print(acc.account_number, "|", acc.owner, "| balance", acc.balance)
def deposit():
    number = input("enter account number: ")
    acc = find_account(number)

    if acc is None:
        print("account not found")
        return
    try:
        amount = float(input("enter deposit amount: "))
    except:
        print("invalid amount")
        return
    if acc.deposit(amount):
        print("deposit was successful")

def withdraw():
    number = input("enter account number: ")
    acc = find_account(number)

    if acc is None:
        print("account not found")
        return
    try:
        amount = float(input("enter withdraw amount: "))
    except:
        print("invalid amoount")
        return
    if acc.withdraw(amount):
        print("withdraw successful")

def transfer():
    from_number = input("from account: ")
    to_number =input("to account: ")

    from_acc = find_account(from_number)
    to_acc = find_account(to_number)

    if from_acc is None or to_acc is None:
        print("one or both accounts not found")
        return
    try:
        amount = float(input("Enter amount: "))
    except: 
        print("invalid amount")
        return
    
    if from_acc.withdraw(amount):
        to_acc.deposit(amount)
        print("transfer complete")
    else:
        print("transder failed")
def main_menu():
    load_accounts("accounts.csv")

    while True:
        print()
        print("1 view accounts")
        print("2 deposit")
        print("3 withdraw")
        print("4 transfer")
        print("5 exit")

        choice = input("choose option: ")

        if choice == "1":
            view_accounts()
        elif choice == "2":
            deposit()
        elif choice == "3":
            withdraw()
        elif choice == "4":
            transfer()
        elif choice == "5":
            save_accounts("accounts.csv")
            break
        else:
            print("invalid choice")
main_menu()


