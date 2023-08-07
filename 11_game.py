import random

def choose_option():

    options = ('piedra', 'papel', 'tijera')
    user_option = input('Piedra, papel o tijera: ').lower()
    computer_option = random.choice(options)

    if not user_option in options:
        print('No se seleccionó ninguna opción')
        #continue
        return None, None
    
    print('\nOpcion de usuario:', user_option)
    print('Opcion de la computadora:', computer_option + "\n")
    return user_option, computer_option

def check_rules(user_option, computer_option, user, computer):
    if user_option == computer_option:
        print('Empate!')
    elif user_option == 'piedra':
        if computer_option == 'tijera':
            print('Piedra gana a tijera')
            print('El usuario gano!')
            user += 1
        else:
            print('Papel gana a piedra')
            print('La computadora gana!')
            computer += 1
    elif user_option == 'papel':
        if computer_option == 'piedra':
            print('Papel gana a piedra')
            print('El usuario gano!')
            user += 1
        else:
            print('Tijera gana a papel')
            print('La computadora gana!')
            computer += 1
    elif user_option == 'tijera':
        if computer_option == 'papel':
            print('Tijera gana a papel')
            print('El usuario gano!')
            user += 1
        else:
            print('Piedra gana a tijera')
            print('La computadora gano!')
            computer += 1
    return user, computer

def check_wins(user, computer):
    if user == 3:
        print("El usuario gano el juego!")
        return user
    elif computer == 3:
        print("La computadora gano el juego!")
        return computer

def run_game():
    user = 0
    computer = 0
    rounds = 1
    
    while True:

        print('*' *10)
        print('ROUND', rounds)
        print('*' *10)

        user_option, computer_option = choose_option()
        user, computer = check_rules(user_option, computer_option, user, computer)
        if check_wins(user, computer) == 3: break

        print('\nVictorias usuario', user)
        print('Victorias computadora\n', computer)

        rounds += 1

run_game()