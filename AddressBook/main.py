def add_contact(address_book: dict[str, int], name: str, phone: int) -> None:
    address_book[name] = phone

def remove_contact(address_book: dict[str, int], name: str) -> None:
    del address_book[name]

def display_contacts(address_book: dict[str, int]) -> None:
    print('=================== Display Contacts ===================')
    if not address_book:
        print('No contacts in the address book.')

    for index, (name, phone) in enumerate(address_book.items(), start=1):
        print(f'[{index}] {name} : {phone}')
    print('=================== Display Contacts ===================')

def search_contact(address_book: dict[str, int], name: str) -> int:
    if name in address_book:
        return address_book[name]

def is_contact_valid(address_book: dict[str, int], name: str) -> bool:
    return name in address_book

def add_name() -> str:
    while True:
        name: str = input('Enter contact name: ')
        if 3 < len(name) < 13:
            return name
        else:
            print('The name must be between 4 and 12 characters long!\n')

def add_phone_number() -> int:
    while True:
        try:
            phone_number: int = int(input('Enter phone number: '))
        except ValueError:
            print('\nInvalid value!\n Expected numerical value!\n')
            continue
        return phone_number


def CLI() -> None:
    print('[1] - Add Contact')
    print('[2] - Remove Contact')
    print('[3] - Display Contacts')
    print('[4] - Search Contact')
    print('[9] - Exit')

def main():
    contacts: dict[str, int] = {}

    while True:
        CLI()
        try:
            user_choice: int = int(input('Select option: '))
            print()
        except ValueError:
            print('\nInvalid value!\n Expected numerical value!\n')
            continue

        if user_choice == 1:
            name = add_name()
            if is_contact_valid(contacts, name):
                print(f'Contact "{name}" already exists!\n')
                continue
            phone_number = add_phone_number()

            add_contact(contacts, name, phone_number)
            print('The contact has been added!\n')


        elif user_choice == 2:
            name: str = input('Enter contact name: ')

            if is_contact_valid(contacts, name):
                remove_contact(contacts, name)
                print('The contact has been deleted!\n')
            else:
                print('The contact does not exist!\n')
        elif user_choice == 3:
            display_contacts(contacts)
        elif user_choice == 4:
            name: str = input('Enter contact name: ')
            if search_contact(contacts, name):
                print(f'Found contact:: {name} : {contacts[name]}\n7')
            else:
                print('The provided contact was not found!\n')
        elif user_choice == 9:
            exit(211)



if __name__ == '__main__':
    main()

