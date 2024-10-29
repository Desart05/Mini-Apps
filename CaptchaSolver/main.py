from random import randint
from ranks import ranks_points, ranks_rates


def generate_captcha() -> str:
    signs: list[str] = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
                        't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

    captcha: str = ''
    for sign in range(6):
        captcha += signs[randint(0, len(signs) - 1)]
    return captcha

def set_user_rank(user_points: int) -> str:
    if user_points >= ranks_points['master']:
        return 'master'
    elif user_points >= ranks_points['diamond']:
        return 'diamond'
    elif user_points >= ranks_points['platinum']:
        return 'platinum'
    elif user_points >= ranks_points['gold']:
        return 'gold'
    elif user_points >= ranks_points['silver']:
        return 'silver'
    elif user_points >= ranks_points['bronze']:
        return 'bronze'
    else:
        return 'unranked'

def set_user_rate(user_rank: str) -> float:
    if user_rank == 'master':
        return ranks_rates['master']
    elif user_rank == 'diamond':
        return ranks_rates['diamond']
    elif user_rank == 'platinum':
        return ranks_rates['platinum']
    elif user_rank == 'gold':
        return ranks_rates['gold']
    elif user_rank == 'silver':
        return ranks_rates['silver']
    elif user_rank == 'bronze':
        return ranks_rates['bronze']
    elif user_rank == 'unranked':
        return ranks_rates['unranked']

def CLI() -> None:
    print('================ CAPTCHA SOLVER ================')
    print('[1] Generate Captcha')
    print('[2] Statistics')
    print('[9] Exit')
    print('================ CAPTCHA SOLVER ================')

def HUD(user_points: int, user_cash: float, user_rank: str) -> None:
    print('================ HUD ================')
    print(f'Your rank: {user_rank}')
    print(f'Your points: {user_points}')
    print(f'Your cash: {user_cash}')
    print('================ HUD ================')

def statistics(user_points: int, user_mistakes: int, user_total_captchas: int) -> None:
    try:
        print('================ STATISTICS ================')
        print(f'Correct captchas: {user_points} || {round(user_points / user_total_captchas * 100, 2)}%')
        print(f'Wrong captchas: {user_mistakes} || {round(user_mistakes / user_total_captchas * 100, 2)}%')
        print(f'Total captchas: {user_total_captchas}')
        print('================ STATISTICS ================')
    except ZeroDivisionError:
        print('\n================ STATISTICS ================')
        print(f'Correct captchas: {user_points}')
        print(f'Wrong captchas: {user_mistakes}')
        print(f'Total captchas: {user_total_captchas}')
        print('================ STATISTICS ================\n')

def main():
    user_cash: float = 0.0
    user_points: int = 0     # 1 points = 1 correct captcha
    user_mistakes: int = 0    # 1 mistake = 1 wrong captcha
    user_total_captchas: int = 0   # captchas = total captcha solved by user (points + mistakes)

    try:
        with open('stats.txt', 'r') as file:
            lines = file.readlines()
            user_points = int(lines[0])
            user_mistakes = int(lines[1])
            user_total_captchas = int(lines[2])
            user_cash = float(lines[3])
    except FileNotFoundError:
        with open('stats.txt', 'w') as file:
            file.write(str(f'{user_points}\n'))
            file.write(str(f'{user_mistakes}\n'))
            file.write(str(f'{user_total_captchas}\n'))
            file.write(str(f'{user_cash}\n'))

    while True:
        user_rank: str = set_user_rank(user_points)
        user_rate: float = set_user_rate(user_rank)

        HUD(user_points, user_cash, user_rank)
        CLI()
        try:
            user_choice: int = int(input('Enter your choice: '))
        except ValueError:
            print('Expected numerical value!\n')
            continue

        if user_choice == 1:
            try:
                quantity_captchas: int = int(input('How many captchas do you want to solve?: '))
            except ValueError:
                print('Expected numerical value!\n')
                continue

            if quantity_captchas <= 0 or quantity_captchas > 10:
                print('It is only possible to solve 1 to 10 captchas at a time!\n')
                continue

            for captcha in range(quantity_captchas):
                correct_captcha: str = generate_captcha()
                print(f'CAPTCHA -> {correct_captcha}')
                user_captcha: str = input('Enter captcha: ')

                if user_captcha == correct_captcha:
                    user_points += 1
                    user_total_captchas += 1
                    user_cash += user_rate
                    print('The captcha you entered is correct! You scored 1 point!\n')
                else:
                    user_mistakes += 1
                    user_total_captchas += 1
                    print('The captcha you entered is incorrect!\n')

                with open('stats.txt', 'w') as file:
                    file.write(str(f'{user_points}\n'))
                    file.write(str(f'{user_mistakes}\n'))
                    file.write(str(f'{user_total_captchas}\n'))
                    file.write(str(f'{user_cash}\n'))

        elif user_choice == 2:
            statistics(user_points, user_mistakes, user_total_captchas)
        elif user_choice == 9:
            exit(211)
        else:
            print('Choose one of the options below!\n')


if __name__ == '__main__':
    main()
