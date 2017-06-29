#import function that import one files other file
#import datetime
from datetime import datetime
#decleration of class spy
class Spy:
     #use of constructor
    def __init__(self, name, salutation, age, rating):
        self.name = name
        self.salutation = salutation
        self.age = age
        self.rating = rating
        self.is_online = True
        self.chats = []
        self.current_status_message = None

#decleration of class chatmessage
class Chat_Message:
    #use of constructor

    def __init__(self,message,sent_by_me,):
        self.message = message
        self.time = datetime.now()
        self.sent_by_me = sent_by_me


spy = Spy('bond','Mr.',24,4.7)

friend_one = Spy('shivam', 'Mr.', 4.9, 27)
friend_two = Spy('satya', 'Ms.', 4.39, 21)
friend_three = Spy('Akash', 'Dr.', 4.95, 37)


friends = [friend_one, friend_two, friend_three]

