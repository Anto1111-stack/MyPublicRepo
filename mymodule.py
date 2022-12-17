import sys, time
from collections import OrderedDict

def make_it_flash(text):
    
    for i in reversed(range(2)):
        sys.stdout.write('\r')
        sys.stdout.write(text if i % 2 else ' '*len(text))
        sys.stdout.flush()
        time.sleep(1)
    
def slowprint(s):
	for c in s + '\n':
		sys.stdout.write(c)
		sys.stdout.flush()
		time.sleep(1./14) # controlinng the speed

def hello_operator():
    """Slowprint function with hello statement and explanation of the game's rules."""
    time.sleep(1)
    slowprint("Hello Operator!\n\nThis is a game of picking.\n\nRules of the game are simple:")


    slowprint("The product code will flash and you will have to input the right code in order to proceed.")
    print() #empty space

    slowprint("Ready?\n\nLet's start!")

    slowprint("Location 1 - Look for the product code:\n\n")

# MAIN FUNCTION OF THE GAME
def product_pick():
    """This function is dealing with main opearations in the game."""
    make_it_flash(corridor1['Lucozade Orange']) # accessing dict value
    print()
    time.sleep(1.5)

    code = input("Enter the product key: ")
    for value in corridor1:
        if code == corridor1[value]:

            slowprint("Product picked.\n") 
            time.sleep(2)
            slowprint("Go to next location.\n\nProduct will flash.")
            time.sleep(2)

        make_it_flash(corridor1['Lucozade Strawbery'])
        print()
        code = input("Enter the product key: ")

        time.sleep(1.5)

        if code == corridor1['Lucozade Strawbery']:
            slowprint("Product picked.\n") 
            time.sleep(2)
            slowprint("Go to next location.")
            time.sleep(2)

        else:
            slowprint("Incorrect code!\n\nGame Over!")
            break

# main dict

corridor1 = OrderedDict({'Lucozade Orange': '34780',
                         'Lucozade Strawbery': '26648',
                         'Lucozade Zero': '12755',
                         'Lucozade Sport': '24654',
                         'Lucozade Alert': '33870',
                         'Lucozade Tropical': '25217',
                         'Lucozade Citrus': '44629'
                         })

# corridor1 = {
#     'Lucozade Orange': '34780',
       
#     'Lucozade Strawbery': '26648',
  
#     'Lucozade Zero': '12755',

#     'Lucozade Sport': '24654',

#     'Lucozade Alert': '33870',

#     'Lucozade Tropical': '25217',

#     'Lucozade Citrus': '44629'
# }

       

