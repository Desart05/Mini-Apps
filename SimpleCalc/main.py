def addition(x: int, y: int) -> int:
    return x + y

def subtraction(x: int, y: int) -> int:
    return x - y

def multiplication(x: int, y: int) -> int:
    return x * y

def division(x: int, y: int) -> float:
    try:
        return x / y
    except ZeroDivisionError:
        print("Can't divide by zero!")

def value_of_number() -> tuple[int, int]:
    while True:
        try:
            first_number: int = int(input('Enter first number: '))
            second_number: int = int(input('Enter second number: '))
        except ValueError:
            print('\nInvalid value!\nExpected numerical value!\n')
            continue
        return first_number, second_number

def CLI() -> None:
    print('[1] Addition')
    print('[2] Subtraction')
    print('[3] Multiplication')
    print('[4] Division')
    print('[9] Exit')

def main() -> None:
    while True:
        CLI()
        try:
            user_choice: int = int(input('Select option: '))
        except ValueError:
            print('\nInvalid value!\nChoose one of the options below!\n')
            continue
        print()
        if user_choice == 1:
            numbers: tuple[int, int] = value_of_number()
            result: int = addition(numbers[0], numbers[1])
            print(f'Result: {result}\n')
        elif user_choice == 2:
            numbers: tuple[int, int] = value_of_number()
            result: int = subtraction(numbers[0], numbers[1])
            print(f'Result: {result}\n')
        elif user_choice == 3:
            numbers: tuple[int, int] = value_of_number()
            result: int = multiplication(numbers[0], numbers[1])
            print(f'Result: {result}\n')
        elif user_choice == 4:
            numbers: tuple[int, int] = value_of_number()
            result: float = division(numbers[0], numbers[1])
            print(f'Result: {result}\n')
        elif user_choice == 9:
            exit(211)
        else:
            print('Invalid option!\n')


if __name__ == '__main__':
    main()