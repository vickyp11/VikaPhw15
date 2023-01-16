import json

file = 'phonebook.json'
phonebook = {}
phonebook_list = []

try:
    with open(file) as file:
        phonebook_list = json.load(file)
except ValueError:
    phonebook_list = []


def add_customer() -> list:
    phonebook['name']: str = input('Please specify the name: ').lower()
    phonebook['surname']: str = input('Please type in the surname: ').lower()
    phonebook['city']: str = input('Please insert city: ').lower()
    phonebook['number']: str = input('What\'s the phone number? ').lower()
    phonebook_list.append(phonebook)

    with open('phonebook.json', 'w') as file:
        json.dump(phonebook_list, file, indent=4)


def search_customer() -> list:
    search_name: str = input('What you\'re looking for? ').lower()
    for i in phonebook_list:
        full_name: str = i['name'] + ' ' + i['surname']
        if i['name'] == search_name or i['surname'] == search_name or i['city'] == search_name or i['number'] == search_name or full_name == search_name:
            print(i)
    else:
        print('No customer found, please double-check!')


def delete_customer() -> list:
    search_delete: str = input('Please insert phone number you wanna delete? ')
    for n, d in enumerate(phonebook_list):
        if d['number'] == search_delete:
            confirm: str = input(f'Please confirm you want to delete the following contact card: {d}.'
                  f'To confirm, press Y. If you don\'t want to remove the record, press N: ').lower()
            print(confirm)
            if confirm == 'y':
                phonebook_list.pop(n)
                print('Contact deleted!')
                break
            elif confirm == 'n':
                print('No worries! Nothing was deleted')
                break
            else:
                print('You didn\'t fill in a correct letter')
                break
    else:
        print('Nothing found upon your request')

    with open('phonebook.json', 'w') as file:
        json.dump(phonebook_list, file, indent=4)


def update_customer() -> list:
    search_update: str = input('Please specify a phone number you would like to update: ')
    for u in phonebook_list:
        if u['number'] == search_update:
            upd_action: str = input('What you would like to update? '
                               'Just type name/surname/city/phone number: ').lower()
            if upd_action == 'name':
                u['name']: str = input('Updated name should be: ').lower()
                print('Contact was updated! Yay!')
                break
            elif upd_action == 'surname':
                u['surname']: str = input('Updated surname should be: ').lower()
                print('Contact was updated! Yay!')
                break
            elif upd_action == 'city':
                u['city']: str = input('Updated city should be: ').lower()
                print('Contact was updated! Yay!')
                break
            elif upd_action == 'phone number':
                u['number']: str = input('Updated phone number should be: ').lower()
                print('Contact was updated! Yay!')
                break
            else:
                print('You have typed in something wrong')
                break
    else:
        print('Such contact doesn\'t exist')

    with open('phonebook.json', 'w') as file:
        json.dump(phonebook_list, file, indent=4)


welcome_inp: str = input('Welcome to the Phonebook!'
                        'Please specify the action you would like to perform:\n'
                        'A - to add a new contact\n'
                        'S - to seach for an existing contact\n'
                        'D - to delete a contact\n'
                        'U - to update a conatact\n'
                        'Q - to quit the program\n').lower()


if welcome_inp == 'a':
    add_customer()
elif welcome_inp == 's':
    search_customer()
elif welcome_inp == 'd':
    delete_customer()
elif welcome_inp == 'u':
    update_customer()
elif welcome_inp == 'q':
    print('Thanks! Bye!')
