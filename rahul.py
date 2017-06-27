#using impoet keyword for access files from another file
from spy12 import*
from steganography.steganography import Steganography
from datetime import datetime
now=datetime.now()



s_mess = ['*********my name is rahul*********','*******Good Evening****, ',' Sir']
#display a message on screen
print (" \033[4m  HELLO   \033[0m ")



qst = "*****Do you want to continue as****** " + spy.salutation + " " + spy.name + " (Y/N)? "
EXISTING= raw_input(qst)

#decleration of add status function
def add_status(current_status_message):

    updated_status_message=None

#if condition implementation
    if spy.current_status_message !=None:
        print 'Your current status message is %s \n' % (spy.current_status_message)
    else:
        print 'don\'t have any status message currently \n'

#raw_input fuction is used for taking input from user
    default = raw_input("Do you want to select from the older status (y/n)? ")

    if default.upper() == "N":
        new_status= raw_input("What status message do you want to set? ")

#len() is used which is used to return the length of string
        if len(new_status) > 0:
            s_mess.append(new_status)
            updated_status_message=new_status


    elif default.upper()=='Y':
#count is used  to set counter
        count_item=1
#implementation of for loop
        for message in s_mess:
            print '%d. %s' % (count_item, message)
            count_item=count_item + 1

        message_selection =int(raw_input("\nChoose from the above messages "))


        if len(s_mess) >= message_selection:
            updated_status_message=s_mess[message_selection - 1]

    else:
        print 'The option you chose is not valid! Press either y or n.'

    if updated_status_message :
        print 'Your updated status message is: %s' % (updated_status_message)
    else:
        print 'You current don\'t have a status update'

    return updated_status_message

#decleration of add_friend function and creation of a dictionary
def add_friend():
    new_friend = Spy('','',0,0.0)
    #accessing dictionary values
    new_friend.name = raw_input("Please add your friend's name: ")
    new_friend.salutation = raw_input("Are they Mr. or Ms.?: ")

    new_friend.name = new_friend.salutation + " " + new_friend.name

    new_friend.age = raw_input("Age?")
    new_friend.age = int(new_friend.age)

    new_friend.rating= raw_input("Spy rating?")
    new_friend.rating = float(new_friend.rating)


    if len(new_friend.name) > 0 and new_friend.age > 12 :
        friends.append(new_friend)
        print 'Friend Added!'
    else:
        print 'Sorry! Invalid entry. We can,t add spy'

    return len(friends)
#decleration of select_a _friend()
def select_a_friend():
    item_number = 0
#for loop implementation
    for friend in friends:
        print '%d. %s aged %d with rating %.2f is online' % (item_number +1, friend.name,
                                                   friend.age,
                                                   friend.rating)
        item_number = item_number + 1

    friend_choice = raw_input("Choose from your friends")

    friend_choice_position = int(friend_choice) - 1

    return friend_choice_position

#decleration of send_message function
def send_message():
#concept of steganography to send a secret meesage
    friend_choice =select_a_friend()

    Original_image = raw_input("What is the name of the image?")
    output_path ="1.jpg"
    text = raw_input("What do you want to say? ")
    Steganography.encode(Original_image,output_path,text)

    new_chat =Chat_Message(text,True)


    friends[friend_choice].chats.append(new_chat)

    print "Your secret message image is ready!"

#decleration of read_message function
def read_message():

    sender = select_a_friend()

    output_path = raw_input("What is the name of the file?")

    secret_text = Steganography.decode(output_path)

    new_chat =Chat_Message(secret_text,False)



    friends[sender].chats.append(new_chat)

    print "Your secret message has been saved!"
    print secret_text


def _CHAT_HISTORY():

    read_for = select_a_friend()



    for chat in friends[read_for].chats:
        if chat.sent_by_me:
            print '[%s] %s: %s' % (chat.time.strftime("%d %B %Y"), 'You said:', chat.message)
        else:

            print '[%s] %s said: %s' % (chat.time.strftime("%d %B %Y"), friends[read_for].name, chat.message)




def start_chat(spy):


    current_status_message = None


    spy_name = spy.salutation + " " + spy.name


    if spy.age > 12 and spy.age < 50:


        print "Authentication complete. Welcome " + spy.name+ " age: " + str(spy.age) + " and rating of: " + str(spy.rating) + " Proud to have you onboard"

        show_menu = True
#while loop implementation
        while show_menu:
            menu_choices = "what you want to do\n 1. ***Add a status update*** \n 2. ***Add a friend****\n 3.***select a friend*** \n 4. ***Send a secret message** \n 5. ***Read a secret message ****\n 6. ***read Chats from a user*** \n 7. **8Close Application** \n"
            menu_choice =int(raw_input(menu_choices))


            menuchoice = int(menu_choice)

            if menuchoice == 1:
                spy.current_status_message = add_status(current_status_message)
            elif menu_choice == 2:
                number_of_friends = add_friend()
                print 'You have %d friends added' % (number_of_friends)
            elif menu_choice==3:
                select_a_friend()

            elif menu_choice == 4:

                send_message()
            elif menu_choice == 5:
                read_message()
            elif menu_choice == 6:
                _CHAT_HISTORY()

            else:
                show_menu = False
    else:
        print '***Enter correct age of spy*****'

if EXISTING.upper() == "Y":
    #function calling
    start_chat(spy)
elif EXISTING.upper()=="N":
    spy=Spy('','',0,0.0)
    spy.name = raw_input("**** WELCOME TO SPY CHAT YOU FIRST TELL ME YOUR NAME***")
#LENGTH FUNCTION RETURN LENGTH OF STRING
    if len(spy.name)>0:

       spy.salutation = raw_input("Should I call you Mr. or Ms.?: ")

       spy.age = raw_input("**WHAT IS YOUR AGE***?")
       spy.age = int(spy.age)

       spy.rating= raw_input("***ENTER YOUR SPY RATING?***")
       spy.rating= float(spy.rating)

    spy_is_online = True
#function calling
    start_chat(spy)