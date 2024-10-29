from random import randint

def roll_dice() -> int:
    return randint(1, 6)


def print_statistics(user_win: int, ai_win: int, draw: int) -> None:
    print('\n================= YOUR STATISTICS =================')
    print(f'You win: {user_win}')
    print(f'AI win: {ai_win}')
    print(f'Draw: {draw}')
    print('================= YOUR STATISTICS =================\n')

def CLI() -> None:
    print('================= DICE SIMULATOR =================')
    print('[1] Play')
    print('[2] Check your session statistics')
    print('[3] Exit')
    print('================= DICE SIMULATOR =================')

def main():
    user_win: int = 0
    ai_win: int = 0
    draw: int = 0

    while True:
        CLI()
        try:
            user_choice: int = int(input('Enter your choice: '))
        except ValueError:
            print('Expected a numerically value!')
            continue

        if user_choice == 1:
            user_first_dice: int = roll_dice()
            user_second_dice: int = roll_dice()
            user_points: int = user_first_dice + user_second_dice
            print(f'You rolled: {user_first_dice} and {user_second_dice} == {user_points} points!\n')

            ai_first_dice: int = roll_dice()
            ai_second_dice: int = roll_dice()
            ai_points: int = ai_first_dice + ai_second_dice
            print(f'AI rolled: {ai_first_dice} and {ai_second_dice} == {ai_points} points!\n')

            if user_points > ai_points:
                print('You won! Congratulations!\n')
                user_win += 1
            elif user_points < ai_points:
                print('AI won! Better luck next time!\n')
                ai_win += 1
            else:
                print('It\'s a draw!\n')
                draw += 1

        elif user_choice == 2:
            print_statistics(user_win, ai_win, draw)
        elif user_choice == 3:
            exit(211)
        else:
            print('Choose one of the options below!')

if __name__ == '__main__':
    main()
