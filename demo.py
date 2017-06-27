#using impoet keyword for access files from another file
from wwww import spy, friends
from steganography.steganography import Steganography
from datetime import datetime

s_mess = ['My name is Bond, rahul', '.', 'Keeping the British end up, Sir']
#display a message on screen
print "Hello!please start"


qst = "Do you want to continue as " + spy['salutation'] + " " + spy['name'] + " (Y/N)? "
existing = raw_input(qst)

#decleration of add status function
def add_status(curstat):

    updated_status_message = None

#if condition implementation
    if curstat != None:
        print 'Your current status message is %s \n' % (curstat)
    else:
        print 'don\'t have any status message currently \n'

#raw_input fuction is used for taking input from user
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status= raw_input("What status message do you want to set? ")

#len() is used which is used to return the length of string
        if len(new_status) > 0:
            s_mess.append(new_status)
            updated_status_message = new_status

    elif default.upper() == 'Y':
#count is used  to set counter
        count_item = 1
#implementation of for loop
        for message in s_mess:
            print '%d. %s' % (count_item, message)
            count_item = count_item + 1

        message_selection = int(raw_input("\nChoose from the above messages "))


        if len(s_mess) >= message_selection:
            updated_status_message = s_mess[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if curstat:
        print 'Your updated status message is: %s' % (curstat)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

#decleration of add_friend function and creation of a dictionary
def add_friend():
    n_friend = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'chats': []
    }
    #accessing dictionary values
    n_friend['name'] = raw_input("Please add your friend's name: ")
    n_friend['salutation'] = raw_input("Are they Mr. or Ms.?: ")

    n_friend['name'] = n_friend['salutation'] + " " + n_friend['name']

    n_friend['age'] = raw_input("Age?")
    n_friend['age'] = int(n_friend['age'])

    n_friend['rating'] = raw_input("Spy rating?")
    n_friend['rating'] = float(n_friend['rating'])


    if len(n_friend['name']) > 0 and n_friend['age'] > 12 :
        friends.append(n_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can,t add spy'

    return len(friends)
#decleration of select_a _friend()
def select_a_friend():
    item_number = 0
#for loop implementation
    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend['name'],
                                                   friend['age'],
                                                   friend['rating'])
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#decleration of send_message function
def send_message():
#concept of steganography to send a secret meesage
    friend_choice = select_a_friend()

    original_image = raw_input("What is the name of the image?")
    output_path = raw_input(":--")
    text = raw_input("What do you want to say? ")
    Steganography.encode(original_image, output_path, text)

    new_chat = {
        "message": text,
        "time": datetime.now(),
        "sent_by_me": True
    }

    friends[friend_choice]['chats'].append(new_chat)

    print "Your secret message image is ready!"

#decleration of read_message function
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat = {
        "message": secret_text,
        "tym": datetime.now(),
        "senbm": False
    }

    friends[sender]['chats'].append(new_chat)

    print "Your secret message has been saved!"
    print secret_text

def start_chat(spy):


    current_status_message = None


    spy_name = spy['salutation'] + " " + spy['name']


    if spy_age > 12 and spy_age < 50:


        print "Authentication complete. Welcome " + spy['name'] + " age: " + str(spy['age']) + " and rating of: " + str(spy['rating']) + " Proud to have you onboard"

        show_menu = True
#while loop implementation
        while show_menu:
            menu_choices = "What do you want to do? \n 1. Add a status update \n 2. Add a friend \n 3. Send a secret message \n 4. Read a secret message \n 5. Read Chats from a user \n 6. Close Application \n"
            menu_choice = raw_input(menu_choices)

            if len(menu_choice) > 0:
                menuchoice = int(menu_choice)

                if menuchoice == 1:
                    current_status_message = add_status(current_status_message)
                elif menu_choice == 2:
                    number_of_friends = add_friend()
                    print 'You have %d friends' % (number_of_friends)
                elif menuchoice == 3:
                    send_message()
                elif menuchoice == 4:
                    read_message()
                else:
                    show_menu = False
    else:
        print 'Sorry you are not of the correct age to be a spy'

if existing.upper() == "Y":
    #function calling
    start_chat(spy['name'],spy['age'], spy['rating'])
elif existing.upper()=="N":
    spy = {
        'name': '',
        'salutation': '',
        'age': 0,
        'rating': 0.0,
        'online': False
    }

    spy['name'] = raw_input("Welcome to spy chat, you must tell me your spy name first: ")
    spy['salutation'] = raw_input("Should I call you Mr. or Ms.?: ")

    spy['age'] = raw_input("What is your age?")
    spy['age'] = int(spy['age'])

    spy['rating'] = raw_input("What is your spy rating?")
    spy['rating'] = float(spy['rating'])

    spy_is_online = True
#function calling
    start_chat(spy['name'], spy['age'], spy['rating'])