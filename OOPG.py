# Your assignment for today is to create a parking garage class to get more familiar with Object Oriented Programming(OOP). This project would usually be a pair programming project. However, for the size our class we will have groups of 2-3. This means, that one person(The driver) will code the project while the other people(The navigators)will brainstorm and guide to a working solution.
# Each of you should share/switch these roles every 30mins-1hr (-- Or you may elect to switch "drivers" after creating specific methods of the class).

# The Initial Driver needs to Make sure to:
# download the files below, create a local folder for the project, create a github repository, commit the inital files, share the link

# Both navigators should then:
# fork the code, clone it and begin.

# The current driver MUST share their screen so the navigators can help brainstorm to a working solution.

# When code has been updated, you will need to pull down the changes.

# Here's an article on doing so -- https://stackoverflow.com/questions/3903817/pull-new-updates-from-original-github-repository-into-forked-github-repository

# Your parking gargage class should have the following methods:
# - takeTicket -Alex
# - This should decrease the amount of tickets available by 1 -Alex
# - This should decrease the amount of parkingSpaces available by 1 - Alex
# - payForParking
# - Display an input that waits for an amount from the user and store it in a variable
# - If the payment variable is not empty then (meaning the ticket has been paid) -> display a message to the user that their ticket has been paid and they have 15mins to leave
# - This should update the "currentTicket" dictionary key "paid" to True
# -leaveGarage
# - If the ticket has been paid, display a message of "Thank You, have a nice day" 
# - If the ticket has not been paid, display an input prompt for payment
# - Once paid, display message "Thank you, have a nice day!" - Alex
# - Update parkingSpaces list to increase by 1 (meaning add to the parkingSpaces list) -Alex
# - Update tickets list to increase by 1 (meaning add to the tickets list) -Alex

# You will need a few attributes as well:
# - tickets -> list
# - parkingSpaces -> list
# - currentTicket -> dictionary

# NOTE: Use VSCode for this project starting with the following files below. Also, each person in the group should list the portion of the project they were responsible for inside of the python file and inside the README file.

# By the end of this project each group/student should be able to:
# - Explain and/or demostrate using Git and Github for collaboration
# - Explain and/or demostrate creating classes
# - Explain and/or demostrate creating class methods
# - Explain and/or demostrate class instantiation


class parking_garage():
    def __init__(self,make, model):
        self.make = make 
        self.model = model
        self.current_tickets = {}
        self.payment_dictionary = {}
        self.number_of_tickets = 0
        self.number_of_parking_spaces = 0
        self.total_number_of_tickets_left = 100
        self.total_number_of_parking_spots_left = 100

    def take_a_ticket(self):
        ticket = input ('Would you like to take a parking ticket today? or quit')
        if ticket == 'quit':
            self.options()
        make = input ('What type of car do you have?')
        model = input('What model is your car?')
        color = input('What color is your car?')
        amount = input ('This will ticket will be around $5.00 is that okay? or quit')
        self.current_tickets[ticket] = amount and make and model and color
        if amount == 'quit':
            self.options()
        elif self.total_number_of_tickets_left <=1:
            print('No more tickets are available. Parking lot is full. Have a nice day')
            self.options()
        self.number_of_tickets += 1
        self.number_of_parking_spaces += 1
        self.total_number_of_tickets_left -= 1
        self.total_number_of_parking_spots_left -= 1
        print('A ticket is be printing.')
        print(f'There are a total number of parking spots left: {self.total_number_of_parking_spots_left}')
        print(f'{self.current_tickets}')
    
    def ticket_payment(self):
        ticket = input ('Would you like to pay for parking? or quit')
        amount = input ('Please pay $5.00. Enter your card and type in 5')
        if amount == '5':
            self.current_tickets[ticket] = amount
            self.number_of_tickets -= 1
            self.number_of_parking_spaces -= 1
            self.total_number_of_tickets_left += 1
            self.total_number_of_parking_spots_left += 1
            print('Thank you, have a nice day!')
        elif ticket == 'quit':
            self.options()
        else:
            print('Invalid answer. Please pay $5.00')
            self.ticket_payment()

    def employee(self):
        print(f'{self.total_number_of_parking_spots_left}')
        print(f'{self.total_number_of_parking_spots_left}')
        print(f'{self.current_tickets}')
        print(f'{self.payment_dictionary}')
        print('Thank you, have a nice day!')
    
    def quit(self):
        print('Thank you, have a nice day!')
        print(f'There are {self.total_number_of_parking_spots_left} parking spots left')


    def options(self):
        while True:
            user = input('Welcome to the parking garage you can choose through the following options: ticket, payment, employee, quit')
            if user == 'ticket':
                self.take_a_ticket()
            elif user == 'payment':
                self.ticket_payment()
            elif user == 'employee':
                self.employee()
            elif user == 'quit':
                self.quit()
                break
            else:
                print('Invalid answer please try again')


User = parking_garage('Make','Model')

User.options()


