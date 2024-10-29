def deposit_money(money: float, user_balance: float) -> float:
    if money <= 0:
        print('Expected positive value!\n')
    else:
        user_balance += money
        print(f'{money} PLN has been successfully deposited!\n')
        return user_balance

def withdraw_money(money: float, user_balance: float) -> float:
    user_balance -= money
    print(f'{money} PLN has been successfully paid!\n')
    return user_balance

def check_history_transactions(history_transactions: list) -> None:
    print('\n================= HISTORY TRANSACTIONS =================')
    if not history_transactions:
        print('No transactions yet!')
    else:
        for index, transaction in enumerate(history_transactions, 1):
            print(f'[{index}] {transaction}')
    print('================= HISTORY TRANSACTIONS =================\n')

def check_balance(user_balance: float) -> None:
    print('\n==================================')
    print(f'Your balance: {user_balance} PLN')
    print('==================================\n')

def amount_of_money() -> float:
    while True:
        try:
            money: float = round(float(input('Enter the amount of money: ')), 2)
        except ValueError:
            print('Expected numerical value!\n')
            continue

        if money <= 0:
            print('Expected positive value!\n')
            continue
        else:
            return money

def CLI() -> None:
    print('================= BANK ACCOUNT SIMULATOR =================')
    print('[1] Deposit')
    print('[2] Withdraw')
    print('[3] Check Balance')
    print('[4] History Transactions')
    print('[9] Exit')
    print('================= BANK ACCOUNT SIMULATOR =================')


def main():
    user_balance: float = 0
    history_transactions: list = []

    while True:
        CLI()
        try:
            user_choice: int = int(input('Enter your choice: '))
        except ValueError:
            print('\nExpected numerical value!')
            print('Try again...')
            continue

        if user_choice == 1:
            money: float = amount_of_money()
            user_balance = deposit_money(money, user_balance)
            history_transactions.append(f'DEPOSIT: {money} PLN')
        elif user_choice == 2:
            money: float = amount_of_money()
            if money > user_balance:
                print('Insufficient funds!\n')
                continue
            else:
                user_balance = withdraw_money(money, user_balance)
                history_transactions.append(f'WITHDRAW: {money} PLN')
        elif user_choice == 3:
            check_balance(user_balance)
        elif user_choice == 4:
            check_history_transactions(history_transactions)
        elif user_choice == 9:
            exit(211)
        else:
            print('Please choose one of the options below!')

if __name__ == '__main__':
    main()
