# GLOBAL VARIABLES BELOW
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.50,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.50,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.00,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


# FUNCTIONS BELOW
def coffee_art():
    print('''
         )))
        (((
      +-----+
      |     |] - WELCOME TO THE COFFEE MACHINE!
      `-----' 
      
      ------ MENU ------ 
      Espresso ($1.50)
      Latte ($2.50)
      Cappuccino ($3.00)
      ------------------
      
      PS: Type "report" at any moment
      to check our resources available.
    ''')


def show_report():
    pass

# MAIN CODE BELOW
while True:
    coffee_art()
    while True:
        user_choice = str(input('What would you like? (espresso/latte/cappuccino): ')).strip().lower()
        if user_choice == "off":
            print('\033[31m<<THE END>>\033[m')
            exit()
        elif user_choice == "report":
            show_report()
        elif user_choice not in MENU:
            print('\033[31mError. Please choose an available option.\033[m')
        else:
            print(f'You chose "{user_choice}" and it costs ${MENU[user_choice]["cost"]:.2f}')
            break
    print('You have reached here.')
    break